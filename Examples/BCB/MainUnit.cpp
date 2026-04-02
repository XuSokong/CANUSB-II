//---------------------------------------------------------------------------

#include <vcl.h>
#pragma hdrstop

#include "MainUnit.h"
#include "CAN_TO_USB.h"
#include "classes.hpp"


//---------------------------------------------------------------------------
#pragma package(smart_init)
#pragma link "SkinCaption"
#pragma link "WinSkinData"
#pragma resource "*.dfm"
TMainForm *MainForm;

BYTE   CANIndex=0;                                //选择CAN的通道  CAN1--1， CAN0--0
BYTE   DevIndex=0;                                //选择设备号

VCI_INIT_CONFIG InitConfig;                   //CAN初始化结构体
VCI_CAN_OBJ     SendData;                     //CAN发送数据的缓冲区
VCI_CAN_OBJ     ReceivedataCan1[1000];         //CAN接受数据的缓冲区
VCI_CAN_OBJ     ReceivedataCan0[1000];         //CAN接受数据的缓冲区

DWORD  FrameID;                                   //帧ID
BYTE   FrameType,                                 //帧类型
       FrameFormat,                               //帧格式
       FrameData[8];                              //帧数据
       
bool   Device_Connect=false;                      //设备已经连接并正确出始化的标志
bool   DeviceCan0Open=false;                      //CAN0通道成功打开的标志
bool   DeviceCan1Open=false;                      //CAN1通道成功打开的标志

DWORD Can0TotalReceiveCount=0;                    //CAN0总共接受到的帧数
DWORD Can1TotalReceiveCount=0;                    //CAN1总共接受到的帧数

DWORD Can0SingleReceiveCount=0;                   //CAN0本次接受到的帧数
DWORD Can1SingleReceiveCount=0;                   //CAN1本次接受到的帧数

//---------------------------------------------------------------------------
__fastcall TMainForm::TMainForm(TComponent* Owner)
        : TForm(Owner)
{
}

//---------------------------------------------------------------------------
void __fastcall TMainForm::Can0StatisticDisplay()
{

}

//---------------------------------------------------------------------------
void __fastcall TMainForm::Can1StatisticDisplay()
{

}

//---------------------------------------------------------------------------

void __fastcall TMainForm::FormClose(TObject *Sender, TCloseAction &Action)
{
         if(Device_Connect==true)
        { 
                Device_Connect=false;

                DeviceCan0Open=false;
                DeviceCan1Open=false;
                
                Sleep(200);
                VCI_CloseDevice(DevIndex);  //关闭设备
                return;
        }
}

//---------------------------------------------------------------------------
void ReceiveThreadCan1(void *param)
{
   TListBox *box=(TListBox*)param;
   DWORD Len,i;
   AnsiString str,tmpstr;
   DWORD ID,count;

while(1)
{
   if(Device_Connect==false)
       break;

   if(DeviceCan1Open==true)
   {
       //端口1
       Len=VCI_Receive(DevIndex,1,ReceivedataCan1,200,100);

       if(Len>0)
       {
                if(count++>=1000)     //当列表筐超过1000帧时自动删除
                {
                     count=0;
                     box->Items->Clear();
                }

                //显示统计信息
                Can1SingleReceiveCount=Len;
                Can1TotalReceiveCount+=Len;

                //控制是否显示数据(在数据量大的时候显示数据占用不少CPU时间)
                if(MainForm->CheckBoxCan1DataDisplay->Checked==false)
                {
                 box->Items->Clear();
                 str="CAN1接受到的总帧数:"+IntToStr(Can1TotalReceiveCount)+",  本次接受到的帧数:"+IntToStr(Can1SingleReceiveCount)+
                 +",  缓冲区中的帧数:"+ IntToStr(VCI_GetReceiveNum(DevIndex,1))+"      ";
                 box->Items->Add(str);
                  continue;
                }

                for(i=0;i<Len;i++)
		{
			str="设备"+IntToStr(DevIndex)+
                            ",通道CAN1"+
                            ",接收到的帧:  ";

                        //ID
		        tmpstr="帧ID:0x"+IntToHex((int)ReceivedataCan1[i].ID,8)+" ";
			str+=tmpstr;

                        //帧类型
			str+="帧类型:";
			if(ReceivedataCan1[i].ExternFlag==0)
				tmpstr="标准帧 ";
			else
				tmpstr="扩展帧 ";
			str+=tmpstr;


                         //帧格式
			str+="帧格式:";
			if(ReceivedataCan1[i].RemoteFlag==0)
				tmpstr="数据帧 ";
			else
				tmpstr="远程帧 ";
			str+=tmpstr;

                        box->Items->Add(str);

                        //数据
			if(ReceivedataCan1[i].RemoteFlag==0)
			{
				str="数据:";
                                if(ReceivedataCan1[i].DataLen>8)
                                        ReceivedataCan1[i].DataLen=8;
				for(int j=0;j<ReceivedataCan1[i].DataLen;j++)
				{
					tmpstr=IntToHex((int)ReceivedataCan1[i].Data[j],2)+" ";
					str+=tmpstr;
				}
				box->Items->Add(str);
			}
		}
		box->ItemIndex=box->Items->Count-1;
        }
   }//DeviceCan1Open==true


}
   _endthread();

}

