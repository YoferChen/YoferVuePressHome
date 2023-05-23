from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton

import os
import PySide2

dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

app = QApplication([])  # 创建Qt应用程序

window = QMainWindow()  # 初始化一个QMainWindow类型窗口
window.resize(400, 200)
window.move(300, 310)
window.setWindowTitle('My First Window')

count = 0

label = QLabel(window)  # 参数指定父窗口
label.setText(str(count))
label.move(100, 100)  # 位置相对于父组件移动(右移，下移)个像素

btn = QPushButton(window)
btn.setText('点击我，让数字+1')
btn.move(200, 100)


# 按钮点击事件的信号与槽函数绑定，实现交互
def countAdd():
    global count
    count += 1
    label.setText(str(count))


btn.clicked.connect(countAdd)  # 参数为函数对象

window.show()  # 设置主窗口显示

app.exec_()  # 启动Qt应用程序
