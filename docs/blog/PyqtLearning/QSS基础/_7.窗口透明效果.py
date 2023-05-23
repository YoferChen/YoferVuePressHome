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
