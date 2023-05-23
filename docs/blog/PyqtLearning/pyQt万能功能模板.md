## PyQt5万能功能模板

- Author：浅若清风cyf



## QWidget与QLayout

### 父窗口创建子窗口

> 注意将子窗口对象声明为父窗口对象的成员，不能是函数中的局部变量，运行后会崩溃！

### 从layout中移除控件

```python
self.layout.itemAt(i).widget().deleteLater()
```

### Widget嵌入带布局的子组件

```python
## 层次关系：widget→layout→widget
## 假设父widget为self.ui.father_widget
##
self.lay=QVBoxLayout(self.ui.father_widget)
self.subWidget=QWidget()
self.lay.addWidget(self.subWidget)
```

### 设为窗口为模态框

```python
from PyQt5.QtCore import Qt

myWin = MainWin()
myWin.setWindowModality(Qt.ApplicationModal)
```

## QMessageBox

### 基本使用

```python
reply = QMessageBox.information(self, '标题','消息对话框正文',QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
reply1 = QMessageBox.question(self, "标题", "提问框消息正文", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
reply2 = QMessageBox.warning(self, "标题", "警告框消息正文", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
reply3 = QMessageBox.critical(self, "标题", "严重错误对话框消息正文", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
reply4 = QMessageBox.about(self, "标题", "关于对话框消息正文")
```

### 按钮文字自定义

```python
def showCustomMessageBox(self):
    save, discard, cancel = QMessageBox.Save, QMessageBox.Discard, QMessageBox.Cancel

    if self.config.language == 'zh_CN':
        msg = '图片未保存，是否保存'
        msg_box = QMessageBox(QMessageBox.Warning, '保存修改？', msg)
        icon = QIcon('./resources/logo.png')
        msg_box.setWindowIcon(icon
        msg_box.setStandardButtons(save|discard|cancel)
        btn_save = msg_box.button(QMessageBox.Save)
        btn_save.setText('保存')
        btn_discard=msg_box.button(QMessageBox.Discard)
        btn_discard.setText('不保存')
        btn_cancel=msg_box.button(QMessageBox.Cancel)
        btn_cancel.setText('取消')
        msg_box.exec_()

        if msg_box.clickedButton() == btn_cancel:
            print('点击取消')
            e.ignore()
        elif msg_box.clickedButton()==btn_discard:
            print('不保存')
            e.accept()
        elif msg_box.clickedButton()==btn_save:
            print('保存')
            if not self.saveFile():
                e.ignore()
                return
            e.accept()

        ## reply = QMessageBox.warning(self, '保存修改？', msg, save | discard | cancel, save)

    else:
        msg = 'Do you want to save the picture?'
        reply = QMessageBox.warning(self, 'Save changes?', msg, save | discard | cancel, save)
        if reply == QMessageBox.Cancel:
            e.ignore()
        elif reply == QMessageBox.Discard:
            e.accept()
        elif reply == QMessageBox.Save:
            if not self.saveFile():
                e.ignore()
                return
            e.accept()
```

### 定制版：支持中英文、自定义按钮、按钮美化

