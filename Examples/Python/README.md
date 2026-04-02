# CAN USB 上位机软件 (Python)

基于 Python + tkinter 的 CAN USB 上位机软件，用于与 CAN_TO_USB 设备通信。

## 文件说明

- **can_interface.py** - CAN接口封装模块，提供与CAN_TO_USB.dll的交互接口
- **can_host.py** - 主GUI应用程序，提供图形化操作界面
- **test_can.py** - 测试脚本，用于测试CAN接口功能

## 环境要求

- **Python 3.7+ (32位版本)** ⚠️ 必须使用32位Python
- Windows操作系统（依赖CAN_TO_USB.dll）
- CAN USB 设备（CANUSB-I/CANUSB-II）

### 关于32位Python的说明

CAN_TO_USB.dll 是32位动态链接库，**必须使用32位Python**才能正常加载。

如果您当前使用的是64位Python，会出现 `[WinError 193] %1 不是有效的 Win32 应用程序` 错误。

**解决方案：**

1. **下载32位Python**
   - 访问 https://www.python.org/downloads/windows/
   - 下载 `Windows installer (32-bit)` 版本
   - 安装时勾选 "Add Python to PATH"

2. **使用32位Python运行程序**
   ```bash
   # 假设32位Python安装在 C:\Python32
   C:\Python32\python.exe can_host.py
   ```

3. **或者创建虚拟环境**
   ```bash
   C:\Python32\python.exe -m venv venv32
   venv32\Scripts\activate
   python can_host.py
   ```

## 使用方法

### 1. 准备DLL文件

确保以下DLL文件在程序目录或上级目录中：
- CAN_TO_USB.dll
- SiUSBXp.dll

### 2. 运行GUI程序

```bash
python can_host.py
```

### 3. 运行测试脚本

```bash
python test_can.py
```

## 界面说明

### 设备连接
- **设备索引**: 选择设备编号（0-7）
- **CAN通道**: 选择CAN通道（0或1）
- **连接设备**: 打开CAN设备
- **断开连接**: 关闭CAN设备

### CAN配置
- **波特率**: 选择通信波特率（5K-1000K）
- **验收码**: 设置验收过滤码（十六进制）
- **屏蔽码**: 设置验收屏蔽码（十六进制）
- **模式**: 正常模式/只听模式
- **滤波方式**: 双滤波/单滤波
- **初始化CAN**: 应用配置并初始化
- **复位CAN**: 复位CAN控制器

### 发送数据
- **帧ID**: 设置CAN帧ID（十六进制）
- **扩展帧**: 勾选使用29位扩展帧ID
- **远程帧**: 勾选发送远程帧
- **发送类型**: 正常发送/单次发送
- **数据**: 发送数据（十六进制，空格分隔）
- **发送**: 发送CAN帧

### 接收控制
- **开始接收**: 启动接收线程
- **停止接收**: 停止接收线程
- **清空显示**: 清空数据记录表格
- **清空缓冲区**: 清空硬件接收缓冲区

### 数据记录
- 显示发送和接收的CAN帧信息
- 包括时间、类型、帧ID、格式、帧类型、长度和数据

## API接口说明

### CANInterface 类

```python
from can_interface import CANInterface, VCI_INIT_CONFIG, VCI_CAN_OBJ

# 创建接口实例
can = CANInterface()

# 打开设备
can.open_device(dev_index=0)

# 初始化CAN
config = VCI_INIT_CONFIG(
    AccCode=0x00000000,
    AccMask=0xFFFFFFFF,
    Timing0=0x01,
    Timing1=0x1C,
    Mode=0
)
can.init_can(config, can_index=0)

# 复位CAN
can.reset_can(can_index=0)

# 发送数据
msg = VCI_CAN_OBJ(
    ID=0x123,
    SendType=0,
    ExternFlag=0,
    RemoteFlag=0,
    DataLen=8,
    Data=b'\x01\x02\x03\x04\x05\x06\x07\x08'
)
can.transmit(msg, can_index=0)

# 接收数据
messages = can.receive(length=10, wait_time=100)

# 关闭设备
can.close_device()
```

## 波特率配置

| 波特率 | Timing0 | Timing1 |
|--------|---------|---------|
| 5K     | 0xBF    | 0xFF    |
| 10K    | 0x31    | 0x1C    |
| 20K    | 0x18    | 0x1C    |
| 50K    | 0x09    | 0x1C    |
| 100K   | 0x04    | 0x1C    |
| 125K   | 0x03    | 0x1C    |
| 250K   | 0x01    | 0x1C    |
| 500K   | 0x00    | 0x1C    |
| 800K   | 0x00    | 0x16    |
| 1000K  | 0x00    | 0x14    |

## 注意事项

1. 确保设备驱动已正确安装
2. 使用前请检查DLL文件路径
3. 发送/接收数据长度最大为8字节
4. 标准帧ID范围为0x000-0x7FF
5. 扩展帧ID范围为0x00000000-0x1FFFFFFF
