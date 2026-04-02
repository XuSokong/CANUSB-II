Attribute VB_Name = "Module1"

'1.定义初始化CAN的数据类型

Public Type VCI_INIT_CONFIG
    AccCode As Long
    AccMask As Long
    Reserved As Long
    Filter As Byte
    BusTime0  As Byte
    BusTime1  As Byte
    Mode As Byte
End Type

'2.定义CAN信息帧的数据类型。

Public Type VCI_CAN_OBJ
    ID As Long
    SendType As Byte
    ExternFlag As Byte
    RemoteFlag As Byte
    DataLen As Byte
    data(7) As Byte
End Type

Declare Function VCI_OpenDevice Lib "CAN_TO_USB.dll" (ByVal DevIndex As Long) As Long

Declare Function VCI_CloseDevice Lib "CAN_TO_USB.dll" (ByVal DevIndex As Long) As Long

Declare Function VCI_InitCan Lib "CAN_TO_USB.dll" (ByVal DevIndex As Long, ByVal CANIndex As Long, ByRef InitConfig As VCI_INIT_CONFIG) As Long

Declare Function VCI_ResetCan Lib "CAN_TO_USB.dll" (ByVal DevIndex As Long, ByVal CANIndex As Long) As Long

Declare Function VCI_Transmit Lib "CAN_TO_USB.dll" (ByVal DevIndex As Long, ByVal CANIndex As Long, ByRef SendData As VCI_CAN_OBJ) As Long

Declare Function VCI_Receive Lib "CAN_TO_USB.dll" (ByVal DevIndex As Long, ByVal CANIndex As Long, ByRef pReceive As VCI_CAN_OBJ, ByVal Length As Long, ByVal WaitTime As Long) As Long