//---------------------------------------------------------------------------
void ReceiveThreadCan0(void *param)
{
   TListBox *box=(TListBox*)param;
   DWORD Len,i;
   AnsiString str,tmpstr;
   DWORD ID,count;

while(1)
{
   if(Device_Connect==false)
       break; 
   if(DeviceCan0Open==true)
   {
       //端口0  
       Len=VCI_Receive(DevIndex,0,ReceivedataCan0,200,100);

       if(Len>0)
       {
                 if(count++>=1000)     //当列表筐超过1000帧时自动删除
                 {
                     count=0;
                     box->Items->Clear();
                 }

                  //显示统计信息
                Can0SingleReceiveCount=Len;
                Can0TotalReceiveCount+=Len;

                //控制是否显示数据(在数据量大的时候显示数据占用不少CPU时间)
                if(MainForm->CheckBoxCan0DataDisplay->Checked==false)
                {
                   box->Items->Clear();
                   str="CAN0接受到的总帧数:"+IntToStr(Can0TotalReceiveCount)+",  本次接受到的帧数:"+IntToStr(Can0SingleReceiveCount)+
                   +",  缓冲区中的帧数:"+ IntToStr(VCI_GetReceiveNum(DevIndex,0))+"      ";
                   box->Items->Add(str);
                  continue;
                 }
                 
                for(i=0;i<Len;i++)
		{
			str="设备"+IntToStr(DevIndex)+
                            ",通道CAN0"+
                            ",接收到的帧:  ";

                        //ID
		        tmpstr="帧ID:0x"+IntToHex((int)ReceivedataCan0[i].ID,8)+" ";
			str+=tmpstr;

                        //帧类型
			str+="帧类型:";
			if(ReceivedataCan0[i].ExternFlag==0)
				tmpstr="标准帧 ";
			else
				tmpstr="扩展帧 ";
			str+=tmpstr;


                         //帧格式
			str+="帧格式:";
			if(ReceivedataCan0[i].RemoteFlag==0)
				tmpstr="数据帧 ";
			else
				tmpstr="远程帧 ";
			str+=tmpstr;

                        box->Items->Add(str);

                        //数据
			if(ReceivedataCan0[i].RemoteFlag==0)
			{
				str="数据:";
                                if(ReceivedataCan0[i].DataLen>8)
                                        ReceivedataCan0[i].DataLen=8;
				for(int j=0;j<ReceivedataCan0[i].DataLen;j++)
				{
					tmpstr=IntToHex((int)ReceivedataCan0[i].Data[j],2)+" ";
					str+=tmpstr;
				}
				box->Items->Add(str);
			}
		}
		box->ItemIndex=box->Items->Count-1;
        }

   }// DeviceCan0Open==true
}
   _endthread();

}


//---------------------------------------------------------------------------


