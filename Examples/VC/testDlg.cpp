// testDlg.cpp : implementation file
//

#include "stdafx.h"
#include "test.h"
#include "testDlg.h"

#include "CAN_TO_USB.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif

/////////////////////////////////////////////////////////////////////////////
// CAboutDlg dialog used for App About

class CAboutDlg : public CDialog
{
public:
	CAboutDlg();

// Dialog Data
	//{{AFX_DATA(CAboutDlg)
	enum { IDD = IDD_ABOUTBOX };
	//}}AFX_DATA

	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CAboutDlg)
	protected:
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV support
	//}}AFX_VIRTUAL

// Implementation
protected:
	//{{AFX_MSG(CAboutDlg)
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};

CAboutDlg::CAboutDlg() : CDialog(CAboutDlg::IDD)
{
	//{{AFX_DATA_INIT(CAboutDlg)
	//}}AFX_DATA_INIT
}

void CAboutDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
	//{{AFX_DATA_MAP(CAboutDlg)
	//}}AFX_DATA_MAP
}

BEGIN_MESSAGE_MAP(CAboutDlg, CDialog)
	//{{AFX_MSG_MAP(CAboutDlg)
		// No message handlers
	//}}AFX_MSG_MAP
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CTestDlg dialog

CTestDlg::CTestDlg(CWnd* pParent /*=NULL*/)
	: CDialog(CTestDlg::IDD, pParent)
{
	//{{AFX_DATA_INIT(CTestDlg)
	m_EditSendData = _T("");
	m_EditSendFrmID = _T("");
	m_EditCode = _T("");
	m_EditMask = _T("");
	m_EditTime0 = _T("");
	m_EditTime1 = _T("");
	//}}AFX_DATA_INIT
	// Note that LoadIcon does not require a subsequent DestroyIcon in Win32
	m_hIcon = AfxGetApp()->LoadIcon(IDR_MAINFRAME);
	m_connect=0;
	m_cannum=0;
	m_devtype=0;
}

void CTestDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
	//{{AFX_DATA_MAP(CTestDlg)
	DDX_Control(pDX, IDC_COMBO_DEVINDEX, m_ComboDevindex);
	DDX_Control(pDX, IDC_COMBO_MODE, m_ComboMode);
	DDX_Control(pDX, IDC_COMBO_FILTERTYPE, m_ComboFilterType);
	DDX_Control(pDX, IDC_COMBO_CANIND, m_ComboCANInd);
	DDX_Control(pDX, IDC_LIST_INFO, m_ListInfo);
	DDX_Control(pDX, IDC_COMBO_SENDTYPE, m_ComboSendType);
	DDX_Control(pDX, IDC_COMBO_SENDFRAMETYPE, m_ComboSendFrmType);
	DDX_Control(pDX, IDC_COMBO_SENDFRAMEFORMAT, m_ComboSendFrmFmt);
	DDX_Text(pDX, IDC_EDIT_SENDDATA, m_EditSendData);
	DDX_Text(pDX, IDC_EDIT_SENDFRAMEID, m_EditSendFrmID);
	DDX_Text(pDX, IDC_EDIT_CODE, m_EditCode);
	DDX_Text(pDX, IDC_EDIT_MASK, m_EditMask);
	DDX_Text(pDX, IDC_EDIT_TIME0, m_EditTime0);
	DDX_Text(pDX, IDC_EDIT_TIME1, m_EditTime1);
	//}}AFX_DATA_MAP
}

BEGIN_MESSAGE_MAP(CTestDlg, CDialog)
	//{{AFX_MSG_MAP(CTestDlg)
	ON_WM_SYSCOMMAND()
	ON_WM_PAINT()
	ON_WM_QUERYDRAGICON()
	ON_BN_CLICKED(IDC_BUTTON_CONNECT, OnButtonConnect)
	ON_BN_CLICKED(IDC_BUTTON_STARTCAN, OnButtonStartcan)
	ON_BN_CLICKED(IDC_BUTTON_RESETCAN, OnButtonResetcan)
	ON_BN_CLICKED(IDC_BUTTON_SEND, OnButtonSend)
	ON_COMMAND(ID_MENU_REFRESH, OnMenuRefresh)
	ON_BN_CLICKED(IDC_BUTTONClear, OnBUTTONClear)
	//}}AFX_MSG_MAP
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CTestDlg message handlers

