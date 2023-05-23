from PyQt5.QtWidgets import *
import sys


class LabelButtonBackground(QWidget):
    def __init__(self):
        super(LabelButtonBackground, self).__init__()
        label1=QLabel(self)
        label1.setToolTip('这是一个文本标签')
        label1.setStyleSheet("QLabel{border-image:url('背景.jpg');}")  # QLabel设置背景图

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

        btn1.setStyleSheet(style)  # 为按钮添加背景图

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
