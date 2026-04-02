; CLW file contains information for the MFC ClassWizard

[General Info]
Version=1
LastClass=CTestDlg
LastTemplate=CDialog
NewFileInclude1=#include "stdafx.h"
NewFileInclude2=#include "test.h"

ClassCount=3
Class1=CTestApp
Class2=CTestDlg
Class3=CAboutDlg

ResourceCount=4
Resource1=IDD_ABOUTBOX
Resource2=IDR_MAINFRAME
Resource3=IDD_TEST_DIALOG
Resource4=IDR_MENU1

[CLS:CTestApp]
Type=0
HeaderFile=test.h
ImplementationFile=test.cpp
Filter=N

[CLS:CTestDlg]
Type=0
HeaderFile=testDlg.h
ImplementationFile=testDlg.cpp
Filter=D
BaseClass=CDialog
VirtualFilter=dWC
LastObject=IDC_COMBO_SENDTYPE

[CLS:CAboutDlg]
Type=0
HeaderFile=testDlg.h
ImplementationFile=testDlg.cpp
Filter=D

[DLG:IDD_ABOUTBOX]
Type=1
Class=CAboutDlg
ControlCount=4
Control1=IDC_STATIC,static,1342177283
Control2=IDC_STATIC,static,1342308480
Control3=IDC_STATIC,static,1342308352
Control4=IDOK,button,1342373889

[DLG:IDD_TEST_DIALOG]
Type=1
Class=CTestDlg
ControlCount=34
Control1=IDC_STATIC,button,1342177287
Control2=IDC_BUTTON_CONNECT,button,1342242817
Control3=IDC_BUTTON_RESETCAN,button,1342242816
Control4=IDC_STATIC,static,1342308352
Control5=IDC_COMBO_SENDTYPE,combobox,1344339971
Control6=IDC_STATIC,static,1342308352
Control7=IDC_COMBO_SENDFRAMETYPE,combobox,1344339971
Control8=IDC_STATIC,static,1342308352
Control9=IDC_COMBO_SENDFRAMEFORMAT,combobox,1344339971
Control10=IDC_STATIC,static,1342308352
Control11=IDC_EDIT_SENDFRAMEID,edit,1350631552
Control12=IDC_STATIC,static,1342308352
Control13=IDC_EDIT_SENDDATA,edit,1350631552
Control14=IDC_BUTTON_SEND,button,1342242816
Control15=IDC_STATIC,button,1342177287
Control16=IDC_LIST_INFO,listbox,1352728835
Control17=IDC_STATIC,button,1342177287
Control18=IDC_STATIC,static,1342308352
Control19=IDC_COMBO_CANIND,combobox,1344339971
Control20=IDC_STATIC,button,1342177287
Control21=IDC_STATIC,static,1342308352
Control22=IDC_EDIT_CODE,edit,1350631552
Control23=IDC_STATIC,static,1342308352
Control24=IDC_EDIT_MASK,edit,1350631552
Control25=IDC_STATIC,static,1342308352
Control26=IDC_COMBO_FILTERTYPE,combobox,1344339971
Control27=IDC_STATIC,static,1342308352
Control28=IDC_COMBO_MODE,combobox,1344339971
Control29=IDC_COMBO_DEVINDEX,combobox,1344339971
Control30=IDC_STATIC,static,1342308352
Control31=IDC_EDIT_TIME0,edit,1350631552
Control32=IDC_EDIT_TIME1,edit,1350631552
Control33=IDC_STATIC,static,1342308352
Control34=IDC_STATIC,static,1342308352

[MNU:IDR_MENU1]
Type=1
Class=?
Command1=ID_MENU_REFRESH
CommandCount=1

