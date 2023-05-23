from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt
import sys


class LabelButtonBackground(QWidget):
    def __init__(self):
        super(LabelButtonBackground, self).__init__()
        label1 = QLabel(self)
        label1.setToolTip('这是一个文本标签')

        label1.setFixedWidth(200)
        label1.setFixedHeight(200)

        filename = '添加.png'
        img = QImage(filename)

        # img_scaled = img.scaled(label1.width(), label1.height(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        img_scaled = img.scaled(label1.width(), label1.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation)  # 保持长宽比例
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
