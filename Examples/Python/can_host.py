"""
CAN USB 上位机软件
基于 tkinter 的图形界面程序
采用MVC架构：GUI类 + 通信控制类
"""

import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
from datetime import datetime
from typing import Optional, Callable

from can_interface import CANInterface, VCI_INIT_CONFIG, VCI_CAN_OBJ, bytes_to_hex, hex_to_bytes


class CANController:
    """CAN通信控制器 - 负责所有CAN通信相关操作"""
    
    def __init__(self):
        self.can_interface: Optional[CANInterface] = None
        self.is_connected = False
        self.is_receiving = False
        self.receive_thread: Optional[threading.Thread] = None
        self.dev_index = 0
        self.can_index = 0
        
        # 回调函数
        self.on_message_received: Optional[Callable] = None
        self.on_error: Optional[Callable] = None
        
        # 统计
        self.tx_count = 0
        self.rx_count = 0
    
    def connect(self, dev_index: int, dll_path: Optional[str] = None) -> bool:
        """连接设备"""
        try:
            import os
            import shutil
            
            # 尝试查找DLL
            if dll_path is None:
                possible_paths = [
                    os.path.join(os.path.dirname(__file__), 'CAN_TO_USB.dll'),
                    os.path.join(os.path.dirname(__file__), '..', 'CAN_TO_USB.dll'),
                    'CAN_TO_USB.dll',
                ]
                for path in possible_paths:
                    if os.path.exists(path):
                        dll_path = path
                        break
                
                if dll_path is None:
                    source_dll = os.path.join('..', 'CAN_TO_USB.dll')
                    if os.path.exists(source_dll):
                        shutil.copy(source_dll, '.')
                        dll_path = 'CAN_TO_USB.dll'
            
            self.can_interface = CANInterface(dll_path)
            
            if self.can_interface.open_device(dev_index):
                self.dev_index = dev_index
                self.is_connected = True
                return True
            return False
        except Exception as e:
            if self.on_error:
                self.on_error(f"连接设备失败: {str(e)}")
            return False
    
    def disconnect(self) -> bool:
        """断开连接"""
        try:
            self.stop_receive()
            
            if self.can_interface:
                self.can_interface.close_device()
                self.can_interface = None
            
            self.is_connected = False
            self.tx_count = 0
            self.rx_count = 0
            return True
        except Exception as e:
            if self.on_error:
                self.on_error(f"断开连接失败: {str(e)}")
            return False
    
    def init_can(self, config: VCI_INIT_CONFIG, can_index: int = 0) -> bool:
        """初始化CAN"""
        try:
            if not self.can_interface:
                return False
            
            self.can_index = can_index
            
            if self.can_interface.init_can(config, can_index):
                self.can_interface.reset_can(can_index)
                return True
            return False
        except Exception as e:
            if self.on_error:
                self.on_error(f"初始化CAN失败: {str(e)}")
            return False
    
    def reset_can(self) -> bool:
        """复位CAN"""
        try:
            if self.can_interface:
                return self.can_interface.reset_can(self.can_index)
            return False
        except Exception as e:
            if self.on_error:
                self.on_error(f"复位CAN失败: {str(e)}")
            return False
    
    def transmit(self, msg: VCI_CAN_OBJ) -> bool:
        """发送数据"""
        try:
            if self.can_interface and self.can_interface.transmit(msg):
                self.tx_count += 1
                return True
            return False
        except Exception as e:
            if self.on_error:
                self.on_error(f"发送数据失败: {str(e)}")
            return False
    
    def start_receive(self):
        """开始接收"""
        if not self.is_receiving:
            self.is_receiving = True
            self.receive_thread = threading.Thread(target=self._receive_loop, daemon=True)
            self.receive_thread.start()
    
    def stop_receive(self):
        """停止接收"""
        self.is_receiving = False
    
    def _receive_loop(self):
        """接收循环"""
        while self.is_receiving and self.can_interface:
            try:
                messages = self.can_interface.receive(length=10, wait_time=100)
                
                for msg in messages:
                    self.rx_count += 1
                    if self.on_message_received:
                        self.on_message_received(msg)
                
                time.sleep(0.01)
            except Exception as e:
                print(f"接收错误: {e}")
                break
    
    def clear_buffer(self) -> bool:
        """清空缓冲区"""
        try:
            if self.can_interface:
                return self.can_interface.clear_buffer(self.can_index)
            return False
        except Exception as e:
            if self.on_error:
                self.on_error(f"清空缓冲区失败: {str(e)}")
            return False
    
    def get_baudrate_config(self, baudrate: str):
        """获取波特率配置"""
        if self.can_interface:
            return self.can_interface.get_baudrate_config(baudrate)
        return None