```python
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt
import sys
import resources.resources_qt5

def message_win(title, msg, btn_list, default_btn, type='warning', language='zh_CN', icon=None):
    '''
    封装QMessageBox，支持按钮中文显示
    两种模式弹出对话框：1、自定义QMessageBox，2、继承parent
    '''

    style_true = '''
                width: 76px;
                height: 24px;
                background: rgba(0, 164, 255, 0.05);
                border: 1px solid rgba(0, 164, 255, 0.2);
                font-family: "Microsoft YaHei";
                font-weight: 400;
                font-size: 14px;
                color: ##00a4ff;
                text-align:center; 
    '''
    style_false = '''
        width: 76px;
        height: 24px;
        background: rgba(26, 155, 82, 0.05);
        border: 1px solid rgba(26, 155, 82, 0.2);
        font-family: "Microsoft YaHei";
        font-weight: 400;
        font-size: 14px;
        color: ##1a9b52;
        text-align:center; 
    '''
    style_cancel = '''
        width: 76px;
        height: 24px;
        background: rgba(80, 80, 80, 0.05);
        border: 1px solid rgba(80, 80, 80, 0.2);
        font-family: "Microsoft YaHei";
        font-weight: 400;
        font-size: 14px;
        color: ##5a5a5a;
        text-align:center; 
    '''

    ## if language == 'zh_CN':
    if type == 'warning':
        msg_box = QMessageBox(QMessageBox.Warning, title, msg)
    elif type == 'information':
        msg_box = QMessageBox(QMessageBox.Information, title, msg)
    elif type == 'critical':
        msg_box = QMessageBox(QMessageBox.Critical, title, msg)
    elif type == 'question':
        msg_box = QMessageBox(QMessageBox.Question, title, msg)
    else:
        return None

    if icon is None:
        my_icon = QIcon(':/logo2.png')
    else:
        my_icon = icon
    msg_box.setWindowIcon(my_icon)
    msg_box.setStandardButtons(btn_list)

    btn_save = msg_box.button(QMessageBox.Save)
    if btn_save is not None:
        if language == 'zh_CN':
            btn_save.setText('保存')
        btn_save.setStyleSheet(style_true)

    btn_discard = msg_box.button(QMessageBox.Discard)
    if btn_discard is not None:
        if language == 'zh_CN':
            btn_discard.setText('不保存')
        btn_discard.setStyleSheet(style_false)

    btn_cancel = msg_box.button(QMessageBox.Cancel)
    if btn_cancel is not None:
        if language == 'zh_CN':
            btn_cancel.setText('取消')
        btn_cancel.setStyleSheet(style_cancel)

    btn_ok = msg_box.button(QMessageBox.Ok)
    if btn_ok is not None:
        if language == 'zh_CN':
            btn_ok.setText('好的')
        btn_ok.setStyleSheet(style_true)

    btn_no = msg_box.button(QMessageBox.No)
    if btn_no is not None:
        if language == 'zh_CN':
            btn_no.setText('否')
        btn_no.setStyleSheet(style_false)

    btn_yes = msg_box.button(QMessageBox.Yes)
    if btn_yes is not None:
        if language == 'zh_CN':
            btn_yes.setText('是')
        btn_yes.setStyleSheet(style_true)

    msg_box.setDefaultButton(msg_box.button(default_btn))

    ## child_list = msg_box.children()
    ## for i in range(len(child_list)):
    ##     obj = child_list[i]
    ##     if obj.inherits("QWidget"):
    ##         obj.setStyleSheet("background-color: transparent;font-family: Microsoft YaHei;")

    style = '''
        background-color:white;
        font-family: "Microsoft YaHei";
        font-weight: 400;
        font-size: 14px;
        color: ##1a1a1a;
        text-align:center; 
    '''
    msg_box.setStyleSheet(style)
    ## msg_box.setWindowFlags(Qt.FramelessWindowHint)
    msg_box.exec_()

    if msg_box.clickedButton() == btn_ok:
        return QMessageBox.Ok
    elif msg_box.clickedButton() == btn_cancel:
        return QMessageBox.Cancel
    elif msg_box.clickedButton() == btn_discard:
        return QMessageBox.Discard
    elif msg_box.clickedButton() == btn_save:
        return QMessageBox.Save
    elif msg_box.clickedButton() == btn_yes:
        return QMessageBox.Yes
    elif msg_box.clickedButton() == btn_no:
        return QMessageBox.No

        ## reply = QMessageBox.warning(self, '保存修改？', msg, save | discard | cancel, save)

    ## else:
    ##     if type == 'warning':
    ##         return QMessageBox.warning(parent, title, msg, btn_list, default_btn)
    ##     elif type == 'information':
    ##         return QMessageBox.information(parent, title, msg, btn_list, default_btn)
    ##     elif type == 'critical':
    ##         return QMessageBox.critical(parent, title, msg, btn_list, default_btn)
    ##     else:
    ##         return None


class MyWin(QWidget):
    '''
    测试用
    '''

    def __init__(self):
        super(MyWin, self).__init__()
        ## self.resize(100, 100)
        icon = QIcon(':/logo2.png')
        self.setWindowIcon(icon)
        ## 继承parent的icon
        message_win(title='title', msg='msg', btn_list=QMessageBox.Yes | QMessageBox.No,
                    default_btn=QMessageBox.Yes, language='en')
        ## self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ## 中文
    reply = message_win(title='标题', msg='提示内容', btn_list=QMessageBox.Yes | QMessageBox.No|QMessageBox.Cancel,
                        default_btn=QMessageBox.Yes, language='zh_CN')
    print(reply)
    ##
    ## reply = message_win(title='标题', msg='提示内容', btn_list=QMessageBox.Yes | QMessageBox.No|QMessageBox.Cancel,
    ##                     default_btn=QMessageBox.Yes, language='zh_CN',type='information')
    ## print(reply)
    ##
    ## reply = message_win(title='标题', msg='提示内容', btn_list=QMessageBox.Yes | QMessageBox.No|QMessageBox.Cancel,
    ##                     default_btn=QMessageBox.Yes, language='zh_CN',type='critical')
    ## print(reply)
    ## 英文（不继承）
    reply = message_win( title='title', msg='msg', btn_list=QMessageBox.Yes | QMessageBox.No,
                        default_btn=QMessageBox.Yes, language='en')
    print(reply)
    ## 英文（继承）
    ## win = MyWin()
    sys.exit(app.exec_())

```

