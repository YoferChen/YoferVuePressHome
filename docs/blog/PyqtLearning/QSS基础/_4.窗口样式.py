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