BOOL CTestDlg::OnInitDialog()
{
	CDialog::OnInitDialog();

	// Add "About..." menu item to system menu.

	// IDM_ABOUTBOX must be in the system command range.
	ASSERT((IDM_ABOUTBOX & 0xFFF0) == IDM_ABOUTBOX);
	ASSERT(IDM_ABOUTBOX < 0xF000);

	CMenu* pSysMenu = GetSystemMenu(FALSE);
	if (pSysMenu != NULL)
	{
		CString strAboutMenu;
		strAboutMenu.LoadString(IDS_ABOUTBOX);
		if (!strAboutMenu.IsEmpty())
		{
			pSysMenu->AppendMenu(MF_SEPARATOR);
			pSysMenu->AppendMenu(MF_STRING, IDM_ABOUTBOX, strAboutMenu);
		}
	}

	// Set the icon for this dialog.  The framework does this automatically
	//  when the application's main window is not a dialog
	SetIcon(m_hIcon, TRUE);			// Set big icon
	SetIcon(m_hIcon, FALSE);		// Set small icon

	// TODO: Add extra initialization here
	m_ComboSendType.SetCurSel(1);

	m_ComboSendFrmType.SetCurSel(0);
	m_ComboSendFrmFmt.SetCurSel(0);
	
	m_EditSendFrmID="00000080";
	m_EditSendData="01 02 03 04 05 06 07 08 ";
	
	CString str;
	
	for(int i=0;i<8;i++)
	{
		str.Format("%d",i);
		m_ComboDevindex.AddString(str);
	}

	for( i=0;i<2;i++)
	{
		str.Format("%d",i);
		m_ComboCANInd.AddString(str);
	}
	
	m_EditCode="00000000";
	m_EditMask="ffffffff";  
    m_EditTime0="00";
    m_EditTime1="14";

	m_ComboDevindex.SetCurSel(0);
	m_ComboCANInd.SetCurSel(0);  
	m_ComboFilterType.SetCurSel(0);
	m_ComboMode.SetCurSel(0);
	
	UpdateData(false);

	InitializeCriticalSection(&m_Section);
	
	return TRUE;  // return TRUE  unless you set the focus to a control
}

void CTestDlg::OnSysCommand(UINT nID, LPARAM lParam)
{
	if ((nID & 0xFFF0) == IDM_ABOUTBOX)
	{
		CAboutDlg dlgAbout;
		dlgAbout.DoModal();
	}
	else
	{
		CDialog::OnSysCommand(nID, lParam);
	}
}

// If you add a minimize button to your dialog, you will need the code below
//  to draw the icon.  For MFC applications using the document/view model,
//  this is automatically done for you by the framework.

void CTestDlg::OnPaint() 
{
	if (IsIconic())
	{
		CPaintDC dc(this); // device context for painting

		SendMessage(WM_ICONERASEBKGND, (WPARAM) dc.GetSafeHdc(), 0);

		// Center icon in client rectangle
		int cxIcon = GetSystemMetrics(SM_CXICON);
		int cyIcon = GetSystemMetrics(SM_CYICON);
		CRect rect;
		GetClientRect(&rect);
		int x = (rect.Width() - cxIcon + 1) / 2;
		int y = (rect.Height() - cyIcon + 1) / 2;

		// Draw the icon
		dc.DrawIcon(x, y, m_hIcon);
	}
	else
	{
		CDialog::OnPaint();
	}
}

// The system calls this to obtain the cursor to display while the user drags
//  the minimized window.
HCURSOR CTestDlg::OnQueryDragIcon()
{
	return (HCURSOR) m_hIcon;
}

