"""
CAN TO USB 接口封装模块
用于与CAN_TO_USB.dll进行交互
"""

import ctypes
from ctypes import wintypes
from dataclasses import dataclass
from typing import List, Optional
import os
import platform
import sys


def get_program_dir():
    """获取程序所在目录，兼容开发环境和 PyInstaller 打包后的 exe"""
    if getattr(sys, 'frozen', False):
        # PyInstaller 打包后的 exe
        return os.path.dirname(sys.executable)
    else:
        # 开发环境
        return os.path.dirname(os.path.abspath(__file__))


def check_python_architecture():
    """检查Python架构是否与DLL兼容"""
    arch = platform.architecture()[0]
    if arch == '64bit':
        raise OSError(
            "检测到您使用的是64位Python，但CAN_TO_USB.dll是32位DLL。\n"
            "请使用以下方法之一解决：\n"
            "1. 安装32位Python（推荐）\n"
            "2. 从官网下载64位版本的CAN驱动\n"
            f"当前Python路径: {sys.executable}"
        )
    return arch


@dataclass
class VCI_INIT_CONFIG:
    """CAN初始化配置结构"""
    AccCode: int = 0x00000000      # 验收码
    AccMask: int = 0xFFFFFFFF      # 屏蔽码
    Reserved: int = 0              # 保留
    Filter: int = 0                # 滤波方式
    Timing0: int = 0x00            # 波特率定时器0
    Timing1: int = 0x14            # 波特率定时器1 (默认250Kbps)
    Mode: int = 0                  # 模式: 0-正常模式, 1-只听模式


@dataclass
class VCI_CAN_OBJ:
    """CAN消息帧结构"""
    ID: int = 0                    # 帧ID
    SendType: int = 0              # 发送类型: 0-正常发送, 1-单次发送
    ExternFlag: int = 0            # 扩展帧标志: 0-标准帧, 1-扩展帧
    RemoteFlag: int = 0            # 远程帧标志: 0-数据帧, 1-远程帧
    DataLen: int = 8               # 数据长度(0-8)
    Data: bytes = b'\x00' * 8      # 数据内容

    def __post_init__(self):
        if isinstance(self.Data, list):
            self.Data = bytes(self.Data)
        elif isinstance(self.Data, bytes):
            # 确保数据长度为8字节
            if len(self.Data) < 8:
                self.Data = self.Data + b'\x00' * (8 - len(self.Data))
            elif len(self.Data) > 8:
                self.Data = self.Data[:8]
        self.DataLen = min(self.DataLen, 8)


