VERSION 5.00
Begin VB.Form Form1 
   Caption         =   "CANUSB-I/II Tester"
   ClientHeight    =   6570
   ClientLeft      =   1950
   ClientTop       =   2550
   ClientWidth     =   8910
   LinkTopic       =   "Form1"
   ScaleHeight     =   6570
   ScaleWidth      =   8910
   Begin VB.ComboBox Combo2 
      Height          =   315
      ItemData        =   "Form1.frx":0000
      Left            =   4920
      List            =   "Form1.frx":000A
      Style           =   2  'Dropdown List
      TabIndex        =   18
      Top             =   480
      Width           =   1185
   End
   Begin VB.TextBox Text1 
      Height          =   285
      Left            =   6975
      TabIndex        =   17
      Text            =   "FFFFFFFF"
      Top             =   2820
      Width           =   1215
   End
   Begin VB.Timer Timer1 
      Enabled         =   0   'False
      Interval        =   1
      Left            =   7920
      Top             =   1920
   End
   Begin VB.TextBox Text4 
      Height          =   285
      Left            =   930
      TabIndex        =   14
      Text            =   "01 02 03 04 05 06 07 08 "
      Top             =   3315
      Width           =   3855
   End
   Begin VB.ComboBox Combo5 
      Height          =   315
      ItemData        =   "Form1.frx":0016
      Left            =   5130
      List            =   "Form1.frx":0020
      Style           =   2  'Dropdown List
      TabIndex        =   13
      Top             =   2805
      Width           =   1215
   End
   Begin VB.ComboBox Combo4 
      Height          =   315
      ItemData        =   "Form1.frx":0034
      Left            =   3120
      List            =   "Form1.frx":003E
      Style           =   2  'Dropdown List
      TabIndex        =   12
      Top             =   2820
      Width           =   1215
   End
   Begin VB.ComboBox Combo3 
      Height          =   315
      ItemData        =   "Form1.frx":0052
      Left            =   1080
      List            =   "Form1.frx":005C
      Style           =   2  'Dropdown List
      TabIndex        =   11
      Top             =   2820
      Width           =   1215
   End
   Begin VB.CommandButton Command3 
      Caption         =   "复位CAN"
      Height          =   330
      Left            =   7440
      TabIndex        =   10
      Top             =   1080
      Width           =   1005
   End
   Begin VB.CommandButton Connect 
      Caption         =   "连接"
      Height          =   330
      Left            =   7440
      TabIndex        =   1
      Top             =   480
      Width           =   1005
   End
   Begin VB.Frame Frame1 
      Caption         =   " 发送数据帧 "
      Height          =   1230
      Left            =   120
      TabIndex        =   0
      Top             =   2520
      Width           =   8595
      Begin VB.CommandButton Command4 
         Caption         =   "清除显示"
         Height          =   375
         Left            =   6840
         TabIndex        =   28
         Top             =   720
         Width           =   975
      End
      Begin VB.CommandButton Command1 
         Caption         =   "发送"
         Height          =   330
         Left            =   4920
         TabIndex        =   7
         Top             =   760
         Width           =   870
      End
      Begin VB.Label Label7 
         Caption         =   "数据："
         Height          =   240
         Left            =   240
         TabIndex        =   6
         Top             =   840
         Width           =   555
      End
      Begin VB.Label Label6 
         Caption         =   "帧ID："
         Height          =   195
         Left            =   6360
         TabIndex        =   5
         Top             =   360
         Width           =   585
      End
      Begin VB.Label Label5 
         Caption         =   "帧格式："
         Height          =   195
         Left            =   4320
         TabIndex        =   4
         Top             =   360
         Width           =   765
      End
      Begin VB.Label Label4 
         Caption         =   "帧类型："
         Height          =   195
         Left            =   2280
         TabIndex        =   3
         Top             =   360
         Width           =   810
      End
      Begin VB.Label Label3 
         Caption         =   "发送格式："
         Height          =   240
         Left            =   120
         TabIndex        =   2
         Top             =   360
         Width           =   960
      End
   End
   Begin VB.Frame Frame2 
      Caption         =   "设备参数"
      Height          =   2295
      Left            =   120
      TabIndex        =   8
      Top             =   120
      Width           =   6855
      Begin VB.ComboBox Combo8 
         Height          =   315
         ItemData        =   "Form1.frx":0074
         Left            =   1800
         List            =   "Form1.frx":0093
         Style           =   2  'Dropdown List
         TabIndex        =   29
         Top             =   360
         Width           =   1185
      End
      Begin VB.Frame Frame3 
         Caption         =   "初始化CAN参数"
         Height          =   1335
         Left            =   120
         TabIndex        =   19
         Top             =   840
         Width           =   6615
         Begin VB.TextBox Text6 
            Height          =   285
            Left            =   3600
            TabIndex        =   34
            Text            =   "14"
            Top             =   960
            Width           =   855
         End
         Begin VB.TextBox Text5 
            Height          =   285
            Left            =   1320
            TabIndex        =   32
            Text            =   "00"
            Top             =   960
            Width           =   855
         End
         Begin VB.ComboBox Combo7 
            Height          =   315
            ItemData        =   "Form1.frx":00B4
            Left            =   5280
            List            =   "Form1.frx":00BE
            Style           =   2  'Dropdown List
            TabIndex        =   27
            Top             =   840
            Width           =   1215
         End
         Begin VB.ComboBox Combo6 
            Height          =   315
            ItemData        =   "Form1.frx":00D6
            Left            =   5280
            List            =   "Form1.frx":00E0
            Style           =   2  'Dropdown List
            TabIndex        =   25
            Top             =   360
            Width           =   1215
         End
         Begin VB.TextBox Text3 
            Height          =   285
            Left            =   3360
            TabIndex        =   23
            Text            =   "FFFFFFFF"
            Top             =   360
            Width           =   855
         End
         Begin VB.TextBox Text2 
            Height          =   285
            Left            =   1200
            TabIndex        =   21
            Text            =   "00000000"
            Top             =   360
            Width           =   855
         End
         Begin VB.Label Label11 
            Caption         =   "定时器1：0x"
            Height          =   255
            Left            =   2400
            TabIndex        =   33
            Top             =   960
            Width           =   975
         End
         Begin VB.Label Label8 
            Caption         =   "定时器0：0x"
            Height          =   255
            Left            =   240
            TabIndex        =   31
            Top             =   960
            Width           =   975
         End
         Begin VB.Label Label13 
            Caption         =   "模式："
            Height          =   255
            Left            =   4680
            TabIndex        =   26
            Top             =   885
            Width           =   615
         End
         Begin VB.Label Label12 
            Caption         =   "滤波方式："
            Height          =   255
            Left            =   4320
            TabIndex        =   24
            Top             =   400
            Width           =   975
         End
         Begin VB.Label Label2 
            Caption         =   "屏蔽码：0x"
            Height          =   255
            Left            =   2400
            TabIndex        =   22
            Top             =   360
            Width           =   975
         End
         Begin VB.Label Label1 
            Caption         =   "验收码：0x"
            Height          =   255
            Left            =   240
            TabIndex        =   20
            Top             =   360
            Width           =   975
         End
      End
      Begin VB.Label Label9 
         Caption         =   "设备索引号："
         Height          =   255
         Left            =   240
         TabIndex        =   30
         Top             =   360
         Width           =   1455
      End
      Begin VB.Label Label10 
         Caption         =   "第几路CAN："
         Height          =   255
         Left            =   3480
         TabIndex        =   9
         Top             =   360
         Width           =   1095
      End
   End
   Begin VB.Frame Frame6 
      Caption         =   "信息"
      Height          =   2535
      Left            =   120
      TabIndex        =   15
      Top             =   3840
      Width           =   8655
      Begin VB.ListBox List1 
         Height          =   2205
         Left            =   120
         TabIndex        =   16
         Top             =   240
         Width           =   8415
      End
   End
