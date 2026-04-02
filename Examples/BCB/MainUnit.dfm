object MainForm: TMainForm
  Left = 212
  Top = 93
  BorderIcons = [biSystemMenu, biMinimize]
  BorderStyle = bsSingle
  Caption = 'CANUSB-I/II Tester  www.embedded-soc.com  '
  ClientHeight = 581
  ClientWidth = 565
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'MS Sans Serif'
  Font.Style = []
  OldCreateOrder = False
  OnClose = FormClose
  OnCreate = FormCreate
  PixelsPerInch = 96
  TextHeight = 13
  object Label11: TLabel
    Left = 168
    Top = 120
    Width = 63
    Height = 13
    Caption = #23450#26102#22120'0  '#65306' '
  end
  object GroupBox2: TGroupBox
    Left = 8
    Top = 8
    Width = 449
    Height = 153
    Caption = #35774#22791#21442#25968
    TabOrder = 3
    object Label9: TLabel
      Left = 168
      Top = 24
      Width = 67
      Height = 13
      Caption = #31532#20960#36335'CAN:  '
    end
    object Label8: TLabel
      Left = 8
      Top = 24
      Width = 72
      Height = 13
      Caption = #35774#22791#32034#24341#21495#65306
    end
    object GroupBox3: TGroupBox
      Left = 8
      Top = 48
      Width = 433
      Height = 97
      Caption = #21021#22987#21270'CAN'#21442#25968
      TabOrder = 0
      object Label1: TLabel
        Left = 8
        Top = 24
        Width = 68
        Height = 13
        Caption = #39564#25910#30721': 0x     '
      end
      object Label2: TLabel
        Left = 152
        Top = 24
        Width = 68
        Height = 13
        Caption = #23631#34109#30721': 0x     '
      end
      object Label10: TLabel
        Left = 8
        Top = 64
        Width = 74
        Height = 13
        Caption = #23450#26102#22120'0: 0x     '
      end
      object Label12: TLabel
        Left = 296
        Top = 24
        Width = 57
        Height = 13
        Caption = #28388#27874#26041#24335':  '
      end
      object Label13: TLabel
        Left = 312
        Top = 64
        Width = 36
        Height = 13
        Caption = #27169#24335':   '
      end
      object Label14: TLabel
        Left = 152
        Top = 64
        Width = 68
        Height = 13
        Caption = #23450#26102#22120'1: 0x   '
      end
      object EditAccCode: TEdit
        Left = 80
        Top = 20
        Width = 65
        Height = 21
        ImeName = #32043#20809#21326#23431#25340#38899'V5'
        TabOrder = 0
        Text = '00000000'
      end
      object EditAccMask: TEdit
        Left = 224
        Top = 20
        Width = 65
        Height = 21
        ImeName = #32043#20809#21326#23431#25340#38899'V5'
        TabOrder = 1
        Text = 'FFFFFFFF'
      end
      object ComboBoxFilter: TComboBox
        Left = 352
        Top = 20
        Width = 73
        Height = 21
        Style = csDropDownList
        ImeName = #32043#20809#21326#23431#25340#38899'V5'
        ItemHeight = 13
        ItemIndex = 0
        TabOrder = 2
        Text = #21333#28388#27874
        Items.Strings = (
          #21333#28388#27874
          #21452#28388#27874)
      end
      object ComboBoxMode: TComboBox
        Left = 352
        Top = 60
        Width = 73
        Height = 21
        Style = csDropDownList
        ImeName = #32043#20809#21326#23431#25340#38899'V5'
        ItemHeight = 13
        ItemIndex = 0
        TabOrder = 3
        Text = #27491#24120#27169#24335
        Items.Strings = (
          #27491#24120#27169#24335
          #21482#21548#27169#24335)
      end
      object EditTimer0: TEdit
        Left = 80
        Top = 64
        Width = 65
        Height = 21
        ImeName = #32043#20809#21326#23431#25340#38899'V5'
        TabOrder = 4
        Text = '00'
      end
    end
    object CheckBoxAllCAN: TCheckBox
      Left = 328
      Top = 24
      Width = 113
      Height = 17
      Caption = #36873#25321#25152#26377#30340'CAN'
      TabOrder = 1
    end
  end
  object ComboBoxCanChannel: TComboBox
    Left = 250
    Top = 27
    Width = 73
    Height = 21
    Style = csDropDownList
    ImeName = #32043#20809#21326#23431#25340#38899'V5'
    ItemHeight = 13
    ItemIndex = 0
    TabOrder = 0
    Text = '0'
    Items.Strings = (
      '0'
      '1')
  end
  object ButtonConnect: TButton
    Left = 480
    Top = 24
    Width = 75
    Height = 25
    Caption = #25171#24320#35774#22791
    TabOrder = 1
    OnClick = ButtonConnectClick
  end
  object ButtonReset: TButton
    Left = 480
    Top = 64
    Width = 75
    Height = 25
    Caption = #22797#20301'CAN'
    TabOrder = 2
    OnClick = ButtonResetClick
  end
  object GroupBox1: TGroupBox
    Left = 8
    Top = 170
    Width = 545
    Height = 89
    Caption = ' '#21457#36865#25968#25454#24103' '
    TabOrder = 4
    object Label4: TLabel
      Left = 152
      Top = 24
      Width = 48
      Height = 13
      Caption = #24103#31867#22411#65306
    end
    object Label5: TLabel
      Left = 280
      Top = 24
      Width = 48
      Height = 13
      Caption = #24103#26684#24335#65306
    end
    object Label6: TLabel
      Left = 408
      Top = 24
      Width = 58
      Height = 13
      Caption = #24103'ID'#65306'0x    '
    end
    object Label7: TLabel
      Left = 16
      Top = 56
      Width = 36
      Height = 13
      Caption = #25968#25454#65306
    end
    object Label3: TLabel
      Left = 8
      Top = 24
      Width = 60
      Height = 13
      Caption = #21457#36865#26684#24335#65306
    end
    object ComboBoxFrameType: TComboBox
      Left = 200
      Top = 20
      Width = 73
      Height = 21
      Style = csDropDownList
      ImeName = #32043#20809#21326#23431#25340#38899'V5'
      ItemHeight = 13
      ItemIndex = 0
      TabOrder = 0
      Text = #26631#20934#24103
      Items.Strings = (
        #26631#20934#24103
        #25193#23637#24103)
    end
    object ComboBoxFrameFormat: TComboBox
      Left = 328
      Top = 20
      Width = 73
      Height = 21
      Style = csDropDownList
      ImeName = #32043#20809#21326#23431#25340#38899'V5'
      ItemHeight = 13
      ItemIndex = 0
      TabOrder = 1
      Text = #25968#25454#24103
      Items.Strings = (
        #25968#25454#24103
        #36828#31243#24103)
    end
    object EditFrameID: TEdit
      Left = 464
      Top = 20
      Width = 73
      Height = 21
      ImeName = #32043#20809#21326#23431#25340#38899'V5'
      TabOrder = 2
      Text = 'FFFFFFFF'
    end
    object EditData: TEdit
      Left = 56
      Top = 53
      Width = 193
      Height = 21
      ImeName = #32043#20809#21326#23431#25340#38899'V5'
      TabOrder = 3
      Text = '01 02 03 04 05 06 07 08 '
    end
    object ButtonSend: TButton
      Left = 304
      Top = 51
      Width = 75
      Height = 25
      Caption = #21457#36865
      TabOrder = 4
      OnClick = ButtonSendClick
    end
    object ButtonClear: TButton
      Left = 440
      Top = 48
      Width = 75
      Height = 25
      Caption = #28165#38500#26174#31034
      TabOrder = 5
      OnClick = ButtonClearClick
    end
    object ComboBoxSendType: TComboBox
      Left = 72
      Top = 20
      Width = 73
      Height = 21
      ImeName = #32043#20809#21326#23431#25340#38899'V5'
      ItemHeight = 13
      ItemIndex = 1
      TabOrder = 6
      Text = #33258#21457#33258#25910
      Items.Strings = (
        #27491#24120#21457#36865
        #33258#21457#33258#25910)
    end
  end
  object GroupBox6: TGroupBox
    Left = 8
    Top = 264
    Width = 545
    Height = 161
    Caption = 'CAN0'#36890#36947#20449#24687
    TabOrder = 5
    object ListBoxReceiveCan0: TListBox
      Left = 8
      Top = 16
      Width = 529
      Height = 113
      ImeName = #32043#20809#21326#23431#25340#38899'V5'
      ItemHeight = 13
      TabOrder = 0
    end
    object CheckBoxCan0DataDisplay: TCheckBox
      Left = 400
      Top = 136
      Width = 129
      Height = 17
      Caption = #26174#31034'CAN0'#36890#36947#25968#25454
      Checked = True
      State = cbChecked
      TabOrder = 1
    end
  end
  object ComboBoxDevIndex: TComboBox
    Left = 98
    Top = 27
    Width = 73
    Height = 21
    Style = csDropDownList
    ImeName = #32043#20809#21326#23431#25340#38899'V5'
    ItemHeight = 13
    ItemIndex = 0
    TabOrder = 6
    Text = '0'
    Items.Strings = (
      '0'
      '1'
      '2'
      '3'
      '4'
      '5'
      '6'
      '7')
  end
  object EditTimer1: TEdit
    Left = 240
    Top = 120
    Width = 65
    Height = 21
    ImeName = #32043#20809#21326#23431#25340#38899'V5'
    TabOrder = 7
    Text = '14'
  end
  object GroupBox4: TGroupBox
    Left = 8
    Top = 424
    Width = 545
    Height = 153
    Caption = 'CAN1'#36890#36947#20449#24687
    TabOrder = 8
    object ListBoxReceiveCan1: TListBox
      Left = 8
      Top = 16
      Width = 529
      Height = 105
      ItemHeight = 13
      TabOrder = 0
    end
    object CheckBoxCan1DataDisplay: TCheckBox
      Left = 400
      Top = 128
      Width = 137
      Height = 17
      Caption = #26174#31034'CAN1'#36890#36947#25968#25454
      Checked = True
      State = cbChecked
      TabOrder = 1
    end
  end
end