void CTestDlg::OnCancel() 
{
	// TODO: Add extra cleanup here
	int connect=m_connect;
	m_connect=0;
	if(connect)
	{
		Sleep(500);		
		VCI_CloseDevice(m_devnum);
	}
	DeleteCriticalSection(&m_Section);
	CDialog::OnCancel();
}

void CTestDlg::OnOK() 
{
	// TODO: Add extra validation here
	int connect=m_connect;
	m_connect=0;
	Sleep(100);
	if(connect)
		VCI_CloseDevice(m_devnum);
	
	DeleteCriticalSection(&m_Section);
	CDialog::OnOK();
}

void CTestDlg::OnButtonConnect() 
{
	// TODO: Add your control notification handler code here
	if(m_connect==1)
	{
		m_connect=0;
		Sleep(500);
		GetDlgItem(IDC_BUTTON_CONNECT)->SetWindowText("连接");
		VCI_CloseDevice(m_devnum);
		return;
	}

	VCI_INIT_CONFIG init_config;

	int cannum,devnum,filtertype,mode;
	CString strcode,strmask,strtiming0,strtiming1,strtmp;
	char szcode[20],szmask[20],sztiming0[20],sztiming1[20];
	unsigned char sztmp[4];
	DWORD code,mask,timing0,timing1;
	
	UpdateData(true);

	devnum=m_ComboDevindex.GetCurSel();
    cannum=m_ComboCANInd.GetCurSel();
    strcode=m_EditCode;
	strmask=m_EditMask;
	filtertype=m_ComboFilterType.GetCurSel();
	mode=m_ComboMode.GetCurSel();	
   	strtiming0=m_EditTime0;
	strtiming1=m_EditTime1;
	UpdateData(false);
	
	strtmp=strcode;
	strcode.Format("%08s",strtmp);
	strtmp=strmask;
	strmask.Format("%08s",strtmp);
	strtmp=strtiming0;
	strtiming0.Format("%02s",strtmp);
	strtmp=strtiming1;
	strtiming1.Format("%02s",strtmp);
	
	strcpy(szcode,(LPCTSTR)strcode);
	strcpy(szmask,(LPCTSTR)strmask);
	strcpy(sztiming0,(LPCTSTR)strtiming0);
	strcpy(sztiming1,(LPCTSTR)strtiming1);

	
	if(strtodata((unsigned char*)szcode,sztmp,4,0)!=0)
	{
		MessageBox("验收码数据格式不对!","警告",MB_OK|MB_ICONQUESTION);
		return;
	}
	code=(((DWORD)sztmp[0])<<24)+(((DWORD)sztmp[1])<<16)+(((DWORD)sztmp[2])<<8)+
		((DWORD)sztmp[3]);
	
	if(strtodata((unsigned char*)szmask,sztmp,4,0)!=0)
	{
		MessageBox("屏蔽码数据格式不对!","警告",MB_OK|MB_ICONQUESTION);
		return;
	}
	mask=(((DWORD)sztmp[0])<<24)+(((DWORD)sztmp[1])<<16)+(((DWORD)sztmp[2])<<8)+
		((DWORD)sztmp[3]);

		if(strtodata((unsigned char*)sztiming0,sztmp,1,0)!=0)
	{
		MessageBox("定时器0数据格式不对!","警告",MB_OK|MB_ICONQUESTION);
		return;
	}
	timing0=((DWORD)sztmp[0]);
	
	if(strtodata((unsigned char*)sztiming1,sztmp,1,0)!=0)
	{
		MessageBox("定时器1数据格式不对!","警告",MB_OK|MB_ICONQUESTION);
		return;
	}
	timing1=((DWORD)sztmp[0]);
	

	init_config.AccCode=code;
	init_config.AccMask=mask;
	init_config.Filter=filtertype;
    init_config.Timing0=timing0;
	init_config.Timing1=timing1;
	init_config.Mode=mode;


    // TODO: Add your control notification handler code here
	if(m_connect==1)
	{
		m_connect=0;
		Sleep(500);
		GetDlgItem(IDC_BUTTON_CONNECT)->SetWindowText("连接");
		VCI_CloseDevice(m_devnum);
		return;
	}
   	
	if((VCI_OpenDevice(devnum))==0)                    //打开设备
	{
		MessageBox("打开设备失败!","警告",MB_OK|MB_ICONQUESTION);
		return;
	}
	if(VCI_InitCan(devnum,cannum,&init_config)!=true)//初始化对应的通道
	{
		MessageBox("初始化CAN失败!","警告",MB_OK|MB_ICONQUESTION);
		VCI_CloseDevice(devnum);
		return;

	}

	m_connect=1;
	m_cannum=cannum;
	m_devnum=devnum;
   
	AfxBeginThread(ReceiveThread,this);  //启动接受线程

	GetDlgItem(IDC_BUTTON_CONNECT)->SetWindowText("断开");
	
}

