# Qt样式

## 1.通过窗口对象设置样式

```python
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QApplication
import sys


class QSSBasic(QWidget):
    def __init__(self):
        super(QSSBasic, self).__init__()

        btn1 = QPushButton(self)
        btn1.setText('按钮1')
        btn2 = QPushButton(self)
        btn2.setText('按钮2')
        btn3 = QPushButton(self)
        btn3.setText('按钮3')

        lay = QVBoxLayout()
        lay.addWidget(btn1)
        lay.addWidget(btn2)
        lay.addWidget(btn3)

        self.setLayout(lay)

        # 设置样式
        qssStyle = '''
            QPushButton{
                background-color:yellow;
            }
        '''
        self.setStyleSheet(qssStyle)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QSSBasic()
    win.show()
    sys.exit(app.exec_())

```

## 2.使用QSS选择器设置控件样式

```python
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QApplication
import sys


class QSSSelector(QWidget):
    def __init__(self):
        super(QSSSelector, self).__init__()

        btn1 = QPushButton(self)
        btn1.setText('按钮1')
        btn1.setProperty('name', 'btn1')  # 为控件设置属性
        btn2 = QPushButton(self)
        btn2.setText('按钮2')
        btn3 = QPushButton(self)
        btn3.setText('按钮3')

        lay = QVBoxLayout()
        lay.addWidget(btn1)
        lay.addWidget(btn2)
        lay.addWidget(btn3)

        self.setLayout(lay)

        # 设置样式
        qssStyle = '''
            QPushButton[name='btn1']{
                background-color:yellow;
            }
        '''
        self.setStyleSheet(qssStyle)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QSSSelector()
    win.show()
    sys.exit(app.exec_())

```

## 3.子控件选择器

## 

```python
from PyQt5.QtWidgets import QWidget, QComboBox, QVBoxLayout, QApplication
import sys


class QSSSubControl(QWidget):
    def __init__(self):
        super(QSSSubControl, self).__init__()

        self.setWindowTitle('QSS子控件选择器')
        combobox=QComboBox(self)
        combobox.setObjectName('myComboBox')
        combobox.addItem('Windows')
        combobox.addItem('Linux')
        combobox.addItem('Unix')

        combobox.move(50,50)

        self.setGeometry(250,200,320,150)

        # 设置样式【#号相当于id；::后为子控件】
        qssStyle = '''
            QComboBox#myComboBox::drop-down{
                image:url(下拉.png)
            }
        '''
        self.setStyleSheet(qssStyle)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QSSSubControl()
    win.show()
    sys.exit(app.exec_())

```



## 4.窗口样式

```python
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class WindowPattern(QMainWindow):
    def __init__(self):
        super(WindowPattern, self).__init__()
        self.resize(500, 260)
        self.setWindowTitle('设置窗口的样式')

        # self.setWindowFlags(Qt.WindowMaximizeButtonHint | Qt.WindowStaysOnTopHint|Qt.FramelessWindowHint)
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMaximizeButtonHint|Qt.WindowMinimizeButtonHint)
        self.setObjectName('MainWindow')
        self.setStyleSheet("#MainWindow{border-image:url(背景.jpg);}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = WindowPattern()
    win.show()
    sys.exit(app.exec_())

```



## 5.为标签和按钮添加背景图

```python
from PyQt5.QtWidgets import *
import sys


class LabelButtonBackground(QWidget):
    def __init__(self):
        super(LabelButtonBackground, self).__init__()
        label1=QLabel(self)
        label1.setToolTip('这是一个文本标签')
        label1.setStyleSheet("QLabel{border-image:url('背景.jpg');}")

        label1.setFixedWidth(476)
        label1.setFixedHeight(259)

        btn1 = QPushButton(self)
        btn1.setObjectName('btn1')
        btn1.setFixedWidth(200)
        btn1.setFixedHeight(200)

        style = '''
            #btn1{
                background-image:url('添加.png');
            }
            #btn1:Pressed{
                background-image:url('已添加.png');
            }
        '''

        btn1.setStyleSheet(style)

        lay = QVBoxLayout()
        lay.addWidget(label1)
        lay.addStretch()
        lay.addWidget(btn1)

        self.setLayout(lay)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LabelButtonBackground()
    win.show()
    sys.exit(app.exec_())

```



## 6.缩放图片

```python
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt
import sys


class LabelButtonBackground(QWidget):
    def __init__(self):
        super(LabelButtonBackground, self).__init__()
        label1 = QLabel(self)
        label1.setToolTip('这是一个文本标签')

        label1.setFixedWidth(100)
        label1.setFixedHeight(200)

        filename = '添加.png'
        img = QImage(filename)

        # img_scaled = img.scaled(label1.width(), label1.height(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        img_scaled = img.scaled(label1.width(), label1.height(),Qt.KeepAspectRatio, Qt.SmoothTransformation)
        label1.setPixmap(QPixmap.fromImage(img_scaled))

        lay = QVBoxLayout()
        lay.addWidget(label1)
        lay.addStretch()

        self.setLayout(lay)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LabelButtonBackground()
    win.show()
    sys.exit(app.exec_())

```



## 7.窗口透明效果

```python
from PyQt5.Qt import *
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setWindowTitle('窗口透明效果')
    win.setWindowOpacity(0.1)
    win.resize(400, 200)
    win.show()
    sys.exit(app.exec_())

```