## QLabel

### 设置图标

```python
label = QLabel()
label.setPixmap(QtGui.QPixmap(":/resources/模型设置.png"))
```

## QListWidget

![image-20220505123808092](/funtions/image-20220505123808092.png)

### item可拖拽调整顺序、删除、双击弹出二级菜单、右键移动控件

```python
'''
    包含可拖动item的QListWidget
    两种模式：mode=files或mode=dirs
    功能：
        拖拽调整item顺序
        右键菜单：上移、下移
        mode=dirs情况下：
            双击可弹窗，调整二级列表顺序
'''

from PyQt5.QtWidgets import QApplication, QListWidgetItem, QWidget, QHBoxLayout, QListWidget, QSpacerItem, QPushButton, \
    QSizePolicy, QMenu, QMessageBox
from PyQt5 import QtCore
import PyQt5.sip as sip
from PyQt5.QtCore import pyqtSignal
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QModelIndex


class FileDirListItemWidget(QWidget):
    signal_delItem = pyqtSignal(str)  ## 删除item信号
    signal_moveUp = pyqtSignal(str)  ## 上移item信号
    signal_moveDown = pyqtSignal(str)  ## 下移item信号

    def __init__(self, text, parent=None):
        super(FileDirListItemWidget, self).__init__(parent=parent)
        self.text = text
        self.setup()

    def setup(self):
        '''
        初始化itemWidget
        :return:
        '''
        ## 布局层（组件添加到layout上）
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        ## 弹簧
        self.spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Expanding)

        ## 删除按钮
        self.del_btn = QPushButton("×")
        self.del_btn.setFixedWidth(30)
        self.del_btn.clicked.connect(self.on_delete)

        ## 右键菜单
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.custom_right_menu)

        ## 控件加入layout
        self.layout.addItem(self.spacer)
        self.layout.addWidget(self.del_btn)

    def on_delete(self):
        '''
        删除按钮的槽函数
        :return:
        '''
        self.signal_delItem.emit(self.text)  ## 向父组件传递item的text，父组件根据text删除item

    def custom_right_menu(self, pos):
        '''
        右键菜单
        :param pos:
        :return:
        '''
        menu = QMenu()
        opt1 = menu.addAction("上移")
        opt2 = menu.addAction("下移")

        action = menu.exec_(self.mapToGlobal(pos))

        if action == opt1:
            print('点击上移', self.text)
            self.signal_moveUp.emit(self.text)
        elif action == opt2:
            print('点击下移', self.text)
            self.signal_moveDown.emit(self.text)


class FileDirListWidget(QListWidget):
    '''
    QListWidget窗口，用于调整item（顺序、删除）
    '''
    signal_subLabelsWidgetClose = pyqtSignal(list)  ## 窗口关闭信号

    def __init__(self, labels=None, subLabels=None, mode='files'):
        '''
            mode可选：files、dirs
            dirs模式下，item双击可弹出新窗口，调整subLabels顺序
        :param labels:
        :param mode:
        '''
        super(FileDirListWidget, self).__init__()
        print('mode:', mode)
        print('labels=',labels)
        print('subLabels=',subLabels)

        self.labels = labels        ## files/dirs
        self.subLabels = subLabels  ## None/files
        self.mode = mode
        self.setup()
        self.setDragDropMode(QListWidget.InternalMove)  ## 设置item拖拽模式
        self.fileListWidget = None

    def setup(self):
        '''
        初始化：添加item
        :return:
        '''
        ## for label in self.labels:
        ##     self.addItemWidget(label)
        self.add_items()

        ## 事件绑定
        ## 双击item事件
        if self.mode == 'dirs':
            self.doubleClicked.connect(self.on_itemDoubleClicked)

    def add_items(self):
        '''
        向widget添加items
        :return:
        '''
        self.clear()
        print('self.labels=',self.labels)
        if self.labels is not None:
            for label in self.labels:
                self.addItemWidget(label)

    def del_Item(self, text):
        '''
        删除指定text的item
        :param text:
        :return:
        '''
        print('删除item：', text)
        for i in range(self.count()):
            item_i = self.item(i)
            if self.itemWidget(item_i).text == text:
                self.takeItem(i)
                sip.delete(item_i)
                self.labels.pop(i)  ## 删除索引为i的元素
                break
        print('当前的文件列表：', self.labels)

    def update_subLabels(self, labels):
        '''
        dirs模式下，返回子窗口调整顺序后的labels，并更新sublabels
        :return:
        '''
        print('调整后的的labels：', labels)
        print('准备更新subLabels...')
        self.subLabels[str(self.select_dir)]=labels
        print('更新后的文件顺序：',self.subLabels[str(self.select_dir)])
        ## print(self.subLabels)
        print('subLabels已更新...')


    def on_itemDoubleClicked(self, modelindex: QModelIndex):
        print(self.subLabels)
        item = self.item(modelindex.row())  ## 获取双击的item
        ## print(modelindex.row())
        dir_name = item.text()
        self.select_dir=dir_name
        print(dir_name)
        print(self.subLabels)
        print(self.subLabels.get(dir_name))
        labels = self.subLabels.get(dir_name)
        self.fileListWidget = FileDirListWidget(labels, 'files')
        self.fileListWidget.resize(400,300)
        self.fileListWidget.signal_subLabelsWidgetClose.connect(self.update_subLabels)
        self.fileListWidget.show()
        ## 重写窗口关闭事件，将调整后的file顺序返回

    def on_labelUp(self, text):
        '''
        点击的label上移
        :return:
        '''
        for i in range(len(self.labels)):
            if self.labels[i] == text:
                if i == 0:
                    print('选中第一个item，无法上移！')
                    res = QMessageBox.critical(self, "警告", "选中第一个文件，无法上移！", QMessageBox.Yes | QMessageBox.No,
                                               QMessageBox.Yes)
                    ## print(res)
                    return

                tmp = self.labels[i]
                self.labels[i] = self.labels[i - 1]
                self.labels[i - 1] = tmp
                ## 更新items
                self.add_items()
                break

    def on_labelDown(self, text):
        '''
        点击的label下移
        :return:
        '''
        for i in range(len(self.labels)):
            if self.labels[i] == text:
                if i == len(self.labels) - 1:
                    print('选中最后一个item，无法下移！')
                    res = QMessageBox.critical(self, "警告", "选中最后一个文件，无法下移！", QMessageBox.Yes | QMessageBox.No,
                                               QMessageBox.Yes)
                    ## print(res)
                    return

                tmp = self.labels[i]
                self.labels[i] = self.labels[i + 1]
                self.labels[i + 1] = tmp
                ## 更新items
                self.add_items()
                break

    def addItemWidget(self, label):
        '''
        向widget中添加itemWidget
        :param label:
        :return:
        '''
        ## 新建itemWidget
        item_widget = FileDirListItemWidget(text=label)

        ## 信号绑定
        item_widget.signal_delItem.connect(self.del_Item)
        item_widget.signal_moveUp.connect(self.on_labelUp)
        item_widget.signal_moveDown.connect(self.on_labelDown)

        item = QListWidgetItem(label)
        item.setSizeHint(QtCore.QSize(200, 30))

        self.addItem(item)
        self.setItemWidget(item, item_widget)

    def dropEvent(self, event) -> None:
        '''
        重写拖拽事件
        :param event:
        :return:
        '''
        super(FileDirListWidget, self).dropEvent(event)
        res_list = []
        for i in range(self.count()):
            item_i = self.item(i)
            res_list.append(item_i.text())
        self.labels = res_list
        print('当前的列表：', self.labels)

    def closeEvent(self, event):
        '''
        重写窗口关闭事件，用于dirs模式
        :param event:
        :return:
        '''
        if self.mode == 'files':
            reply = QMessageBox.question(self,
                                         '保存修改？',
                                         "是否保存对文件列表的修改？",
                                         QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.signal_subLabelsWidgetClose.emit(self.labels)
                print('更新数据完成，关闭窗口...')
                event.accept()
            else:
                event.accept()



if __name__ == "__main__":
    app = QApplication(sys.argv)

    ## labels = [str(i + 1) + '.jpg' for i in range(10)]
    ## myshow = FileDirListWidget(labels)

    dirs_num = 10
    labels = [str(i + 1) + '' for i in range(dirs_num)]
    subLabels = {str(key + 1): [str(i + 1) + '.jpg' for i in range(5)] for key in range(dirs_num)}
    print(labels)
    print(subLabels)
    myshow = FileDirListWidget(labels, subLabels, 'dirs')
    myshow.show()
    sys.exit(app.exec_())

```