End
Attribute VB_Name = "Form1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Dim m_devtype As Long
Dim m_connect As Byte
Dim m_devind As Long
Dim m_cannum As Long




Private Sub Command1_Click()
    If m_connect = 0 Then
        MsgBox ("请先打开端口")
        Exit Sub
    End If
    
    Dim SendType, frameformat, frametype As Byte
    Dim ID As Long
    Dim data(7) As Byte
    Dim frameinfo As VCI_CAN_OBJ
    Dim str As String
    
    SendType = Combo3.ListIndex
    
    frametype = Combo4.ListIndex
    
    frameformat = Combo5.ListIndex
    
    str = "&H"
    str = str + Text1.Text
    ID = Val(str)
    
    
    str = Text4.Text
    strdata = " "
    i = 0
    For i = 0 To 7
       strdata = Left(str, 2)
       If Len(strdata) = 0 Then
          Exit For
       End If
       str = Right(str, Len(str) - 3)
       data(i) = Val("&H" + strdata)
    Next
        
    
    frameinfo.SendType = SendType
    frameinfo.ExternFlag = frametype
    frameinfo.RemoteFlag = frameformat
    frameinfo.ID = ID
    frameinfo.DataLen = i
    
    For j = 0 To i - 1
        frameinfo.data(j) = data(j)
    Next
    If VCI_Transmit(m_devind, m_cannum, frameinfo) <> 1 Then
        MsgBox ("发送数据失败")
    Else
        List1.AddItem "发送数据成功", List1.ListCount
    End If