class CANInterface:
    """CAN接口类"""
    
    # 波特率配置表 (Timing0, Timing1)
    BAUDRATES = {
        '5K': (0xBF, 0xFF),
        '10K': (0x31, 0x1C),
        '20K': (0x18, 0x1C),
        '40K': (0x87, 0xFF),
        '50K': (0x09, 0x1C),
        '80K': (0x83, 0xFF),
        '100K': (0x04, 0x1C),
        '125K': (0x03, 0x1C),
        '200K': (0x81, 0xFA),
        '250K': (0x01, 0x1C),
        '400K': (0x80, 0xFA),
        '500K': (0x00, 0x1C),
        '666K': (0x80, 0xB6),
        '800K': (0x00, 0x16),
        '1000K': (0x00, 0x14),
    }
    
    def __init__(self, dll_path: Optional[str] = None):
        """
        初始化CAN接口
        :param dll_path: DLL文件路径,默认使用当前目录下的CAN_TO_USB.dll
        """
        # 检查Python架构
        check_python_architecture()
        
        if dll_path is None:
            # 尝试在不同目录查找DLL
            program_dir = get_program_dir()
            possible_paths = [
                os.path.join(program_dir, 'CAN_TO_USB.dll'),
                os.path.join(program_dir, '..', 'CAN_TO_USB.dll'),
                'CAN_TO_USB.dll',
                os.path.join('..', 'CAN_TO_USB.dll'),
            ]
            for path in possible_paths:
                if os.path.exists(path):
                    dll_path = path
                    break
        
        if dll_path and os.path.exists(dll_path):
            try:
                self.dll = ctypes.CDLL(dll_path)
            except OSError as e:
                if "WinError 193" in str(e) or "%1 不是有效的 Win32 应用程序" in str(e):
                    raise OSError(
                        "DLL加载失败：架构不匹配。\n"
                        "CAN_TO_USB.dll是32位DLL，请使用32位Python运行此程序。\n"
                        f"当前Python: {sys.executable} ({platform.architecture()[0]})"
                    )
                raise
        else:
            raise FileNotFoundError(f"找不到CAN_TO_USB.dll,请确保DLL文件在正确位置")
        
        self._setup_functions()
        self._connected = False
        self._dev_index = 0
        self._can_index = 0
    
    def _setup_functions(self):
        """设置DLL函数参数类型"""
        # VCI_OpenDevice
        self.dll.VCI_OpenDevice.argtypes = [wintypes.DWORD]
        self.dll.VCI_OpenDevice.restype = wintypes.BOOL
        
        # VCI_CloseDevice
        self.dll.VCI_CloseDevice.argtypes = [wintypes.DWORD]
        self.dll.VCI_CloseDevice.restype = wintypes.BOOL
        
        # VCI_InitCan
        self.dll.VCI_InitCan.argtypes = [wintypes.DWORD, wintypes.DWORD, wintypes.LPVOID]
        self.dll.VCI_InitCan.restype = wintypes.BOOL
        
        # VCI_ResetCan
        self.dll.VCI_ResetCan.argtypes = [wintypes.DWORD, wintypes.DWORD]
        self.dll.VCI_ResetCan.restype = wintypes.BOOL
        
        # VCI_Transmit
        self.dll.VCI_Transmit.argtypes = [wintypes.DWORD, wintypes.DWORD, wintypes.LPVOID]
        self.dll.VCI_Transmit.restype = wintypes.BOOL
        
        # VCI_Receive
        self.dll.VCI_Receive.argtypes = [wintypes.DWORD, wintypes.DWORD, wintypes.LPVOID, wintypes.DWORD, wintypes.INT]
        self.dll.VCI_Receive.restype = wintypes.DWORD
        
        # VCI_GetReceiveNum
        self.dll.VCI_GetReceiveNum.argtypes = [wintypes.DWORD, wintypes.DWORD]
        self.dll.VCI_GetReceiveNum.restype = wintypes.DWORD
        
        # VCI_ClearBuffer
        self.dll.VCI_ClearBuffer.argtypes = [wintypes.DWORD, wintypes.DWORD]
        self.dll.VCI_ClearBuffer.restype = wintypes.BOOL
        
        # VCI_ReadDevSn
        self.dll.VCI_ReadDevSn.argtypes = [wintypes.DWORD, wintypes.LPSTR]
        self.dll.VCI_ReadDevSn.restype = wintypes.BOOL
    
    def open_device(self, dev_index: int = 0) -> bool:
        """
        打开CAN设备
        :param dev_index: 设备索引(0-7)
        :return: 是否成功
        """
        result = self.dll.VCI_OpenDevice(dev_index)
        if result:
            self._dev_index = dev_index
            self._connected = True
        return bool(result)
    
    def close_device(self, dev_index: Optional[int] = None) -> bool:
        """
        关闭CAN设备
        :param dev_index: 设备索引,默认使用当前打开的设备
        :return: 是否成功
        """
        if dev_index is None:
            dev_index = self._dev_index
        result = self.dll.VCI_CloseDevice(dev_index)
        if result:
            self._connected = False
        return bool(result)
    
    def init_can(self, config: VCI_INIT_CONFIG, can_index: int = 0, dev_index: Optional[int] = None) -> bool:
        """
        初始化CAN通道
        :param config: 初始化配置
        :param can_index: CAN通道索引(0-1)
        :param dev_index: 设备索引
        :return: 是否成功
        """
        if dev_index is None:
            dev_index = self._dev_index
        
        # 创建配置结构体
        class InitConfig(ctypes.Structure):
            _fields_ = [
                ("AccCode", wintypes.DWORD),
                ("AccMask", wintypes.DWORD),
                ("Reserved", wintypes.DWORD),
                ("Filter", wintypes.BYTE),
                ("Timing0", wintypes.BYTE),
                ("Timing1", wintypes.BYTE),
                ("Mode", wintypes.BYTE),
            ]
        
        init_config = InitConfig()
        init_config.AccCode = config.AccCode
        init_config.AccMask = config.AccMask
        init_config.Reserved = config.Reserved
        init_config.Filter = config.Filter
        init_config.Timing0 = config.Timing0
        init_config.Timing1 = config.Timing1
        init_config.Mode = config.Mode
        
        result = self.dll.VCI_InitCan(dev_index, can_index, ctypes.byref(init_config))
        if result:
            self._can_index = can_index
        return bool(result)
    
    def reset_can(self, can_index: Optional[int] = None, dev_index: Optional[int] = None) -> bool:
        """
        复位CAN通道
        :param can_index: CAN通道索引
        :param dev_index: 设备索引
        :return: 是否成功
        """
        if dev_index is None:
            dev_index = self._dev_index
        if can_index is None:
            can_index = self._can_index
        return bool(self.dll.VCI_ResetCan(dev_index, can_index))
    
    def transmit(self, msg: VCI_CAN_OBJ, can_index: Optional[int] = None, dev_index: Optional[int] = None) -> bool:
        """
        发送CAN帧
        :param msg: CAN消息帧
        :param can_index: CAN通道索引
        :param dev_index: 设备索引
        :return: 是否成功
        """
        if dev_index is None:
            dev_index = self._dev_index
        if can_index is None:
            can_index = self._can_index
        
        # 创建发送结构体 (16字节)
        class CAN_OBJ(ctypes.Structure):
            _fields_ = [
                ("ID", wintypes.DWORD),
                ("SendType", wintypes.BYTE),
                ("ExternFlag", wintypes.BYTE),
                ("RemoteFlag", wintypes.BYTE),
                ("DataLen", wintypes.BYTE),
                ("Data", wintypes.BYTE * 8),
            ]
        
        can_obj = CAN_OBJ()
        can_obj.ID = msg.ID
        can_obj.SendType = msg.SendType
        can_obj.ExternFlag = msg.ExternFlag
        can_obj.RemoteFlag = msg.RemoteFlag
        can_obj.DataLen = msg.DataLen
        
        # 复制数据
        data_bytes = msg.Data if isinstance(msg.Data, bytes) else bytes(msg.Data)
        for i in range(8):
            can_obj.Data[i] = data_bytes[i] if i < len(data_bytes) else 0
        
        return bool(self.dll.VCI_Transmit(dev_index, can_index, ctypes.byref(can_obj)))
    
    def receive(self, length: int = 1, wait_time: int = 100, 
                can_index: Optional[int] = None, dev_index: Optional[int] = None) -> List[VCI_CAN_OBJ]:
        """
        接收CAN帧
        :param length: 期望接收的帧数
        :param wait_time: 等待时间(毫秒)
        :param can_index: CAN通道索引
        :param dev_index: 设备索引
        :return: 接收到的CAN帧列表
        """
        if dev_index is None:
            dev_index = self._dev_index
        if can_index is None:
            can_index = self._can_index
        
        # 创建接收缓冲区
        class CAN_OBJ(ctypes.Structure):
            _fields_ = [
                ("ID", wintypes.DWORD),
                ("SendType", wintypes.BYTE),
                ("ExternFlag", wintypes.BYTE),
                ("RemoteFlag", wintypes.BYTE),
                ("DataLen", wintypes.BYTE),
                ("Data", wintypes.BYTE * 8),
            ]
        
        buffer = (CAN_OBJ * length)()
        count = self.dll.VCI_Receive(dev_index, can_index, ctypes.byref(buffer), length, wait_time)
        
        messages = []
        for i in range(count):
            msg = VCI_CAN_OBJ(
                ID=buffer[i].ID,
                SendType=buffer[i].SendType,
                ExternFlag=buffer[i].ExternFlag,
                RemoteFlag=buffer[i].RemoteFlag,
                DataLen=buffer[i].DataLen,
                Data=bytes(buffer[i].Data)
            )
            messages.append(msg)
        
        return messages
    
    def get_receive_num(self, can_index: Optional[int] = None, dev_index: Optional[int] = None) -> int:
        """
        获取接收缓冲区中未读取的帧数
        :param can_index: CAN通道索引
        :param dev_index: 设备索引
        :return: 帧数
        """
        if dev_index is None:
            dev_index = self._dev_index
        if can_index is None:
            can_index = self._can_index
        return int(self.dll.VCI_GetReceiveNum(dev_index, can_index))
    
    def clear_buffer(self, can_index: Optional[int] = None, dev_index: Optional[int] = None) -> bool:
        """
        清空接收缓冲区
        :param can_index: CAN通道索引
        :param dev_index: 设备索引
        :return: 是否成功
        """
        if dev_index is None:
            dev_index = self._dev_index
        if can_index is None:
            can_index = self._can_index
        return bool(self.dll.VCI_ClearBuffer(dev_index, can_index))
    
    def read_device_sn(self, dev_index: Optional[int] = None) -> Optional[str]:
        """
        读取设备序列号
        :param dev_index: 设备索引
        :return: 序列号字符串,失败返回None
        """
        if dev_index is None:
            dev_index = self._dev_index
        
        buffer = ctypes.create_string_buffer(20)
        result = self.dll.VCI_ReadDevSn(dev_index, buffer)
        if result:
            return buffer.value.decode('utf-8', errors='ignore')
        return None
    
    def set_baudrate(self, baudrate: str) -> bool:
        """
        设置波特率
        :param baudrate: 波特率字符串,如'250K', '500K', '1000K'
        :return: 是否成功
        """
        if baudrate.upper() in self.BAUDRATES:
            return True  # 波特率有效,实际设置在init_can时生效
        return False
    
    def get_baudrate_config(self, baudrate: str) -> tuple:
        """
        获取波特率配置
        :param baudrate: 波特率字符串
        :return: (Timing0, Timing1)元组
        """
        return self.BAUDRATES.get(baudrate.upper(), (0x01, 0x1C))
    
    @property
    def is_connected(self) -> bool:
        """是否已连接设备"""
        return self._connected
    
    @property
    def dev_index(self) -> int:
        """当前设备索引"""
        return self._dev_index
    
    @property
    def can_index(self) -> int:
        """当前CAN通道索引"""
        return self._can_index


def create_config(baudrate: str = '250K', acc_code: int = 0x00000000, 
                  acc_mask: int = 0xFFFFFFFF, mode: int = 0, filter_type: int = 0) -> VCI_INIT_CONFIG:
    """
    创建CAN配置对象
    :param baudrate: 波特率字符串
    :param acc_code: 验收码
    :param acc_mask: 屏蔽码
    :param mode: 模式
    :param filter_type: 滤波类型
    :return: 配置对象
    """
    can_interface = CANInterface()
    timing0, timing1 = can_interface.get_baudrate_config(baudrate)
    return VCI_INIT_CONFIG(
        AccCode=acc_code,
        AccMask=acc_mask,
        Reserved=0,
        Filter=filter_type,
        Timing0=timing0,
        Timing1=timing1,
        Mode=mode
    )


def bytes_to_hex(data: bytes, separator: str = ' ') -> str:
    """将字节数据转换为十六进制字符串"""
    return separator.join(f'{b:02X}' for b in data)


def hex_to_bytes(hex_str: str) -> bytes:
    """将十六进制字符串转换为字节数据"""
    # 移除空格和其他分隔符
    hex_str = hex_str.replace(' ', '').replace('-', '')
    return bytes.fromhex(hex_str)
