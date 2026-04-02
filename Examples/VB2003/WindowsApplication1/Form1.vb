Option Strict Off
Option Explicit On 
Imports VB = Microsoft.VisualBasic


Public Class Form1
    Inherits System.Windows.Forms.Form

#Region " Windows 窗体设计器生成的代码 "

    Public Sub New()
        MyBase.New()

        '该调用是 Windows 窗体设计器所必需的。
        InitializeComponent()

        '在 InitializeComponent() 调用之后添加任何初始化

    End Sub

    '窗体重写 dispose 以清理组件列表。
    Protected Overloads Overrides Sub Dispose(ByVal disposing As Boolean)
        If disposing Then
            If Not (components Is Nothing) Then
                components.Dispose()
            End If
        End If
        MyBase.Dispose(disposing)
    End Sub

    'Windows 窗体设计器所必需的
    Private components As System.ComponentModel.IContainer

    '注意: 以下过程是 Windows 窗体设计器所必需的
    '可以使用 Windows 窗体设计器修改此过程。
    '不要使用代码编辑器修改它。
    Friend WithEvents GroupBox1 As System.Windows.Forms.GroupBox
    Friend WithEvents Label1 As System.Windows.Forms.Label
    Friend WithEvents Label2 As System.Windows.Forms.Label
    Friend WithEvents GroupBox2 As System.Windows.Forms.GroupBox
    Friend WithEvents GroupBox3 As System.Windows.Forms.GroupBox
    Friend WithEvents GroupBox4 As System.Windows.Forms.GroupBox
    Friend WithEvents Label3 As System.Windows.Forms.Label
    Friend WithEvents Label4 As System.Windows.Forms.Label
    Friend WithEvents Label5 As System.Windows.Forms.Label
    Friend WithEvents Label6 As System.Windows.Forms.Label
    Friend WithEvents Label7 As System.Windows.Forms.Label
    Friend WithEvents Label8 As System.Windows.Forms.Label
    Friend WithEvents Label9 As System.Windows.Forms.Label
    Friend WithEvents Label10 As System.Windows.Forms.Label
    Friend WithEvents Label11 As System.Windows.Forms.Label
    Friend WithEvents Label12 As System.Windows.Forms.Label
    Friend WithEvents Label13 As System.Windows.Forms.Label
    Friend WithEvents butSend As System.Windows.Forms.Button
    Friend WithEvents cboMode As System.Windows.Forms.ComboBox
    Friend WithEvents txtTimer1 As System.Windows.Forms.TextBox
    Friend WithEvents txtTimer0 As System.Windows.Forms.TextBox
    Friend WithEvents cboFilterMode As System.Windows.Forms.ComboBox
    Friend WithEvents txtScreenCode As System.Windows.Forms.TextBox
    Friend WithEvents txtCheckCode As System.Windows.Forms.TextBox
    Friend WithEvents cboCANNum As System.Windows.Forms.ComboBox
    Friend WithEvents cboIndexNum As System.Windows.Forms.ComboBox
    Friend WithEvents txtFrameID As System.Windows.Forms.TextBox
    Friend WithEvents cboFrameFormat As System.Windows.Forms.ComboBox
    Friend WithEvents cboFrameType As System.Windows.Forms.ComboBox
    Friend WithEvents txtDate As System.Windows.Forms.TextBox
    Friend WithEvents cboSendFormat As System.Windows.Forms.ComboBox
    Friend WithEvents butReplacement As System.Windows.Forms.Button
    Friend WithEvents lstInfo As System.Windows.Forms.ListBox
    Friend WithEvents tmrRead As System.Windows.Forms.Timer
    Friend WithEvents butConnect As System.Windows.Forms.Button
    <System.Diagnostics.DebuggerStepThrough()> Private Sub InitializeComponent()
        Me.components = New System.ComponentModel.Container
        Me.GroupBox1 = New System.Windows.Forms.GroupBox
        Me.GroupBox2 = New System.Windows.Forms.GroupBox
        Me.cboMode = New System.Windows.Forms.ComboBox
        Me.Label8 = New System.Windows.Forms.Label
        Me.txtTimer1 = New System.Windows.Forms.TextBox
        Me.Label7 = New System.Windows.Forms.Label
        Me.txtTimer0 = New System.Windows.Forms.TextBox
        Me.Label6 = New System.Windows.Forms.Label
        Me.cboFilterMode = New System.Windows.Forms.ComboBox
        Me.Label5 = New System.Windows.Forms.Label
        Me.txtScreenCode = New System.Windows.Forms.TextBox
        Me.Label4 = New System.Windows.Forms.Label
        Me.txtCheckCode = New System.Windows.Forms.TextBox
        Me.Label3 = New System.Windows.Forms.Label
        Me.cboCANNum = New System.Windows.Forms.ComboBox
        Me.Label2 = New System.Windows.Forms.Label
        Me.cboIndexNum = New System.Windows.Forms.ComboBox
        Me.Label1 = New System.Windows.Forms.Label
        Me.GroupBox3 = New System.Windows.Forms.GroupBox
        Me.butSend = New System.Windows.Forms.Button
        Me.txtFrameID = New System.Windows.Forms.TextBox
        Me.Label13 = New System.Windows.Forms.Label
        Me.cboFrameFormat = New System.Windows.Forms.ComboBox
        Me.Label12 = New System.Windows.Forms.Label
        Me.cboFrameType = New System.Windows.Forms.ComboBox
        Me.Label11 = New System.Windows.Forms.Label
        Me.txtDate = New System.Windows.Forms.TextBox
        Me.Label10 = New System.Windows.Forms.Label
        Me.cboSendFormat = New System.Windows.Forms.ComboBox
        Me.Label9 = New System.Windows.Forms.Label
        Me.butReplacement = New System.Windows.Forms.Button
        Me.GroupBox4 = New System.Windows.Forms.GroupBox
        Me.lstInfo = New System.Windows.Forms.ListBox
        Me.tmrRead = New System.Windows.Forms.Timer(Me.components)
        Me.butConnect = New System.Windows.Forms.Button
        Me.GroupBox1.SuspendLayout()
        Me.GroupBox2.SuspendLayout()
        Me.GroupBox3.SuspendLayout()
        Me.GroupBox4.SuspendLayout()
        Me.SuspendLayout()
        '
        'GroupBox1
        '
        Me.GroupBox1.Controls.Add(Me.GroupBox2)
        Me.GroupBox1.Controls.Add(Me.cboCANNum)
        Me.GroupBox1.Controls.Add(Me.Label2)
        Me.GroupBox1.Controls.Add(Me.cboIndexNum)
        Me.GroupBox1.Controls.Add(Me.Label1)
        Me.GroupBox1.Location = New System.Drawing.Point(8, 8)
        Me.GroupBox1.Name = "GroupBox1"
        Me.GroupBox1.Size = New System.Drawing.Size(480, 144)
        Me.GroupBox1.TabIndex = 0
        Me.GroupBox1.TabStop = False
        Me.GroupBox1.Text = "设备参数"
        '
        'GroupBox2
        '
        Me.GroupBox2.Controls.Add(Me.cboMode)
        Me.GroupBox2.Controls.Add(Me.Label8)
        Me.GroupBox2.Controls.Add(Me.txtTimer1)
        Me.GroupBox2.Controls.Add(Me.Label7)
        Me.GroupBox2.Controls.Add(Me.txtTimer0)
        Me.GroupBox2.Controls.Add(Me.Label6)
        Me.GroupBox2.Controls.Add(Me.cboFilterMode)
        Me.GroupBox2.Controls.Add(Me.Label5)
        Me.GroupBox2.Controls.Add(Me.txtScreenCode)
        Me.GroupBox2.Controls.Add(Me.Label4)
        Me.GroupBox2.Controls.Add(Me.txtCheckCode)
        Me.GroupBox2.Controls.Add(Me.Label3)
        Me.GroupBox2.Location = New System.Drawing.Point(8, 56)
        Me.GroupBox2.Name = "GroupBox2"
        Me.GroupBox2.Size = New System.Drawing.Size(464, 80)
        Me.GroupBox2.TabIndex = 5
        Me.GroupBox2.TabStop = False
        Me.GroupBox2.Text = "初始化CAN参数"
        '
        'cboMode
        '
        Me.cboMode.ItemHeight = 12
        Me.cboMode.Location = New System.Drawing.Point(376, 48)
        Me.cboMode.Name = "cboMode"
        Me.cboMode.Size = New System.Drawing.Size(80, 20)
        Me.cboMode.TabIndex = 11
        '
        'Label8
        '
        Me.Label8.ImeMode = System.Windows.Forms.ImeMode.NoControl
        Me.Label8.Location = New System.Drawing.Point(336, 50)
        Me.Label8.Name = "Label8"
        Me.Label8.Size = New System.Drawing.Size(48, 16)
        Me.Label8.TabIndex = 10
        Me.Label8.Text = "模式："
        '
        'txtTimer1
        '
        Me.txtTimer1.Location = New System.Drawing.Point(233, 47)
        Me.txtTimer1.Name = "txtTimer1"
        Me.txtTimer1.Size = New System.Drawing.Size(63, 21)
        Me.txtTimer1.TabIndex = 9
        Me.txtTimer1.Text = "1c"
        '
        'Label7
        '
        Me.Label7.ImeMode = System.Windows.Forms.ImeMode.NoControl
        Me.Label7.Location = New System.Drawing.Point(158, 50)
        Me.Label7.Name = "Label7"
        Me.Label7.Size = New System.Drawing.Size(73, 16)
        Me.Label7.TabIndex = 8
        Me.Label7.Text = "定时器1：0x"
        '
        'txtTimer0
        '
        Me.txtTimer0.Location = New System.Drawing.Point(88, 48)
        Me.txtTimer0.Name = "txtTimer0"
        Me.txtTimer0.Size = New System.Drawing.Size(56, 21)
        Me.txtTimer0.TabIndex = 7
        Me.txtTimer0.Text = "00"
        '
        'Label6
        '
        Me.Label6.ImeMode = System.Windows.Forms.ImeMode.NoControl
        Me.Label6.Location = New System.Drawing.Point(10, 48)
        Me.Label6.Name = "Label6"
        Me.Label6.Size = New System.Drawing.Size(80, 16)
        Me.Label6.TabIndex = 6
        Me.Label6.Text = "定时器0：0x"
        '
        'cboFilterMode
        '
        Me.cboFilterMode.ItemHeight = 12
        Me.cboFilterMode.Location = New System.Drawing.Point(376, 17)
        Me.cboFilterMode.Name = "cboFilterMode"
        Me.cboFilterMode.Size = New System.Drawing.Size(80, 20)
        Me.cboFilterMode.TabIndex = 5
        '
        'Label5
        '
        Me.Label5.ImeMode = System.Windows.Forms.ImeMode.NoControl
        Me.Label5.Location = New System.Drawing.Point(312, 20)
        Me.Label5.Name = "Label5"
        Me.Label5.Size = New System.Drawing.Size(72, 16)
        Me.Label5.TabIndex = 4
        Me.Label5.Text = "滤波方式："
        '
        'txtScreenCode
        '
        Me.txtScreenCode.Location = New System.Drawing.Point(233, 16)
        Me.txtScreenCode.Name = "txtScreenCode"
        Me.txtScreenCode.Size = New System.Drawing.Size(64, 21)
        Me.txtScreenCode.TabIndex = 3
        Me.txtScreenCode.Text = "FFFFFFFF"
        '
        'Label4
        '
        Me.Label4.ImeMode = System.Windows.Forms.ImeMode.NoControl
        Me.Label4.Location = New System.Drawing.Point(164, 19)
        Me.Label4.Name = "Label4"
        Me.Label4.Size = New System.Drawing.Size(68, 16)
        Me.Label4.TabIndex = 2
        Me.Label4.Text = "屏蔽码：0x"
        '
        'txtCheckCode
        '
        Me.txtCheckCode.Location = New System.Drawing.Point(88, 14)
        Me.txtCheckCode.Name = "txtCheckCode"
        Me.txtCheckCode.Size = New System.Drawing.Size(56, 21)
        Me.txtCheckCode.TabIndex = 1
        Me.txtCheckCode.Text = "00000000"
        '
        'Label3
        '
        Me.Label3.ImeMode = System.Windows.Forms.ImeMode.NoControl
        Me.Label3.Location = New System.Drawing.Point(16, 17)
        Me.Label3.Name = "Label3"
        Me.Label3.Size = New System.Drawing.Size(72, 16)
        Me.Label3.TabIndex = 0
        Me.Label3.Text = "验收码：0x"
        '
        'cboCANNum
        '
        Me.cboCANNum.ItemHeight = 12
        Me.cboCANNum.Location = New System.Drawing.Point(256, 24)
        Me.cboCANNum.Name = "cboCANNum"
        Me.cboCANNum.Size = New System.Drawing.Size(64, 20)
        Me.cboCANNum.TabIndex = 3
        '
        'Label2
        '
        Me.Label2.ImeMode = System.Windows.Forms.ImeMode.NoControl
        Me.Label2.Location = New System.Drawing.Point(176, 24)
        Me.Label2.Name = "Label2"
        Me.Label2.Size = New System.Drawing.Size(72, 15)
        Me.Label2.TabIndex = 2
        Me.Label2.Text = "第几路CAN："
        '
        'cboIndexNum
        '
        Me.cboIndexNum.ItemHeight = 12
        Me.cboIndexNum.Location = New System.Drawing.Point(96, 21)
        Me.cboIndexNum.Name = "cboIndexNum"
        Me.cboIndexNum.Size = New System.Drawing.Size(64, 20)
        Me.cboIndexNum.TabIndex = 1
        '
        'Label1
        '
        Me.Label1.ImeMode = System.Windows.Forms.ImeMode.NoControl
        Me.Label1.Location = New System.Drawing.Point(16, 24)
        Me.Label1.Name = "Label1"
        Me.Label1.Size = New System.Drawing.Size(80, 16)
        Me.Label1.TabIndex = 0
        Me.Label1.Text = "设备索引号："
        '
        'GroupBox3
        '
        Me.GroupBox3.Controls.Add(Me.butSend)
        Me.GroupBox3.Controls.Add(Me.txtFrameID)
        Me.GroupBox3.Controls.Add(Me.Label13)
        Me.GroupBox3.Controls.Add(Me.cboFrameFormat)
        Me.GroupBox3.Controls.Add(Me.Label12)
        Me.GroupBox3.Controls.Add(Me.cboFrameType)
        Me.GroupBox3.Controls.Add(Me.Label11)
        Me.GroupBox3.Controls.Add(Me.txtDate)
        Me.GroupBox3.Controls.Add(Me.Label10)
        Me.GroupBox3.Controls.Add(Me.cboSendFormat)
        Me.GroupBox3.Controls.Add(Me.Label9)
        Me.GroupBox3.Location = New System.Drawing.Point(8, 158)
        Me.GroupBox3.Name = "GroupBox3"
        Me.GroupBox3.Size = New System.Drawing.Size(576, 82)
        Me.GroupBox3.TabIndex = 1
        Me.GroupBox3.TabStop = False
        Me.GroupBox3.Text = "发送数据帧"
        '
        'butSend
        '
        Me.butSend.ImeMode = System.Windows.Forms.ImeMode.NoControl
        Me.butSend.Location = New System.Drawing.Point(368, 48)
        Me.butSend.Name = "butSend"
        Me.butSend.Size = New System.Drawing.Size(56, 24)
        Me.butSend.TabIndex = 10
        Me.butSend.Text = "发送"
        '
        'txtFrameID
        '
        Me.txtFrameID.Location = New System.Drawing.Point(456, 17)
        Me.txtFrameID.Name = "txtFrameID"
        Me.txtFrameID.Size = New System.Drawing.Size(80, 21)
        Me.txtFrameID.TabIndex = 9
        Me.txtFrameID.Text = "00000080"
        '
        'Label13
        '
        Me.Label13.ImeMode = System.Windows.Forms.ImeMode.NoControl
        Me.Label13.Location = New System.Drawing.Point(414, 21)
        Me.Label13.Name = "Label13"
        Me.Label13.Size = New System.Drawing.Size(48, 16)
        Me.Label13.TabIndex = 8
        Me.Label13.Text = "帧ID："
        '
        'cboFrameFormat
        '
        Me.cboFrameFormat.ItemHeight = 12
        Me.cboFrameFormat.Location = New System.Drawing.Point(339, 17)
        Me.cboFrameFormat.Name = "cboFrameFormat"
        Me.cboFrameFormat.Size = New System.Drawing.Size(64, 20)
        Me.cboFrameFormat.TabIndex = 7
        '
        'Label12
        '
        Me.Label12.ImeMode = System.Windows.Forms.ImeMode.NoControl
        Me.Label12.Location = New System.Drawing.Point(287, 21)
        Me.Label12.Name = "Label12"
        Me.Label12.Size = New System.Drawing.Size(64, 16)
        Me.Label12.TabIndex = 6
        Me.Label12.Text = "帧格式："
        '
        'cboFrameType
        '
        Me.cboFrameType.ItemHeight = 12
        Me.cboFrameType.Location = New System.Drawing.Point(210, 17)
        Me.cboFrameType.Name = "cboFrameType"
        Me.cboFrameType.Size = New System.Drawing.Size(72, 20)
        Me.cboFrameType.TabIndex = 5
        '
        'Label11
        '
        Me.Label11.ImeMode = System.Windows.Forms.ImeMode.NoControl
        Me.Label11.Location = New System.Drawing.Point(158, 22)
        Me.Label11.Name = "Label11"
        Me.Label11.Size = New System.Drawing.Size(64, 16)
        Me.Label11.TabIndex = 4
        Me.Label11.Text = "帧类型："
        '
        'txtDate
        '
        Me.txtDate.Location = New System.Drawing.Point(72, 48)
        Me.txtDate.Name = "txtDate"
        Me.txtDate.Size = New System.Drawing.Size(280, 21)
        Me.txtDate.TabIndex = 3
        Me.txtDate.Text = "01 02 03 04 05 06 07 08 "
        '
        'Label10
        '
        Me.Label10.ImeMode = System.Windows.Forms.ImeMode.NoControl
        Me.Label10.Location = New System.Drawing.Point(31, 48)
        Me.Label10.Name = "Label10"
        Me.Label10.Size = New System.Drawing.Size(48, 16)
        Me.Label10.TabIndex = 2
        Me.Label10.Text = "数据："
        '
        'cboSendFormat
        '
        Me.cboSendFormat.ItemHeight = 12
        Me.cboSendFormat.Location = New System.Drawing.Point(71, 17)
        Me.cboSendFormat.Name = "cboSendFormat"
        Me.cboSendFormat.Size = New System.Drawing.Size(80, 20)
        Me.cboSendFormat.TabIndex = 1
        '
        'Label9
        '
        Me.Label9.ImeMode = System.Windows.Forms.ImeMode.NoControl
        Me.Label9.Location = New System.Drawing.Point(8, 19)
        Me.Label9.Name = "Label9"
        Me.Label9.Size = New System.Drawing.Size(80, 16)
        Me.Label9.TabIndex = 0
        Me.Label9.Text = "发送格式："
        '
        'butReplacement
        '
        Me.butReplacement.ImeMode = System.Windows.Forms.ImeMode.NoControl
        Me.butReplacement.Location = New System.Drawing.Point(512, 64)
        Me.butReplacement.Name = "butReplacement"
        Me.butReplacement.Size = New System.Drawing.Size(64, 24)
        Me.butReplacement.TabIndex = 3
        Me.butReplacement.Text = "复位CAN"
        '
        'GroupBox4
        '
        Me.GroupBox4.Controls.Add(Me.lstInfo)
        Me.GroupBox4.Location = New System.Drawing.Point(8, 248)
        Me.GroupBox4.Name = "GroupBox4"
        Me.GroupBox4.Size = New System.Drawing.Size(576, 160)
        Me.GroupBox4.TabIndex = 4
        Me.GroupBox4.TabStop = False
        Me.GroupBox4.Text = "信息"
        '
        'lstInfo
        '
        Me.lstInfo.ItemHeight = 12
        Me.lstInfo.Location = New System.Drawing.Point(8, 17)
        Me.lstInfo.Name = "lstInfo"
        Me.lstInfo.Size = New System.Drawing.Size(560, 124)
        Me.lstInfo.TabIndex = 0
        '
        'tmrRead
        '
        '
        'butConnect
        '
        Me.butConnect.ImeMode = System.Windows.Forms.ImeMode.NoControl
        Me.butConnect.Location = New System.Drawing.Point(512, 24)
        Me.butConnect.Name = "butConnect"
        Me.butConnect.Size = New System.Drawing.Size(64, 24)
        Me.butConnect.TabIndex = 5
        Me.butConnect.Text = "连接设备"
        '
        'Form1
        '
        Me.AutoScaleBaseSize = New System.Drawing.Size(6, 14)
        Me.ClientSize = New System.Drawing.Size(592, 413)
        Me.Controls.Add(Me.butConnect)
        Me.Controls.Add(Me.GroupBox4)
        Me.Controls.Add(Me.butReplacement)
        Me.Controls.Add(Me.GroupBox3)
        Me.Controls.Add(Me.GroupBox1)
        Me.MaximizeBox = False
        Me.MinimizeBox = False
        Me.Name = "Form1"
        Me.Text = "CANUSB-I/II Tester"
        Me.GroupBox1.ResumeLayout(False)
        Me.GroupBox2.ResumeLayout(False)
        Me.GroupBox3.ResumeLayout(False)
        Me.GroupBox4.ResumeLayout(False)
        Me.ResumeLayout(False)

    End Sub