End Sub

Private Sub Command2_Click()

 
      
End Sub

Private Sub Command3_Click()
    If m_connect = 0 Then
        MsgBox ("请先打开端口")
        Exit Sub
    End If
    If VCI_ResetCan(m_devind, m_cannum) <> 1 Then
        MsgBox ("复位CAN错误")
   Else
        List1.AddItem "复位CAN成功", List1.ListCount
    End If

End Sub

Private Sub Command4_Click()
List1.Clear

End Sub

Private Sub Command5_Click(index As Integer)
 

End Sub

Private Sub Connect_Click()
    Dim index As Long
    Dim cannum, devind As Long
    Dim code, mask As Long
    
    Dim Timing0, Timing1, filtertype, Mode As Byte
    
    
    Dim InitConfig As VCI_INIT_CONFIG
    
    If m_connect = 1 Then
        m_connect = 0
        Connect.Caption = "连接"
        Timer1.Enabled = False
        VCI_CloseDevice (m_devind)
        Exit Sub
    End If
        
    If Combo2.ListIndex <> -1 Then
       

        cannum = Combo2.ListIndex
        devind = Combo8.ListIndex
        
        code = Val("&H" + Text2.Text)
        mask = Val("&H" + Text3.Text)
       
        filtertype = Combo6.ListIndex
        
        Mode = Combo7.ListIndex
      
        InitConfig.AccCode = code
        InitConfig.AccMask = mask
        InitConfig.Filter = filtertype
        InitConfig.BusTime0 = Val("&H" + Text5.Text)
        InitConfig.BusTime1 = Val("&H" + Text6.Text)
        
        InitConfig.Mode = Mode
      
        If VCI_OpenDevice(devind) <> 1 Then
            MsgBox ("打开设备错误")
        Else
            If VCI_InitCan(devind, cannum, InitConfig) <> 0 Then
                m_connect = 1
                m_cannum = cannum
                m_devind = devind
                Connect.Caption = "断开"
                Timer1.Enabled = True

            Else
                MsgBox ("初始化CAN错误")
            End If
        End If
    End If
    
End Sub

Private Sub Form_Load()
   
    m_connect = 0
    m_cannum = 0
    
    Combo2.ListIndex = 0
    Combo3.ListIndex = 1
    Combo4.ListIndex = 0
    Combo5.ListIndex = 0
    Combo6.ListIndex = 0
    Combo7.ListIndex = 0
    Combo8.ListIndex = 0
    
End Sub

Private Sub Form_Unload(Cancel As Integer)
    If m_connect = 1 Then
        m_connect = 0
        VCI_CloseDevice (m_devind)
    End If
End Sub





Private Sub Timer1_Timer()
  
    Dim Length As Long
    Dim frameinfo(49) As VCI_CAN_OBJ
    Dim str As String
    
    Timer1.Enabled = False
    
    If m_connect = 0 Then
        Timer1.Enabled = True
        Exit Sub
    End If
    
    Length = VCI_Receive(m_devind, m_cannum, frameinfo(0), 50, 200)
    If Length <= 0 Then
       '没有接受到数据
        Timer1.Enabled = True
        Exit Sub
    Else
        
    For i = 0 To Length - 1
        str = "接收到数据帧:  "
        
        '帧ID
        tmpstr = "  帧ID:0x" + Hex(frameinfo(i).ID)
        str = str + tmpstr
        
        '帧类型
        str = str + "  帧类型:"
        If frameinfo(i).ExternFlag = 0 Then
            tmpstr = "标准帧 "
        Else
            tmpstr = "扩展帧 "
        End If
        str = str + tmpstr
        
        
       '帧格式
        str = str + "  帧格式:"
        If frameinfo(i).RemoteFlag = 0 Then
            tmpstr = "数据帧 "
        Else
            tmpstr = "远程帧 "
        End If
        str = str + tmpstr
        
       
        '帧数据
        List1.AddItem str, List1.ListCount
        If frameinfo(i).RemoteFlag = 0 Then
            str = "  数据:"
            If frameinfo(i).DataLen > 8 Then
                frameinfo(i).DataLen = 8
            End If
            
            For j = 0 To frameinfo(i).DataLen - 1
                tmpstr = Hex(frameinfo(i).data(j)) + " "
                str = str + tmpstr
            Next
            List1.AddItem str, List1.ListCount
        End If
    Next
 Timer1.Enabled = True
 End If
   
End Sub