void CTestDlg::OnButtonStartcan() 
{

}

void CTestDlg::OnButtonResetcan() 
{
	// TODO: Add your control notification handler code here
	if(m_connect==0)
		return;
	if(VCI_ResetCan(m_devnum,m_cannum)==1)   //复位对应的CAN通道
	{
		//GetDlgItem(IDC_BUTTON_STARTCAN)->EnableWindow(true);
		ShowInfo("复位成功",0);		
	}
	else
	{
		CString str;
		str="复位失败";
		ShowInfo(str,2);
	}
	
}

void CTestDlg::OnButtonSend() 
{
	// TODO: Add your control notification handler code here
	if(m_connect==0)
		return;

	VCI_CAN_OBJ frameinfo;
	char szFrameID[9];
	unsigned char FrameID[4]={0,0,0,0};
	memset(szFrameID,'0',9);
	unsigned char Data[8];
	char szData[25];
	BYTE datalen=0;
	
	UpdateData(true);
	if(m_EditSendFrmID.GetLength()==0||
		(m_EditSendData.GetLength()==0&&m_ComboSendFrmType.GetCurSel()==0))
	{
		ShowInfo("请输入数据",1);
		return;
	}
	
	if(m_EditSendFrmID.GetLength()>8)
	{
		ShowInfo("ID值超过范围",1);
		return;
	}
	if(m_EditSendData.GetLength()>24)
	{
		ShowInfo("数据长度超过范围,最大为8个字节",1);
		return;
	}
	if(m_ComboSendFrmType.GetCurSel()==0)
	{
		if(m_EditSendData.GetLength()%3==1)
		{
			ShowInfo("数据格式不对,请重新输入",1);
			return;		
		}		
	}
	memcpy(&szFrameID[8-m_EditSendFrmID.GetLength()],(LPCTSTR)m_EditSendFrmID,m_EditSendFrmID.GetLength());
	strtodata((unsigned char*)szFrameID,FrameID,4,0);

	datalen=(m_EditSendData.GetLength()+1)/3;
	strcpy(szData,(LPCTSTR)m_EditSendData);
	strtodata((unsigned char*)szData,Data,datalen,1);

	UpdateData(false);
	
	frameinfo.SendType=m_ComboSendType.GetCurSel();     //发送类型 
	frameinfo.ExternFlag=m_ComboSendFrmType.GetCurSel();//是否是扩展帧
    frameinfo.RemoteFlag=m_ComboSendFrmFmt.GetCurSel(); //是否是远程帧
	frameinfo.DataLen=datalen;                          //数据长度
	memcpy(&frameinfo.Data,Data,datalen);               //数据

	

	if(frameinfo.ExternFlag==1)
	{
		frameinfo.ID=((DWORD)FrameID[0]<<24)+((DWORD)FrameID[1]<<16)+((DWORD)FrameID[2]<<8)+
			((DWORD)FrameID[3]);
	}
	else
	{
		frameinfo.ID=((DWORD)FrameID[2]<<8)+((DWORD)FrameID[3]);		
	}

	if(VCI_Transmit(m_devnum,m_cannum,&frameinfo)==true)
	{
		ShowInfo("写入成功",0);		
	}
	else
	{
		ShowInfo("写入失败",2);		
	}
	
}

