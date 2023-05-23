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
