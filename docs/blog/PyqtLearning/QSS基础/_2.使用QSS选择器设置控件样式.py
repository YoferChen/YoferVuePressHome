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