void __fastcall TMainForm::ButtonConnectClick(TObject *Sender)
{
    DWORD   TempAccCode;
    DWORD   TempAccMask;

    HANDLE   ReceiveThreadHanle;

        if(Device_Connect==true)
        {
                ButtonConnect->Caption ="连接";
                Device_Connect=false;

                DeviceCan0Open=false;
                DeviceCan1Open=false;
                
                Sleep(400);
                VCI_CloseDevice(DevIndex); //关闭设备
                return;
        }
        
        CANIndex = ComboBoxCanChannel->ItemIndex;            //选择CAN的通道
                                                             // CAN1--1
                                                             // CAN0--0

        DevIndex=ComboBoxDevIndex->ItemIndex ;               //设备号
        InitConfig.AccCode=StrToInt("0x"+EditAccCode->Text); //验证码
        InitConfig.AccMask=StrToInt("0x"+EditAccMask->Text); //屏蔽码

        InitConfig.Filter=ComboBoxFilter->ItemIndex;         //滤波方式 0: 单滤波 1: 双滤波
        InitConfig.Mode=ComboBoxMode->ItemIndex;             //模式  0:正常模式 1: 只听模式 2: 自检测模式

        InitConfig.Timing0 = StrToInt("0x"+EditTimer0->Text);//波特率设置
	InitConfig.Timing1 = StrToInt("0x"+EditTimer1->Text);
        
        if(CANIndex>=0)
        {
                if(VCI_OpenDevice(DevIndex))
                {
                   if(CheckBoxAllCAN->Checked==true)  //打开二个通道
                   {
                         //打开CAN0通道
                        if(VCI_InitCan(DevIndex,0, &InitConfig)==true)
                        {
                                ButtonConnect->Caption ="断开";

                                Device_Connect=true;  //设备已连接并正确初始化

                                ListBoxReceiveCan0->Items->Add("初始化CAN0成功");

                                DeviceCan0Open=true;   //CAN0已经成功打开

                                _beginthread(ReceiveThreadCan0,0,(void*)ListBoxReceiveCan0); //启动接受数据线程


                        }
                        else
                        {
                                ShowMessage("初始化CAN0错误");
                        }

                        //打开CAN1通道
                        if(VCI_InitCan(DevIndex,1, &InitConfig)==true)
                        {
                                ButtonConnect->Caption ="断开";

                                Device_Connect=true;  //设备已连接并正确初始化

                                ListBoxReceiveCan1->Items->Add("初始化CAN1成功");

                                DeviceCan1Open=true;  //CAN1已经成功打开

                                _beginthread(ReceiveThreadCan1,0,(void*)ListBoxReceiveCan1); //启动接受数据线程

                        }
                        else
                        {
                                ShowMessage("初始化CAN1错误");
                        }



                   }                                       //打开对应通道
                   else
                   { 
                        if(VCI_InitCan(DevIndex,CANIndex, &InitConfig))
                        {
                                ButtonConnect->Caption ="断开";

                                Device_Connect=true;  //设备已连接并正确初始化

                                if(CANIndex==0)
                                {
                                   DeviceCan0Open=true;

                                   ListBoxReceiveCan0->Items->Add("初始化CAN" + IntToStr(CANIndex) +"成功");

                                  _beginthread(ReceiveThreadCan0,0,(void*)ListBoxReceiveCan0); //启动接受数据线程
                                }
                                else
                                {
                                  DeviceCan1Open=true;

                                  ListBoxReceiveCan1->Items->Add("初始化CAN" + IntToStr(CANIndex) +"成功");

                                 _beginthread(ReceiveThreadCan1,0,(void*)ListBoxReceiveCan1); //启动接受数据线程
                                }

                        }
                        else
                        {
                                ShowMessage("初始化CAN" + IntToStr(CANIndex) +"错误");
                        }

                   }
                }
                else
                {
                        ShowMessage("打开设备错误");
                }

        }
}
//---------------------------------------------------------------------------

void __fastcall TMainForm::ButtonResetClick(TObject *Sender)
{
        if(Device_Connect==false)
        {
                ShowMessage("请先打开端口");
                return;
        }
        if(CheckBoxAllCAN->Checked==true)  //复位二个通道
        {
             //复位通道0
             if(VCI_ResetCan(DevIndex,0)==true)
             {
                ListBoxReceiveCan0->Items->Add("复位CAN0成功");
             }
             else
             {
                ListBoxReceiveCan0->Items->Add("复位CAN0失败");
             }
             //复位通道1
              if(VCI_ResetCan(DevIndex,1)==true)
             {
                ListBoxReceiveCan1->Items->Add("复位CAN1成功");
             }
             else
             {
                ListBoxReceiveCan1->Items->Add("复位CAN1失败");
             }


        }
        else
        {
          if(CANIndex==0)//CAN0
          {
             //复位对应通道
             if(VCI_ResetCan(DevIndex,CANIndex)==true)
             {
                ListBoxReceiveCan0->Items->Add("复位CAN" + IntToStr(CANIndex) +"成功");
             }
             else
             {
                ListBoxReceiveCan0->Items->Add("复位CAN" + IntToStr(CANIndex) +"失败");
             }
           }
           else          //CAN1
           {
             //复位对应通道
             if(VCI_ResetCan(DevIndex,CANIndex)==true)
             {
                ListBoxReceiveCan1->Items->Add("复位CAN" + IntToStr(CANIndex) +"成功");
             }
             else
             {
                ListBoxReceiveCan1->Items->Add("复位CAN" + IntToStr(CANIndex) +"失败");
             }

           }
        }
}
//---------------------------------------------------------------------------






