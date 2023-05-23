from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton

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

        # 主窗口
        self.window = QMainWindow()
        self.window.resize(400, 200)
        self.window.move(300, 310)
        self.window.setWindowTitle('My First Window')

        # 控件（嵌入主窗口）
        self.label = QLabel(self.window)  # 参数指定父窗口
        self.label.setText(str(self.count))
        self.label.move(100, 100)  # 位置相对于父组件移动(右移，下移)个像素

        self.btn = QPushButton(self.window)
        self.btn.setText('点击我，让数字+1')
        self.btn.move(200, 100)

        # 信号与槽的绑定
        self.btn.clicked.connect(self.countAdd)  # 按钮点击事件的信号与槽函数绑定，实现交互

    # 槽函数作为成员函数
    def countAdd(self):
        self.count += 1
        self.label.setText(str(self.count))


if __name__ == '__main__':
    app = QApplication([])  # 创建Qt应用程序

    myApp = MyFirstWin()  # 创建GUI
    myApp.window.show()  # 设置主窗口显示

    app.exec_()  # 启动Qt应用程序
