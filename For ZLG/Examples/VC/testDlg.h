// testDlg.h : header file
//

#if !defined(AFX_TESTDLG_H__0B453A60_AE2F_4119_AF51_CC52D47F30DF__INCLUDED_)
#define AFX_TESTDLG_H__0B453A60_AE2F_4119_AF51_CC52D47F30DF__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

/////////////////////////////////////////////////////////////////////////////
// CTestDlg dialog
#include "TestListBox.h"

class CTestDlg : public CDialog
{
	// Construction
public:
	int m_cannum;
	int m_devtype;
	DWORD m_devind;
	static UINT ReceiveThread(void *param);
	void ShowInfo(CString str,int code);
	int m_connect;
	CTestDlg(CWnd* pParent = NULL);	// standard constructor
	int strtodata(unsigned char *str, unsigned char *data,int len,int flag);
	int chartoint(unsigned char chr, unsigned char *cint);
	// Dialog Data
	//{{AFX_DATA(CTestDlg)
	enum { IDD = IDD_TEST_DIALOG };
	CComboBox	m_ComboMode;
	CComboBox	m_ComboFilterType;
	CComboBox	m_ComboCANInd;
	CComboBox	m_ComboIndex;
	CTestListBox	m_ListInfo;
	CComboBox	m_ComboSendType;
	CComboBox	m_ComboSendFrmType;
	CComboBox	m_ComboSendFrmFmt;
	CString	m_EditSendData;
	CString	m_EditSendFrmID;
	CString	m_EditCode;
	CString	m_EditMask;
	CString	m_EditTiming0;
	CString	m_EditTiming1;
	//}}AFX_DATA
	
	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CTestDlg)
protected:
	virtual void DoDataExchange(CDataExchange* pDX);	// DDX/DDV support
	//}}AFX_VIRTUAL
	
	// Implementation
protected:
	HICON m_hIcon;
	CRITICAL_SECTION m_Section;
	// Generated message map functions
	//{{AFX_MSG(CTestDlg)
	virtual BOOL OnInitDialog();
	afx_msg void OnSysCommand(UINT nID, LPARAM lParam);
	afx_msg void OnPaint();
	afx_msg HCURSOR OnQueryDragIcon();
	virtual void OnCancel();
	virtual void OnOK();
	afx_msg void OnButtonConnect();
	afx_msg void OnButtonStartcan();
	afx_msg void OnButtonResetcan();
	afx_msg void OnButtonSend();
	afx_msg void OnMenuRefresh();
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_TESTDLG_H__0B453A60_AE2F_4119_AF51_CC52D47F30DF__INCLUDED_)