class CANHostGUI:
    """CAN上位机GUI - 负责界面显示和用户交互"""
    
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("CAN USB 上位机软件 v1.0")
        self.root.geometry("900x700")
        self.root.minsize(800, 600)
        
        # 通信控制器
        self.controller = CANController()
        self.controller.on_message_received = self._on_message_received
        self.controller.on_error = self._on_error
        
        # 创建界面
        self._create_widgets()
        self._create_menu()
        self._layout_widgets()
        
        # 状态更新定时器
        self._update_status()
    
    def _create_widgets(self):
        """创建界面组件"""
        # 设备连接框架（顶部栏，只保留连接按钮）
        self.frame_connection = ttk.LabelFrame(self.root, text="设备连接", padding=10)
        
        self.btn_connect_toggle = ttk.Button(self.frame_connection, text="连接设备", command=self._on_toggle_connection, width=12)
        self.btn_connect_toggle.pack(padx=20, pady=5)
        
        # 初始化通信设置默认值（用于对话框）
        self._comm_settings = {
            'dev_index': 0,
            'can_index': 0,
            'baudrate': '100K',
            'acc_code': '00000000',
            'acc_mask': 'FFFFFFFF',
            'mode': 0,  # 正常模式
            'filter': 0,  # 双滤波
            'ext_frame': False,
            'remote_frame': False,
            'send_type': 0  # 正常发送
        }
        
        # 发送数据框架
        self.frame_send = ttk.LabelFrame(self.root, text="发送数据", padding=10)
        
        ttk.Label(self.frame_send, text="帧ID:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.entry_send_id = ttk.Entry(self.frame_send, width=12)
        self.entry_send_id.insert(0, "0000000F")
        self.entry_send_id.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
        
        ttk.Label(self.frame_send, text="数据:").grid(row=0, column=2, sticky=tk.W, padx=5, pady=5)
        self.entry_send_data = ttk.Entry(self.frame_send, width=40)
        self.entry_send_data.insert(0, "01 02 03 04 05 06 07 08")
        self.entry_send_data.grid(row=0, column=3, columnspan=3, sticky=tk.W+tk.E, padx=5, pady=5)
        
        self.btn_send = ttk.Button(self.frame_send, text="发送", command=self._on_send, state=tk.DISABLED)
        self.btn_send.grid(row=0, column=6, padx=5, pady=5)
        
        self.btn_clear = ttk.Button(self.frame_send, text="清空显示", command=self._on_clear_display)
        self.btn_clear.grid(row=0, column=7, padx=5, pady=5)
        
        self.btn_clear_buffer = ttk.Button(self.frame_send, text="清空缓冲区", command=self._on_clear_buffer, state=tk.DISABLED)
        self.btn_clear_buffer.grid(row=0, column=8, padx=5, pady=5)
        # 数据显示框架
        self.frame_data = ttk.LabelFrame(self.root, text="数据记录", padding=10)
        
        # 创建表格
        columns = ('time', 'type', 'id', 'format', 'dtype', 'length', 'data')
        self.tree_data = ttk.Treeview(self.frame_data, columns=columns, show='headings', height=15)
        
        self.tree_data.heading('time', text='时间')
        self.tree_data.heading('type', text='类型')
        self.tree_data.heading('id', text='帧ID')
        self.tree_data.heading('format', text='格式')
        self.tree_data.heading('dtype', text='帧类型')
        self.tree_data.heading('length', text='长度')
        self.tree_data.heading('data', text='数据')
        
        self.tree_data.column('time', width=100, anchor=tk.CENTER)
        self.tree_data.column('type', width=50, anchor=tk.CENTER)
        self.tree_data.column('id', width=80, anchor=tk.CENTER)
        self.tree_data.column('format', width=60, anchor=tk.CENTER)
        self.tree_data.column('dtype', width=60, anchor=tk.CENTER)
        self.tree_data.column('length', width=50, anchor=tk.CENTER)
        self.tree_data.column('data', width=300, anchor=tk.W)
        
        scrollbar_y = ttk.Scrollbar(self.frame_data, orient=tk.VERTICAL, command=self.tree_data.yview)
        scrollbar_x = ttk.Scrollbar(self.frame_data, orient=tk.HORIZONTAL, command=self.tree_data.xview)
        self.tree_data.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
        
        self.tree_data.grid(row=0, column=0, sticky=tk.NSEW)
        scrollbar_y.grid(row=0, column=1, sticky=tk.NS)
        scrollbar_x.grid(row=1, column=0, sticky=tk.EW)
        
        self.frame_data.grid_rowconfigure(0, weight=1)
        self.frame_data.grid_columnconfigure(0, weight=1)
        
        # 状态栏框架
        self.frame_status = ttk.Frame(self.root, padding=5, relief=tk.SUNKEN, borderwidth=1)
        
        # 左侧状态信息
        self.lbl_status = ttk.Label(self.frame_status, text="状态: 未连接", foreground="red")
        self.lbl_status.pack(side=tk.LEFT, padx=5)
        
        ttk.Separator(self.frame_status, orient=tk.VERTICAL).pack(side=tk.LEFT, fill=tk.Y, padx=10)
        
        self.lbl_tx_count = ttk.Label(self.frame_status, text="发送: 0")
        self.lbl_tx_count.pack(side=tk.LEFT, padx=5)
        
        self.lbl_rx_count = ttk.Label(self.frame_status, text="接收: 0")
        self.lbl_rx_count.pack(side=tk.LEFT, padx=5)
        
        ttk.Separator(self.frame_status, orient=tk.VERTICAL).pack(side=tk.LEFT, fill=tk.Y, padx=10)
        
        self.lbl_device_info = ttk.Label(self.frame_status, text="设备: 无")
        self.lbl_device_info.pack(side=tk.LEFT, padx=5)
        
        # 底部状态信息栏（用于显示详细状态信息）
        self.lbl_status_info = ttk.Label(self.frame_status, text="就绪", foreground="gray")
        self.lbl_status_info.pack(side=tk.RIGHT, padx=5)
    
    def _create_menu(self):
        """创建菜单栏"""
        menubar = tk.Menu(self.root)
        
        # 设置菜单
        setting_menu = tk.Menu(menubar, tearoff=0)
        setting_menu.add_command(label="USBCAN", command=self._show_comm_settings)
        setting_menu.add_separator()
        setting_menu.add_command(label="本地路径设置", command=self._show_path_settings)
        menubar.add_cascade(label="设置", menu=setting_menu)
        
        # 帮助菜单
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="关于", command=self._show_about)
        menubar.add_cascade(label="帮助", menu=help_menu)
        
        self.root.config(menu=menubar)
    
    def _show_comm_settings(self):
        """显示通信设置对话框"""
        dialog = tk.Toplevel(self.root)
        dialog.title("USBCAN设置")
        dialog.geometry("500x450")
        dialog.resizable(False, False)
        dialog.transient(self.root)
        dialog.grab_set()
        
        # === 设备设置 ===
        frame_device = ttk.LabelFrame(dialog, text="设备设置", padding=10)
        frame_device.grid(row=0, column=0, columnspan=4, sticky=tk.W+tk.E, padx=10, pady=5)
        
        ttk.Label(frame_device, text="设备索引:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        combo_dev_index = ttk.Combobox(frame_device, values=list(range(8)), width=8, state="readonly")
        combo_dev_index.set(self._comm_settings['dev_index'])
        combo_dev_index.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
        
        ttk.Label(frame_device, text="CAN通道:").grid(row=0, column=2, sticky=tk.W, padx=5, pady=5)
        combo_can_index = ttk.Combobox(frame_device, values=[0, 1], width=8, state="readonly")
        combo_can_index.set(self._comm_settings['can_index'])
        combo_can_index.grid(row=0, column=3, sticky=tk.W, padx=5, pady=5)
        
        # === CAN参数设置 ===
        frame_can = ttk.LabelFrame(dialog, text="CAN参数设置", padding=10)
        frame_can.grid(row=1, column=0, columnspan=4, sticky=tk.W+tk.E, padx=10, pady=5)
        
        ttk.Label(frame_can, text="波特率:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        combo_baudrate = ttk.Combobox(frame_can,
            values=['5K', '10K', '20K', '40K', '50K', '80K', '100K', '125K', '200K', '250K', '400K', '500K', '666K', '800K', '1000K'],
            width=12, state="readonly")
        combo_baudrate.set(self._comm_settings['baudrate'])
        combo_baudrate.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
        
        ttk.Label(frame_can, text="验收码 (Hex):").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        entry_acc_code = ttk.Entry(frame_can, width=15)
        entry_acc_code.insert(0, self._comm_settings['acc_code'])
        entry_acc_code.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
        
        ttk.Label(frame_can, text="屏蔽码 (Hex):").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        entry_acc_mask = ttk.Entry(frame_can, width=15)
        entry_acc_mask.insert(0, self._comm_settings['acc_mask'])
        entry_acc_mask.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)
        
        ttk.Label(frame_can, text="模式:").grid(row=0, column=2, sticky=tk.W, padx=5, pady=5)
        combo_mode = ttk.Combobox(frame_can, values=["正常模式", "只听模式"], width=10, state="readonly")
        combo_mode.current(self._comm_settings['mode'])
        combo_mode.grid(row=0, column=3, sticky=tk.W, padx=5, pady=5)
        
        ttk.Label(frame_can, text="滤波方式:").grid(row=1, column=2, sticky=tk.W, padx=5, pady=5)
        combo_filter = ttk.Combobox(frame_can, values=["双滤波", "单滤波"], width=10, state="readonly")
        combo_filter.current(self._comm_settings['filter'])
        combo_filter.grid(row=1, column=3, sticky=tk.W, padx=5, pady=5)
        
        # === 发送设置 ===
        frame_send = ttk.LabelFrame(dialog, text="默认发送设置", padding=10)
        frame_send.grid(row=2, column=0, columnspan=4, sticky=tk.W+tk.E, padx=10, pady=5)
        
        var_ext_frame = tk.BooleanVar(value=self._comm_settings['ext_frame'])
        chk_ext_frame = ttk.Checkbutton(frame_send, text="扩展帧", variable=var_ext_frame)
        chk_ext_frame.grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        
        var_remote_frame = tk.BooleanVar(value=self._comm_settings['remote_frame'])
        chk_remote_frame = ttk.Checkbutton(frame_send, text="远程帧", variable=var_remote_frame)
        chk_remote_frame.grid(row=0, column=1, sticky=tk.W, padx=10, pady=5)
        
        ttk.Label(frame_send, text="发送类型:").grid(row=0, column=2, sticky=tk.W, padx=5, pady=5)
        combo_send_type = ttk.Combobox(frame_send, values=["正常发送", "单次发送"], width=10, state="readonly")
        combo_send_type.current(self._comm_settings['send_type'])
        combo_send_type.grid(row=0, column=3, sticky=tk.W, padx=5, pady=5)
        
        def on_save():
            try:
                # 验证十六进制输入
                int(entry_acc_code.get(), 16)
                int(entry_acc_mask.get(), 16)
            except ValueError:
                messagebox.showerror("错误", "验收码或屏蔽码格式错误！")
                return
            
            self._comm_settings['dev_index'] = int(combo_dev_index.get())
            self._comm_settings['can_index'] = int(combo_can_index.get())
            self._comm_settings['baudrate'] = combo_baudrate.get()
            self._comm_settings['acc_code'] = entry_acc_code.get()
            self._comm_settings['acc_mask'] = entry_acc_mask.get()
            self._comm_settings['mode'] = combo_mode.current()
            self._comm_settings['filter'] = combo_filter.current()
            self._comm_settings['ext_frame'] = var_ext_frame.get()
            self._comm_settings['remote_frame'] = var_remote_frame.get()
            self._comm_settings['send_type'] = combo_send_type.current()
            dialog.destroy()
        
        def on_cancel():
            dialog.destroy()
        
        # 按钮
        btn_frame = ttk.Frame(dialog)
        btn_frame.grid(row=3, column=0, columnspan=4, pady=20)
        
        ttk.Button(btn_frame, text="确定", command=on_save, width=10).pack(side=tk.LEFT, padx=10)
        ttk.Button(btn_frame, text="取消", command=on_cancel, width=10).pack(side=tk.LEFT, padx=10)
        
        # 居中显示
        dialog.update_idletasks()
        x = self.root.winfo_x() + (self.root.winfo_width() - dialog.winfo_width()) // 2
        y = self.root.winfo_y() + (self.root.winfo_height() - dialog.winfo_height()) // 2
        dialog.geometry(f"+{x}+{y}")
    
    def _show_path_settings(self):
        """显示路径设置对话框"""
        messagebox.showinfo("本地路径设置", "DLL路径：程序自动查找CAN_TO_USB.dll\n" +
                           "查找顺序：\n" +
                           "1. 当前目录\n" +
                           "2. 上级目录\n" +
                           "3. 系统PATH")
    
    def _show_about(self):
        """显示关于对话框"""
        messagebox.showinfo("关于", "CAN USB 上位机软件 v1.0\n\n" +
                           "基于 Python + tkinter 开发\n" +
                           "用于 USBCAN 设备通信")
    
    def _layout_widgets(self):
        """布局界面组件"""
        self.frame_connection.pack(fill=tk.X, padx=10, pady=5)
        self.frame_send.pack(fill=tk.X, padx=10, pady=5)
        self.frame_data.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        self.frame_status.pack(fill=tk.X, side=tk.BOTTOM, padx=10, pady=5)
    
    def _on_toggle_connection(self):
        """切换连接状态（连接/断开）"""
        if self.controller.is_connected:
            self._do_disconnect()
        else:
            self._do_connect()
    
    def _do_connect(self):
        """执行连接设备"""
        try:
            dev_index = self._comm_settings['dev_index']
            
            if self.controller.connect(dev_index):
                self.lbl_status.config(text="状态: 已连接", foreground="green")
                self.lbl_device_info.config(text=f"设备: CAN{dev_index}")
                
                # 更新按钮为断开状态
                self.btn_connect_toggle.config(text="断开连接")
                
                # 自动初始化CAN
                baudrate = self._comm_settings['baudrate']
                self.lbl_status_info.config(text=f"正在初始化CAN (波特率: {baudrate})...", foreground="blue")
                self.root.update()
                
                if self._auto_init_can():
                    self.lbl_status_info.config(text=f"设备 {dev_index} 连接并初始化成功 (波特率: {baudrate})", foreground="green")
                else:
                    self.lbl_status_info.config(text=f"设备 {dev_index} 连接成功，但CAN初始化失败", foreground="red")
                    messagebox.showerror("错误", f"设备 {dev_index} 连接成功，但CAN初始化失败！\n请检查配置后重新连接。")
                    self._do_disconnect()
            else:
                messagebox.showerror("错误", "连接设备失败！")
        except Exception as e:
            messagebox.showerror("错误", f"连接设备时出错: {str(e)}")
    
    def _do_disconnect(self):
        """执行断开连接"""
        try:
            self.controller.disconnect()
            
            self.lbl_status.config(text="状态: 未连接", foreground="red")
            self.lbl_device_info.config(text="设备: 无")
            
            # 更新按钮为连接状态
            self.btn_connect_toggle.config(text="连接设备")
            
            self.btn_send.config(state=tk.DISABLED)
            self.btn_clear_buffer.config(state=tk.DISABLED)
            
            # 更新状态栏
            self.lbl_status_info.config(text="已断开连接", foreground="gray")
            
            # 重置计数显示
            self.lbl_tx_count.config(text="发送: 0")
            self.lbl_rx_count.config(text="接收: 0")
            
        except Exception as e:
            self.lbl_status_info.config(text=f"断开连接出错: {str(e)}", foreground="red")
            messagebox.showerror("错误", f"断开连接时出错: {str(e)}")
    
    def _auto_init_can(self) -> bool:
        """自动初始化CAN（连接后自动调用）"""
        try:
            # 从设置中获取参数
            settings = self._comm_settings
            can_index = settings['can_index']
            baudrate = settings['baudrate']
            
            # 解析验收码和屏蔽码
            try:
                acc_code = int(settings['acc_code'], 16)
                acc_mask = int(settings['acc_mask'], 16)
            except ValueError:
                return False
            
            # 获取模式和滤波方式
            mode = settings['mode']
            filter_type = settings['filter']
            
            # 创建配置
            timing0, timing1 = self.controller.get_baudrate_config(baudrate)
            config = VCI_INIT_CONFIG(
                AccCode=acc_code,
                AccMask=acc_mask,
                Reserved=0,
                Filter=filter_type,
                Timing0=timing0,
                Timing1=timing1,
                Mode=mode
            )
            
            if self.controller.init_can(config, can_index):
                self.btn_send.config(state=tk.NORMAL)
                self.btn_clear_buffer.config(state=tk.NORMAL)
                
                # 自动开始接收
                self.controller.start_receive()
                
                return True
            else:
                return False
        except Exception:
            return False
    
    def _on_send(self):
        """发送数据"""
        try:
            # 解析帧ID
            try:
                frame_id = int(self.entry_send_id.get(), 16)
            except ValueError:
                messagebox.showerror("错误", "帧ID格式错误！")
                return
            
            # 解析数据
            data_str = self.entry_send_data.get()
            try:
                data = hex_to_bytes(data_str)
            except ValueError:
                messagebox.showerror("错误", "数据格式错误！")
                return
            
            # 从设置中获取发送参数
            settings = self._comm_settings
            
            # 创建CAN帧
            msg = VCI_CAN_OBJ(
                ID=frame_id,
                SendType=settings['send_type'],
                ExternFlag=1 if settings['ext_frame'] else 0,
                RemoteFlag=1 if settings['remote_frame'] else 0,
                DataLen=len(data),
                Data=data
            )
            
            if self.controller.transmit(msg):
                self.lbl_tx_count.config(text=f"发送: {self.controller.tx_count}")
                
                # 添加到显示
                self._add_message_to_display(
                    "TX",
                    f"{frame_id:08X}" if msg.ExternFlag else f"{frame_id:03X}",
                    "扩展" if msg.ExternFlag else "标准",
                    "远程" if msg.RemoteFlag else "数据",
                    msg.DataLen,
                    bytes_to_hex(data[:msg.DataLen])
                )
            else:
                messagebox.showerror("错误", "发送数据失败！")
        except Exception as e:
            messagebox.showerror("错误", f"发送数据时出错: {str(e)}")
    
    def _on_message_received(self, msg: VCI_CAN_OBJ):
        """接收到消息的回调"""
        # 使用after方法在主线程中更新UI
        self.root.after(0, self._update_rx_count)
        self.root.after(0, self._add_message_to_display,
            "RX",
            f"{msg.ID:08X}" if msg.ExternFlag else f"{msg.ID:03X}",
            "扩展" if msg.ExternFlag else "标准",
            "远程" if msg.RemoteFlag else "数据",
            msg.DataLen,
            bytes_to_hex(msg.Data[:msg.DataLen])
        )
    
    def _update_rx_count(self):
        """更新接收计数显示"""
        self.lbl_rx_count.config(text=f"接收: {self.controller.rx_count}")
    
    def _on_error(self, error_msg: str):
        """错误回调"""
        self.root.after(0, lambda: messagebox.showerror("错误", error_msg))
    
    def _add_message_to_display(self, msg_type: str, frame_id: str, frame_format: str, 
                                 data_type: str, length: int, data: str):
        """添加消息到显示表格（向下更新，新数据在底部）"""
        current_time = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        
        # 在末尾插入新数据（向下更新）
        self.tree_data.insert('', 'end', values=(
            current_time,
            msg_type,
            frame_id,
            frame_format,
            data_type,
            length,
            data
        ))
        
        # 限制显示行数，删除最旧的数据（顶部）
        children = self.tree_data.get_children()
        if len(children) > 1000:
            self.tree_data.delete(children[0])
        
        # 自动滚动到最新数据
        try:
            last_item = self.tree_data.get_children()[-1]
            self.tree_data.see(last_item)
        except (IndexError, tk.TclError):
            pass
    
    def _on_clear_display(self):
        """清空显示"""
        for item in self.tree_data.get_children():
            self.tree_data.delete(item)
    
    def _on_clear_buffer(self):
        """清空接收缓冲区"""
        try:
            if self.controller.clear_buffer():
                messagebox.showinfo("成功", "接收缓冲区已清空！")
            else:
                messagebox.showerror("错误", "清空缓冲区失败！")
        except Exception as e:
            messagebox.showerror("错误", f"清空缓冲区时出错: {str(e)}")
    
    def _update_status(self):
        """更新状态"""
        # 可以在这里添加周期性状态更新
        self.root.after(1000, self._update_status)
    
    def on_closing(self):
        """窗口关闭处理"""
        if self.controller.is_connected:
            self._do_disconnect()
        self.root.destroy()


def main():
    """主函数"""
    root = tk.Tk()
    app = CANHostGUI(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()


if __name__ == "__main__":
    main()
