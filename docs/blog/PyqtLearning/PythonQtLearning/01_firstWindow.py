from PySide2.QtWidgets import QApplication, QMainWindow, QLabel

import os
import PySide2

dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

app = QApplication([])  # 创建Qt应用程序

window = QMainWindow()  # 初始化一个QMainWindow类型窗口
window.resize(500, 400)
window.move(300, 310)
window.setWindowTitle('My First Window')

label = QLabel(window)  # 参数指定父窗口
label.setText('Hello World!')

window.show()  # 设置主窗口显示

app.exec_()  # 启动Qt应用程序