## QCheckBox

```python
## 勾选状态事件与槽函数
self.ui.checkBox.stateChanged.connect(self.state_changed)

## 槽函数
def state_changed(self, state):
    print('状态设置为：', state)
    if state==2:  ## 勾选
        print('选项已勾选')
    elif state==0:  ## 取消勾选
        print('选项已取消勾选')
```



## QFileDialog

### 文件类型列表设置

- QFileDialog.getSaveFileName

```python
def save_dialog(self):
        """Save Image in image formats(PNG,JPEG,BMP,TIFF)
        """
        ## 不同文件扩展名以;;分隔；选择对应项后，会自动设置文件名的扩展名为()中的类型
        files_types = "PNG (*.png);;JPEG (*.jpeg);;TIFF (*.tiff);;BMP(*.bmp)"
        fileName, _ = QFileDialog.getSaveFileName(self, 'Export_Name', os.getenv('HOME'), "untitled.png"),files_types)
        fName = str(fileName)
        file_extension = fName.split(".")[-1]

        if file_extension == 'png' or file_extension == 'jpeg' or file_extension == 'bmp' or file_extension == 'tiff':

            QMessageBox.about(self, 'Information', "File saved")
```

## QPushButton

### 基本事件绑定

```python
self.ui.pBtn.clicked.connect(self.slotA)
```



