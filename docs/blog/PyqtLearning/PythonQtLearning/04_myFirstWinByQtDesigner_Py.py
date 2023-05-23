from PySide2.QtWidgets import QApplication,QMainWindow
from _04_myFirstWin import Ui_window

import os
import PySide2

dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path


# 将GUI（包括主窗口及控件）以及用到的变量封装成类，程序运行时启动一个QApplication对象，然后创建GUI对象，设置主窗口显示，最后启动QApplication对象
class MyFirstWin(QMainWindow):  # --------注意：继承父类--------
    # 初始化函数：GUI，成员变量，信号与槽的绑定等
    def __init__(self):
        # 初始化父类
        super().__init__()  # --------注意：先初始化父类--------

        # 成员变量
        self.count = 0

        # 从文件中加载UI定义，创建一个相应的窗口对象
        # 注：里面的控件对象也成为窗口对象的属性
        self.ui = Ui_window()  # --------注意：创建UI对象--------

        # 初始化界面
        self.ui.setupUi(self)  # --------注意：调用UI对象的初始化函数--------

        # 信号与槽的绑定
        self.ui.btn.clicked.connect(self.countAdd)  # 按钮点击事件的信号与槽函数绑定，实现交互

    # 槽函数作为成员函数
    def countAdd(self):
        self.count += 1
        self.ui.label.setText('计数器：'+str(self.count))


if __name__ == '__main__':
    app = QApplication([])  # 创建Qt应用程序

    myApp = MyFirstWin()  # 创建GUI
    myApp.show()  # 设置主窗口显示（即：让ui定义的窗口显示）  # --------注意--------

    app.exec_()  # 启动Qt应用程序
