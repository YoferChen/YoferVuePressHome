from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader  # --------注意：引入ui文件加载模块--------

import os
import PySide2

dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path


# 将GUI（包括主窗口及控件）以及用到的变量封装成类，程序运行时启动一个QApplication对象，然后创建GUI对象，设置主窗口显示，最后启动QApplication对象
class MyFirstWin():
    # 初始化函数：GUI，成员变量，信号与槽的绑定等
    def __init__(self):
        # 成员变量
        self.count = 0

        # 从文件中加载UI定义，创建一个相应的窗口对象
        # 注：里面的控件对象也成为窗口对象的属性
        self.ui = QUiLoader().load('04_myFirstWin.ui')  # UI中定义的控件可通过self.ui.XXX进行访问  # --------注意：加载ui文件--------

        # 信号与槽的绑定
        self.ui.btn.clicked.connect(self.countAdd)  # 按钮点击事件的信号与槽函数绑定，实现交互  # --------注意：通过self.ui访问控件--------

    # 槽函数作为成员函数
    def countAdd(self):
        self.count += 1
        self.ui.label.setText('计数器：'+str(self.count))


if __name__ == '__main__':
    app = QApplication([])  # 创建Qt应用程序

    myApp = MyFirstWin()  # 创建GUI
    myApp.ui.show()  # 设置主窗口显示（即：让ui定义的窗口显示）  # --------注意：设置ui显示--------

    app.exec_()  # 启动Qt应用程序
