"""
CAN USB 上位机软件 - 打包脚本
使用 PyInstaller 打包成 exe 文件
"""

import PyInstaller.__main__
import os
import shutil

def build_exe():
    """打包 exe 文件"""

    # 清理旧的构建文件
    if os.path.exists('build'):
        shutil.rmtree('build')
    if os.path.exists('dist'):
        shutil.rmtree('dist')

    # 检查图标文件
    icon_file = None
    possible_icons = ['USBCAN.ico', 'icon.ico', 'app.ico']
    for icon in possible_icons:
        if os.path.exists(icon):
            icon_file = icon
            break

    # PyInstaller 参数
    args = [
        'can_host.py',              # 主程序入口
        '--name=USBCAN',      # exe 文件名
        '--onefile',                # 打包成单个 exe 文件
        '--windowed',               # 使用窗口模式（不显示控制台）
        '--clean',                  # 清理临时文件
        '--noconfirm',              # 不确认覆盖
    ]

    # 添加图标（如果存在）
    if icon_file:
        args.append(f'--icon={icon_file}')
        print(f"使用图标文件: {icon_file}")
    else:
        print("警告: 未找到 .ico 格式的图标文件，任务栏可能无法显示图标")
        print("支持的图标文件名: USBCAN.ico, icon.ico, app.ico")

    # 添加依赖文件
    args.extend([
        '--add-data=can_interface.py;.',
    ])

    # 运行 PyInstaller
    PyInstaller.__main__.run(args)

    print("\n" + "="*60)
    print("打包完成！")
    print("="*60)
    print(f"\nEXE 文件位置: {os.path.abspath('dist/CAN_USB_Host.exe')}")
    print("\n使用说明:")
    print("1. 将 dist/CAN_USB_Host.exe 复制到目标位置")
    print("2. 确保同目录下有 CAN_TO_USB.dll 和 SiUSBXp.dll")
    print("3. 运行 CAN_USB_Host.exe 即可")
    print("="*60)

if __name__ == "__main__":
    build_exe()