#End Region


    Public m_devtype As Integer
    Public m_connect As Byte
    Public m_devind As Integer
    Public m_cannum As Integer
    Public SendType, frameformat As Object
    Public frametype As Byte
    Public ID As Integer
    Public data(7) As Byte
    Dim frameinfo(49) As VCI_CAN_OBJ

    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        F_Init(1)
    End Sub

    Public Function F_Init(ByVal inp As Byte) As Byte

        m_connect = 0
        m_cannum = 0

        Dim i As Integer
        '初始化Combobox控件
        For i = 0 To 7
            cboIndexNum.Items.Add(i)
        Next
        cboCANNum.Items.Add(0)
        cboCANNum.Items.Add(1)
        cboFilterMode.Items.Add("单滤波")
        cboFilterMode.Items.Add("双滤波")
        cboMode.Items.Add("正常模式")
        cboMode.Items.Add("只听模式")
        cboSendFormat.Items.Add("正常发送")
        cboSendFormat.Items.Add("自发自收")
        cboFrameType.Items.Add("标准帧")
        cboFrameType.Items.Add("扩展帧")
        cboFrameFormat.Items.Add("数据帧")
        cboFrameFormat.Items.Add("远程帧")
        tmrRead.Enabled = False
        cboIndexNum.SelectedIndex = 0
        cboCANNum.SelectedIndex = 0
        cboSendFormat.SelectedIndex = 1
        cboFrameType.SelectedIndex = 0
        cboFrameFormat.SelectedIndex = 0
        cboFilterMode.SelectedIndex = 0
        cboMode.SelectedIndex = 0

        Return 0
    End Function

    Private Sub butReplacement_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles butReplacement.Click
        F_Reset(1)
    End Sub

    Public Function F_Reset(ByVal inp As Byte) As Byte
        Dim ret As Byte
        If m_connect = 0 Then
            If inp = 1 Then
                MsgBox("请先打开端口")
            End If
            ret = 21
            Exit Function
        End If

        If VCI_ResetCan(m_devtype, m_cannum) <> 1 Then
            If inp = 1 Then
                MsgBox("复位CAN错误")
            End If
            ret = 32
        Else
            If inp = 1 Then
                lstInfo.Items.Add("复位CAN成功")
            End If
            ret = 0
        End If

        Return ret
    End Function

    Private Sub butSend_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles butSend.Click
        F_Send(1)
    End Sub

    Public Function F_Send(ByVal inp As Byte) As Byte
        Dim ret As Byte
        Dim j As Object
        Dim i As Object
        Dim strdata As Object

        If m_connect = 0 Then
            If inp = 1 Then
                MsgBox("请先打开端口")
            End If
            ret = 21
            Exit Function
        End If

        Dim frameinfo(0) As VCI_CAN_OBJ
        frameinfo(0).Initialize()

        Dim str As String

        SendType = cboSendFormat.SelectedIndex
        frameformat = cboFrameFormat.SelectedIndex
        frametype = cboFrameType.SelectedIndex
        str = "&H"
        str = str + txtFrameID.Text
        ID = Val(str)
        str = txtDate.Text

        strdata = " "
        i = 0
        For i = 0 To 7
            strdata = VB.Left(str, 2)
            If Len(strdata) = 0 Then
                Exit For
            End If
            str = VB.Right(str, Len(str) - 3)
            data(i) = Val("&H" + strdata)
        Next

        frameinfo(0).DataLen = i
        frameinfo(0).ExternFlag = frametype
        frameinfo(0).RemoteFlag = frameformat
        frameinfo(0).SendType = SendType
        frameinfo(0).ID = ID
        For j = 0 To i - 1
            frameinfo(0).data(j) = data(j)
        Next

        If Transmit(m_devind, m_cannum, frameinfo) <> 1 Then
            If inp = 1 Then
                MsgBox("发送数据失败")
            End If
            ret = 42
        Else
            If inp = 1 Then
                lstInfo.Items.Add("发送数据成功")
            End If
            ret = 0
        End If

        Return ret
    End Function


    Private Sub tmrRead_Tick(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles tmrRead.Tick
        tmrRead.Enabled = False
        F_Timer(1)
        tmrRead.Enabled = True
    End Sub

    Public Function F_Timer(ByVal inp As Byte) As Byte
        Dim j, k As Object
        Dim tmpstr As Object
        Dim i As Object

        If m_connect = 0 Then
            tmrRead.Enabled = True
            Exit Function
        End If

        Dim length As Long
        Dim SendFrame(49) As VCI_CAN_OBJ        '接受数组长度50
        For i = 0 To 49
            SendFrame(i).Initialize()
        Next

        Dim str, str1, str2, str3 As String
        length = Receive(m_devind, m_cannum, SendFrame, 50, 10)
        If length <= 0 Then
            tmrRead.Enabled = True '
            Exit Function
        End If

        For i = 0 To length - 1
            str = "接收到数据帧:  "
            str1 = ""

            tmpstr = "  帧ID:0x" + Hex(SendFrame(i).ID)
            str = str + tmpstr

            str1 = str1 + Hex(SendFrame(i).ID)

            str = str + "  帧类型:"
            If SendFrame(i).ExternFlag = 0 Then
                tmpstr = "标准帧 "
            Else
                tmpstr = "扩展帧 "
            End If

            str = str + tmpstr

            str = str + "  帧格式:"

            If SendFrame(i).RemoteFlag = 0 Then
                tmpstr = "数据帧 "
            Else
                tmpstr = "远程帧 "
            End If

            str = str + tmpstr

            If inp = 1 Then
                lstInfo.Items.Add(str)
            End If

            If SendFrame(i).RemoteFlag = 0 Then
                str = "  数据:"
                str2 = ""
                If SendFrame(i).DataLen > 8 Then
                    SendFrame(i).DataLen = 8
                End If

                For j = 0 To SendFrame(i).DataLen - 1
                    tmpstr = Hex(SendFrame(i).data(j)) + " "
                    str = str + tmpstr
                    str2 = str2 + tmpstr
                Next

                lstInfo.Items.Add(str)
            End If

        Next

        Return 0

    End Function

    Private Sub butConnect_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles butConnect.Click
        F_Conn(1)
    End Sub

    Public Function F_Conn(ByVal inp As Byte) As Byte
        Dim ret, cando As Short
        Dim index As Integer
        Dim cannum As Integer
        Dim code As Object
        Dim mask As Integer
        Dim Timing0, Timing1, filtertype As Object
        Dim Mode As Byte
        Dim InitConfig As VCI_INIT_CONFIG

        ret = 0
        cando = 0

        If m_connect = 1 Then
            m_connect = 0
            If inp = 1 Then
                butConnect.Text = "连接设备"
            End If
            ret = 11
            VCI_CloseDevice(m_devind)
            'Exit Function
        End If

        If ret = 0 Then
            If cboIndexNum.SelectedIndex <> -1 And cboCANNum.SelectedIndex <> -1 Then
                index = cboIndexNum.SelectedIndex '0
                cannum = cboCANNum.SelectedIndex '0
                filtertype = cboFilterMode.SelectedIndex '1
                Mode = cboMode.SelectedIndex '0
                code = Val("&H" + txtCheckCode.Text) '0
                mask = Val("&H" + txtScreenCode.Text) 'fffffffffffffff
                Timing0 = Val("&H" + txtTimer0.Text) '0
                Timing1 = Val("&H" + txtTimer1.Text) '28
                InitConfig.AccCode = code
                InitConfig.AccMask = mask
                InitConfig.Filter_Renamed = filtertype
                InitConfig.Mode = Mode
                InitConfig.Timing0 = Timing0
                InitConfig.Timing1 = Timing1
                cando = 1
            End If

            If cando = 1 Then
                If VCI_OpenDevice(index) <> 1 Then        '见定义
                    If inp = 1 Then
                        MsgBox("打开设备错误")
                    End If
                    ret = 12
                Else
                    If VCI_InitCan(index, cannum, InitConfig) = 1 Then

                        tmrRead.Enabled = True

                        m_connect = 1
                        m_devind = index
                        m_cannum = cannum
                        If inp = 1 Then
                            butConnect.Text = "断开设备"
                        End If
                        ret = 0
                    Else
                        If inp = 1 Then
                            MsgBox("初始化CAN错误")
                        End If
                        ret = 13
                    End If
                End If
            End If
        End If

        Return ret

    End Function

    Private Sub Form1_Closed(ByVal sender As Object, ByVal e As System.EventArgs) Handles MyBase.Closed
        Disc_CAN()
    End Sub

    Sub Disc_CAN()
        m_connect = 0 '退出时，中断CAN
        VCI_CloseDevice(m_devind)
    End Sub

    Private Sub Form1_LostFocus(ByVal sender As Object, ByVal e As System.EventArgs) Handles MyBase.LostFocus
        Me.Close()
    End Sub

    Private Sub cboFrameType_SelectedIndexChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles cboFrameType.SelectedIndexChanged

    End Sub
End Class