void CTestDlg::ShowInfo(CString str, int code)
{
	m_ListInfo.InsertString(m_ListInfo.GetCount(),str);
	m_ListInfo.SetCurSel(m_ListInfo.GetCount()-1);
}

//-----------------------------------------------------
//参数：
//str：要转换的字符串
//data：储存转换过来的数据串
//len:数据长度
//函数功能：字符串转换为数据串
//-----------------------------------------------------
int CTestDlg::strtodata(unsigned char *str, unsigned char *data,int len,int flag)
{
	unsigned char cTmp=0;
	int i=0;
	for(int j=0;j<len;j++)
	{
		if(chartoint(str[i++],&cTmp))
			return 1;
		data[j]=cTmp;
		if(chartoint(str[i++],&cTmp))
			return 1;
		data[j]=(data[j]<<4)+cTmp;
		if(flag==1)
			i++;
	}
	return 0;
}

//-----------------------------------------------------
//参数：
//chr：要转换的字符
//cint：储存转换过来的数据
//函数功能：字符转换为数据
//-----------------------------------------------------
int CTestDlg::chartoint(unsigned char chr, unsigned char *cint)
{
	unsigned char cTmp;
	cTmp=chr-48;
	if(cTmp>=0&&cTmp<=9)
	{
		*cint=cTmp;
		return 0;
	}
	cTmp=chr-65;
	if(cTmp>=0&&cTmp<=5)
	{
		*cint=(cTmp+10);
		return 0;
	}
	cTmp=chr-97;
	if(cTmp>=0&&cTmp<=5)
	{
		*cint=(cTmp+10);
		return 0;
	}
	return 1;
}

UINT CTestDlg::ReceiveThread(void *param)
{
	CTestDlg *dlg=(CTestDlg*)param;
	CListBox *box=(CListBox *)dlg->GetDlgItem(IDC_LIST_INFO);
	VCI_CAN_OBJ frameinfo[50];

  
	int Len=0;
	int i=0;
	CString str,tmpstr;   

	while(1)
	{
		Sleep(1);
		if(dlg->m_connect==0)
			break;

		Len=VCI_Receive(dlg->m_devnum,dlg->m_cannum ,frameinfo,50,200);
		if(Len<=0)
		{
		   //没有读到数据 
		   continue;	
		}
		else
		{
			for(i=0;i<Len;i++)
			{
				tmpstr.Format("设备%d 通道CAN%d 接收到数据帧: ",dlg->m_devnum,dlg->m_cannum) ;
				str=tmpstr;


			    //帧ID
				tmpstr.Format("帧ID:%08x ",frameinfo[i].ID);
				str+=tmpstr;

                //帧类型
	            str+="帧类型:";
				if(frameinfo[i].ExternFlag==0)
					tmpstr="标准帧 ";
				else
					tmpstr="扩展帧 ";
				str+=tmpstr;
				
				//帧格式
				str+="帧格式:";
				if(frameinfo[i].RemoteFlag==0)
					tmpstr="数据帧 ";
				else
					tmpstr="远程帧 ";
				str+=tmpstr;

				box->InsertString(box->GetCount(),str);

				//数据
				if(frameinfo[i].RemoteFlag==0)
				{
					str="数据:";
					if(frameinfo[i].DataLen>8)
						frameinfo[i].DataLen=8;
					for(int j=0;j<frameinfo[i].DataLen;j++)
					{
						tmpstr.Format("%02x ",frameinfo[i].Data[j]);
						str+=tmpstr;
					}
					//EnterCriticalSection(&(dlg->m_Section));
					//LeaveCriticalSection(&(dlg->m_Section));
					box->InsertString(box->GetCount(),str);
				}				
			}
			box->SetCurSel(box->GetCount()-1);
		}
	}
	return 0;
}

void CTestDlg::OnMenuRefresh() 
{
	// TODO: Add your command handler code here
}



void CTestDlg::OnBUTTONClear() 
{
	// TODO: Add your control notification handler code here
  
}