### 绑定颜色选择器

- 参考：[PyQt5 ColorDialog(颜色选择器) 学习 - 简书 (jianshu.com)](https://www.jianshu.com/p/8475c0aa3334)

```python
self.ui.pBtnColorSelector.clicked.connect(self.setColor)

def colorSelector(self):
    ## 弹出颜色选择对话框
    color = QColorDialog.getColor()

    ## 检测用的选择是否合法(点击cancel就是非法,否则就是合法)
    if color.isValid():
        return color.name()
    else:
        return False

def setColor(self):
    color = self.colorSelector()
    if color:
        self.ui.pBtnColorSelector.setStyleSheet('QPushButton{background:%s};' % color)
```

## QTableWidget

### 添加包含控件的行&设置控件居中

![image-20220425124135720](/funtions/image-20220425124135720.png)

```python
def addRow(self, rowData: list):
    '''
        向单元格添加一行数据
        :param rowData:
        :return:
        '''
    self.ui.tableWidget.setRowCount(self.ui.tableWidget.rowCount() + 1)
    rowIndex = self.ui.tableWidget.rowCount() - 1
    itemOder = QTableWidgetItem(rowData[0])
    itemOder.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    self.ui.tableWidget.setItem(rowIndex, 0, itemOder)
    widgetColorTag = QWidget()
    btnColorTag = QPushButton()
    btnColorTag.setEnabled(False)
    btnColorTag.setStyleSheet('QPushButton{width: 28px;height: 28px;background:%s;border:none;}' % rowData[1])
    btnColorTag.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    layoutColorTag = QHBoxLayout()
    layoutColorTag.setContentsMargins(5, 5, 5, 5)
    layoutColorTag.addWidget(btnColorTag)
    widgetColorTag.setLayout(layoutColorTag)
    self.ui.tableWidget.setCellWidget(rowIndex, 1, widgetColorTag)
    itemTagName = QTableWidgetItem(rowData[2])
    itemTagName.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    self.ui.tableWidget.setItem(rowIndex, 2, itemTagName)
    widgetDelete = QWidget()
    btnOp = QPushButton('删除')
    btnOp.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
    btnOp.setStyleSheet('''
        QPushButton{
            width: 68px;
            height: 28px;
            background: ##252b41;
            border: 1px solid rgba(142, 159, 196, 0.3);
            font-family: "Microsoft YaHei";
            font-weight: 400;
            font-size: 14px;
            text-align: center;
            color: ##8e9fc4;
            border:none;
        }
        QPushButton:hover{
            background:#2c344b;
        }
        ''')
        layoutDelete = QHBoxLayout()
        layoutDelete.addWidget(btnOp)
        layoutDelete.setContentsMargins(5, 5, 5, 5)
        widgetDelete.setLayout(layoutDelete)
        self.ui.tableWidget.setCellWidget(rowIndex, 3, widgetDelete)
        self.ui.tableWidget.setRowHeight(rowIndex, 44)

```

### 单元格按钮绑定删除事件（获取控件所在行列）

- 基于QPoint和QModelIndex获取

```python
def deleteRow(self, btn: QPushButton):
    widget = btn.parentWidget()  ## 由于btn外面嵌套了一层widget，应该通过获取这个widget所在位置确定按钮的位置（直接获取btn的位置得到的行列永远是0,1）
    modelIndex = self.ui.tableWidget.indexAt(QPoint(widget.frameGeometry().x(), widget.frameGeometry().y()))
    print('点击了{}行{}列的按钮'.format(modelIndex.row(), modelIndex.column()))
    self.ui.tableWidget.removeRow(modelIndex.row())
```

## QListWidget

### 自定义QListWidgetItem

- 先创建一个QListWidgetItem添加到QListWidget中，通过setSizeHint设置QListWidgetItem的尺寸，防止自定义的Widget加入后显示不全
- 创建自定义的widget，通过self.ui.listWidget.setItemWidget(item, widget)替换原来的item

- ![image-20220427181256355](/funtions/image-20220427181256355.png)

```python
from PyQt5.QtWidgets import *
from PyQt5.Qt import Qt
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap
import sys
import wisdom_store.ui.main.resources_qt5

'''
自定义QListWidget的item的方法（item可包含多个控件）：
    先创建一个QListWidgetItem添加到QListWidget中，然后创建自定义的widget，之后通过self.ui.listWidget.setItemWidget(item, widget)替换原来的item
    
'''


class CustomItemWidget(QWidget):
    def __init__(self,text):
        super(CustomItemWidget, self).__init__()

        lay = QHBoxLayout()
        labelIcon = QLabel()
        labelIcon.setPixmap(QtGui.QPixmap(":/resources/模型设置.png"))
        labelIcon.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        labelIcon.setContentsMargins(5, 0, 5, 0)
        lay.addWidget(labelIcon)
        labelItemName = QLabel(text)
        labelItemName.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        labelItemName.setStyleSheet('''
            font-family: "Microsoft YaHei";
            font-weight: 400;
            font-size: 14px;
            color: ##dcefff;
            border: 1px solid rgba(0, 0, 0, 0);
        ''')
        lay.addWidget(labelItemName)
        labelIndicator = QLabel()
        labelIndicator.setPixmap(QtGui.QPixmap(":/resources/右箭头.png"))
        labelIndicator.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        lay.addWidget(labelIndicator)

        lay.setSpacing(0)
        self.setLayout(lay)


class CustomListWidget(QWidget):
    def __init__(self):
        super(CustomListWidget, self).__init__()
        self.resize(300, 600)
        self.listWidget = QListWidget()

        self.listWidget.setStyleSheet('''
            QListWidget{
                background: ##2c344b;
                border:none;
                outline:0px;  /*去除选中item外轮廓虚线*/
            }
            QListWidget::item:selected{
                background: ##21273C;
                border:none;
            }
        ''')

        lay = QHBoxLayout()
        lay.addWidget(self.listWidget)
        self.setLayout(lay)

        ## item1
        listItem1 = QListWidgetItem(self.listWidget)
        self.listWidget.addItem(listItem1)
        widget1 = CustomItemWidget('模型设置')
        listItem1.setSizeHint(QSize(100, 60))
        self.listWidget.setItemWidget(listItem1, widget1)

        ## item2
        listItem2 = QListWidgetItem(self.listWidget)
        self.listWidget.addItem(listItem2)
        widget2 = CustomItemWidget('推理参数')
        listItem2.setSizeHint(QSize(100, 60))  ## 设置原始item的尺寸，否则自定义的widget可能显示不全
        self.listWidget.setItemWidget(listItem2, widget2)

        self.listWidget.setCurrentItem(listItem1)

        self.listWidget.currentItemChanged.connect(self.selectItem)

    def selectItem(self, currentItem: QListWidgetItem, previousItem: QListWidgetItem):
        ## currentItem.setBackground(QtGui.QColor('#21273C'))
        ## if previousItem is not None:
        ##     previousItem.setBackground(QtGui.QColor('#2C344B'))
        print('当前选中：{}'.format(self.listWidget.currentRow()))


if __name__ == '__main__':
    ## 自适应高分辨率屏幕（注意放在QApplication创建之前）
    QtCore.QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)  ## 适应windows缩放
    QtGui.QGuiApplication.setAttribute(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)  ## 设置支持小数放大比例（适应如125%的缩放比）
    app = QApplication(sys.argv)
    widgetWindow = CustomListWidget()
    widgetWindow.show()
    sys.exit(app.exec_())

```





- 

## 其他功能&操作

### 替换QtDesigner创建的控件&保持已绑定的事件处理方法仍然有效

### 1、继承QLabel，增加点击事件（以重写QLabel增加点击事件为例）

```python
class QLabelUser(QLabel):
    signal_clicked = pyqtSignal()

    def __init__(self, text=''):
        super(QLabelUser, self).__init__()
        self.setText(text)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
        self.setFont(font)
        self.setStyleSheet("font-family: \"Microsoft YaHei\";\n"
                           "font-weight: 500;\n"
                           "font-size: 16px;\n"
                           "line-height: 14px;\n"
                           "text-align: left;\n"
                           "color: ##fff;")
        self.setAlignment(Qt.AlignCenter)
        self.setObjectName("label_user")
        self.setCursor(QCursor(Qt.ArrowCursor))

    def mousePressEvent(self, ev):
        self.signal_clicked.emit()
        print('信号发送')
```

### 2、替换控件

```python
## 替换欢迎信息的label，增加点击事件
## 创建新的控件
self.label_user = QLabelUser('欢迎使用')
self.label_user.setParent(self.ui.widget_welcome)
self.label_user.signal_clicked.connect(self.show_auth_win)

## self.ui.label_user = self.label_user  ## 替换布局的widget与直接覆盖原始ui的控件的效果不完全一样
lay1 = self.ui.widget_welcome.layout()
widget_label_user = lay1.itemAt(0).widget()  ## 获取原始控件（指向self.ui.label_user）
widget_label_user = self.label_user  ## 替换控件（勿删）【此方法替换后，self.ui.label_user绑定的事件仍然有效】
```



### 设置鼠标手势

```python
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt

self.ui.btn.setCursor(QCursor(Qt.PointingHandCursor))  ## 鼠标在某个控件上的样式
self.setCursor(QCursor(Qt.ArrowCursor))  ## 界面全局的鼠标样式

'''
常用手势：
textToCursorShape = {
            u'正常': Qt.ArrowCursor,  ## 正常样式
            u'后台运行': Qt.BusyCursor,
            u'等待': Qt.WaitCursor,
            u'精准十字': Qt.CrossCursor,
            u'禁止': Qt.ForbiddenCursor,     
            u'食指手型': Qt.PointingHandCursor,  ## 点击样式
            u'打开手型': Qt.OpenHandCursor,  ## 拖拽样式
            u'关闭手型': Qt.ClosedHandCursor,
            u'水平调整': Qt.SizeHorCursor,
            u'垂直调整': Qt.SizeVerCursor,
            u'沿对角线调整1': Qt.SizeFDiagCursor,
            u'沿对角线调整2': Qt.SizeBDiagCursor,
            u'候选上箭头': Qt.UpArrowCursor,
            u'移动': Qt.SizeAllCursor,
            u'文本选择': Qt.IBeamCursor,
            u'帮助选择': Qt.WhatsThisCursor,
            u'水平分割': Qt.SplitHCursor,
            u'垂直分割': Qt.SplitVCursor,
            u'空': Qt.BlankCursor,
            u'自定义': custonCursor
        }
'''
```



## Qt样式设置

- 样式美化见：[QSS万能样式模板.md](QSS万能样式模板.md)

### 1.通过窗口对象设置样式

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

        ## 设置样式
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

### 2.使用QSS选择器设置控件样式

```python
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QApplication
import sys


class QSSSelector(QWidget):
    def __init__(self):
        super(QSSSelector, self).__init__()

        btn1 = QPushButton(self)
        btn1.setText('按钮1')
        btn1.setProperty('name', 'btn1')  ## 为控件设置属性
        btn2 = QPushButton(self)
        btn2.setText('按钮2')
        btn3 = QPushButton(self)
        btn3.setText('按钮3')

        lay = QVBoxLayout()
        lay.addWidget(btn1)
        lay.addWidget(btn2)
        lay.addWidget(btn3)

        self.setLayout(lay)

        ## 设置样式
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

### 3.子控件选择器

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

        ## 设置样式【#号相当于id；::后为子控件】
        qssStyle = '''
            QComboBox##myComboBox::drop-down{
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



### 4.窗口样式

```python
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class WindowPattern(QMainWindow):
    def __init__(self):
        super(WindowPattern, self).__init__()
        self.resize(500, 260)
        self.setWindowTitle('设置窗口的样式')

        ## self.setWindowFlags(Qt.WindowMaximizeButtonHint | Qt.WindowStaysOnTopHint|Qt.FramelessWindowHint)
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMaximizeButtonHint|Qt.WindowMinimizeButtonHint)
        self.setObjectName('MainWindow')
        self.setStyleSheet("#MainWindow{border-image:url(背景.jpg);}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = WindowPattern()
    win.show()
    sys.exit(app.exec_())

```



### 5.为标签和按钮添加背景图

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
            ##btn1{
                background-image:url('添加.png');
            }
            ##btn1:Pressed{
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



### 6.缩放图片

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

        ## img_scaled = img.scaled(label1.width(), label1.height(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
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



### 7.窗口透明效果

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





















