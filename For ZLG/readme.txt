
Dll     :  兼容ZLG CAN卡的dll

Document:  编程手册 

Drivers :  CAN卡驱动程序

Examples:  应用例程从ZLG提供的例程而来，直接用ControlCAN.dll和SiUSBXp.dll替换ZLG的ControlCAN.dll即可

           源代码无需改动，例程是针对CANUSB-II的其它CAN卡类似，函数参数不同的只是类型号。

           VB:           Visual Basic 6.0 单个CANUSB设备操作的示例

           VC:           Visual C++   6.0 单个CANUSB设备操作的示例

           BCB:          C++Builder 6.0   单个CANUSB设备操作的示例         

           Delphi:       Delphi7.0        单个CANUSB设备操作的示例 

           Labview:      Labviwe8.6       单个CANUSB设备操作的示例


ZLGCANTest：ZLG的测试程序(直接用ControlCAN.dll和SiUSBXp.dll替换了ZLG的ControlCAN.dll)
            

CAN卡型号和ZLG CAN卡的对应关系：

           #define VCI_PCI5121    1  //对应PCI-68XX
           #define VCI_PCI9810    2  //对应PCI-5810I
           #define VCI_USBCAN1    3  //对应CANUSB-I  
           #define VCI_USBCAN2    4  //对应CANUSB-II
           #define VCI_PCI9820    5  //对应PCI-5820I
           #define VCI_PCI9820I  16  //对应PCI-5820I
            
 

                        
           