void __fastcall TMainForm::FormCreate(TObject *Sender)
{

      ComboBoxCanChannel->ItemIndex = 0;
      ComboBoxFilter->ItemIndex = 0;
      ComboBoxMode->ItemIndex = 0;
      ComboBoxFrameType->ItemIndex =0;
      ComboBoxFrameFormat->ItemIndex =0;  
}

//---------------------------------------------------------------------------


void __fastcall TMainForm::ButtonSendClick(TObject *Sender)
{


        if(Device_Connect==false)
        {
                ShowMessage("请先打开端口");
                return;
        }

        FrameType=ComboBoxFrameType->ItemIndex;        //帧类型
        FrameFormat=ComboBoxFrameFormat->ItemIndex;    //帧格式
        FrameID=StrToInt("0x"+EditFrameID->Text);      //帧ID

        AnsiString str=EditData->Text;
        AnsiString strdata;

        int i,kkk;                                     //整理数据
        for(i=0;i<8;i++)
        {
                strdata=str.SubString(3*i+1,2);
                strdata=strdata.Trim();
                kkk=strdata.Length();
                if(kkk==0)
                {
                        goto exit;
                }
                FrameData[i]=StrToInt("0x"+strdata);

        }

exit:
        //整理好的数据存入发送数据的结构体
        SendData.SendType =ComboBoxSendType->ItemIndex;//存入发送类型，正常发送--0, 自发自收--1
        SendData.ExternFlag=FrameType;                 //存入帧类型，标准帧--0,扩展帧--1
        SendData.RemoteFlag=FrameFormat;               //存入帧格式 ,数据帧--0,远程帧--1
        SendData.ID        =FrameID ;                  //存入帧ID
        SendData.DataLen=i;                           //存入数据长度 <8
        memcpy(SendData.Data,FrameData,i);            //存入数据

       
          //对应通道发送

        if(ComboBoxCanChannel->ItemIndex==0)//CAN0
        {
           if(VCI_Transmit(DevIndex,ComboBoxCanChannel->ItemIndex,&SendData)==true)
           {
                ListBoxReceiveCan0->Items->Add("设备"+IntToStr(DevIndex) +
                                           " 通道CAN" + IntToStr(ComboBoxCanChannel->ItemIndex) +"发送成功");
           }
           else
           {
                ListBoxReceiveCan0->Items->Add("设备"+IntToStr(DevIndex) +
                                           " 通道CAN" + IntToStr(ComboBoxCanChannel->ItemIndex) +"发送失败");
           }

        }else
        {
           if(VCI_Transmit(DevIndex,ComboBoxCanChannel->ItemIndex,&SendData)==true)
           {
                ListBoxReceiveCan1->Items->Add("设备"+IntToStr(DevIndex) +
                                           " 通道CAN" + IntToStr(ComboBoxCanChannel->ItemIndex) +"发送成功");
           }
           else
           {
                ListBoxReceiveCan1->Items->Add("设备"+IntToStr(DevIndex) +
                                           " 通道CAN" + IntToStr(ComboBoxCanChannel->ItemIndex) +"发送失败");
           }

        }
}
//---------------------------------------------------------------------------



void __fastcall TMainForm::ButtonClearClick(TObject *Sender)
{
  ListBoxReceiveCan0->Clear() ;
  ListBoxReceiveCan1->Clear() ;

  Can0TotalReceiveCount=0;                    //CAN0总共接受到的帧数
  Can1TotalReceiveCount=0;                    //CAN1总共接受到的帧数

  Can0SingleReceiveCount=0;                   //CAN0本次接受到的帧数
  Can1SingleReceiveCount=0;                   //CAN1本次接受到的帧数   
}
//---------------------------------------------------------------------------




