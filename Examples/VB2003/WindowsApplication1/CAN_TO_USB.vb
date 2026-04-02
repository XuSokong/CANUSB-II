Option Strict Off
Option Explicit On 
Module Module1
  '定义需要用到的数据结构

    Public Structure VCI_CAN_OBJ
        Dim ID As Integer
        Dim SendType As Byte
        Dim RemoteFlag As Byte
        Dim ExternFlag As Byte
        Dim DataLen As Byte
        <VBFixedArray(7)> Dim data() As Byte

        'Public Sub New(ByVal a As Byte, ByVal b As Byte)
        'End Sub
        Public Sub Initialize()     '这种数组的初始化可不可以在构造函数中实现，如下边注释中，这样在定义这个结构时就不用再实例化数组，节省时间
            ReDim data(7)
        End Sub
        'Sub New(ByVal DataLenth As Byte, ByVal ReservedLenth As Byte)
        '    ReDim data(DataLenth)
        '    ReDim Reserved(ReservedLenth)
        'End Sub
    End Structure
    Public Structure VCI_INIT_CONFIG
        Dim AccCode As Integer
        Dim AccMask As Integer
        Dim Reserved As Integer
        Dim Filter_Renamed As Byte
        Dim Timing0 As Byte
        Dim Timing1 As Byte
        Dim Mode As Byte
    End Structure

    '打开设备，DeviceInd表示设备索引号（具体见接口函数库使用手册）；
    Declare Function VCI_OpenDevice Lib "CAN_TO_USB.dll" (ByVal DeviceInd As Integer) As Integer
    '关闭设备
    Declare Function VCI_CloseDevice Lib "CAN_TO_USB.dll" (ByVal DeviceInd As Integer) As Integer
    '初始化指定的CAN
    Declare Function VCI_InitCan Lib "CAN_TO_USB.dll" (ByVal DeviceInd As Integer, ByVal CANInd As Integer, ByRef InitConfig As VCI_INIT_CONFIG) As Integer
    '获取指定接收缓冲区中接收到但尚未被读取得帧数
    Declare Function VCI_GetReceiveNum Lib "CAN_TO_USB.dll" (ByVal DeviceInd As Integer, ByVal CANInd As Integer) As Integer
    '清空指定缓冲区
    Declare Function VCI_ClearBuffer Lib "CAN_TO_USB.dll" (ByVal DeviceInd As Integer, ByVal CANInd As Integer) As Integer
    '复位CAN
    Declare Function VCI_ResetCan Lib "CAN_TO_USB.dll" (ByVal DeviceInd As Integer, ByVal CANInd As Integer) As Integer
    '向指定的的设备发送数据
    Declare Function VCI_Transmit Lib "CAN_TO_USB.dll" (ByVal DeviceInd As Integer, ByVal CANInd As Integer, ByRef Sendbuf As Byte) As Integer
    '从指定的设备读取数据
    Declare Function VCI_Receive Lib "CAN_TO_USB.dll" (ByVal DeviceInd As Integer, ByVal CANInd As Integer, ByRef Receive As Byte, ByVal length As Integer, ByVal WaitTime As Integer) As Integer

    Public Sub bytecpy(ByRef desarr() As Byte, ByVal desoff As Long, ByVal srcarr() As Byte, ByVal srcoff As Long, ByVal len As Long)
        Dim i As Long

        For i = 0 To len - 1
            desarr(desoff + i) = srcarr(i + srcoff)
        Next
    End Sub

    Public Function Transmit(ByVal DeviceInd As Integer, ByVal CANInd As Integer, ByRef Sendbuf() As VCI_CAN_OBJ) As Integer
        Dim pbuf() As Byte
        ReDim pbuf(16 - 1)
        Dim res, index, i As Integer

        index = 0
        For i = 0 To 1 - 1
            index = 16 * i
            pbuf(index) = CByte(Sendbuf(i).ID And &HFF)
            index += 1
            pbuf(index) = CByte((Sendbuf(i).ID >> 8) And &HFF)
            index += 1
            pbuf(index) = CByte((Sendbuf(i).ID >> 16) And &HFF)
            index += 1
            pbuf(index) = CByte((Sendbuf(i).ID >> 24) And &HFF)
            index += 1
            pbuf(index) = Sendbuf(i).SendType
            index += 1

            pbuf(index) = Sendbuf(i).ExternFlag '是否为远程帧
            index += 1

            pbuf(index) = Sendbuf(i).RemoteFlag '是否为扩展帧
            index += 1

            pbuf(index) = Sendbuf(i).DataLen
            index += 1
            bytecpy(pbuf, index, Sendbuf(i).data, 0, 8)
            index += 8
        Next
        Transmit = VCI_Transmit(DeviceInd, CANInd, pbuf(0))
    End Function

    Public Function Receive(ByVal DeviceInd As Integer, ByVal CANInd As Integer, ByRef Rec() As VCI_CAN_OBJ, ByVal length As Integer, ByVal WaitTime As Integer) As Integer
        Dim pbuf() As Byte
        ReDim pbuf(length * 16 - 1)
        Dim res, index, i As Integer

        res = VCI_Receive(DeviceInd, CANInd, pbuf(0), length, WaitTime)

        If (res > 0) Then
            For i = 0 To res - 1
                index = 16 * i
                Rec(i).ID = CInt(pbuf(index)) + (CInt(pbuf(index + 1)) << 8) + _
                  (CInt(pbuf(index + 2)) << 16) + (CInt(pbuf(index + 3)) << 24)
                index += 4
                Rec(i).SendType = pbuf(index)
                index += 1

                Rec(i).ExternFlag = pbuf(index) '是否为扩展帧
                index += 1

                Rec(i).RemoteFlag = pbuf(index) '是否为远程帧
                index += 1

                Rec(i).DataLen = pbuf(index)
                index += 1
                bytecpy(Rec(i).data, 0, pbuf, index, 8)
                index += 8
            Next
        End If

        Receive = res
    End Function

End Module