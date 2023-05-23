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
