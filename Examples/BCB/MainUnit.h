//---------------------------------------------------------------------------

#ifndef MainUnitH
#define MainUnitH
//---------------------------------------------------------------------------
#include <Classes.hpp>
#include <Controls.hpp>
#include <StdCtrls.hpp>
#include <Forms.hpp>
#include <process.h>
#include "SkinCaption.hpp"
#include "WinSkinData.hpp"

//---------------------------------------------------------------------------
class TMainForm : public TForm
{
__published:	// IDE-managed Components
        TComboBox *ComboBoxCanChannel;
        TButton *ButtonConnect;
        TButton *ButtonReset;
        TGroupBox *GroupBox1;
        TLabel *Label4;
        TLabel *Label5;
        TLabel *Label6;
        TLabel *Label7;
        TGroupBox *GroupBox2;
        TLabel *Label9;
        TComboBox *ComboBoxFrameType;
        TComboBox *ComboBoxFrameFormat;
        TEdit *EditFrameID;
        TEdit *EditData;
        TGroupBox *GroupBox6;
        TListBox *ListBoxReceiveCan0;
        TButton *ButtonSend;
        TGroupBox *GroupBox3;
        TLabel *Label1;
        TEdit *EditAccCode;
        TLabel *Label2;
        TEdit *EditAccMask;
        TLabel *Label10;
        TLabel *Label12;
        TLabel *Label13;
        TComboBox *ComboBoxFilter;
        TComboBox *ComboBoxMode;
        TCheckBox *CheckBoxAllCAN;
        TButton *ButtonClear;
        TLabel *Label8;
        TComboBox *ComboBoxDevIndex;
        TEdit *EditTimer0;
        TLabel *Label11;
        TEdit *EditTimer1;
        TLabel *Label14;
        TLabel *Label3;
        TComboBox *ComboBoxSendType;
        TGroupBox *GroupBox4;
        TListBox *ListBoxReceiveCan1;
        TCheckBox *CheckBoxCan0DataDisplay;
        TCheckBox *CheckBoxCan1DataDisplay;
        void __fastcall FormClose(TObject *Sender, TCloseAction &Action);
        void __fastcall ButtonConnectClick(TObject *Sender);
        void __fastcall ButtonResetClick(TObject *Sender);
        void __fastcall FormCreate(TObject *Sender);
        void __fastcall ButtonSendClick(TObject *Sender);
        void __fastcall ButtonClearClick(TObject *Sender);


private:	// User declarations

        void __fastcall Can0StatisticDisplay();
        void __fastcall Can1StatisticDisplay();

public:
        HANDLE m_readhandle;		// User declarations
        __fastcall TMainForm(TComponent* Owner);

};
//---------------------------------------------------------------------------
extern PACKAGE TMainForm *MainForm;
//---------------------------------------------------------------------------
#endif
