## QSS万能样式模板

- Date: 2022/04/15
- Author: 浅若清风cyf



## 参考资料

- [QSS总结以及最近做的Qt项目 - 薰衣草的旋律 - 博客园 (cnblogs.com)](https://www.cnblogs.com/wangqiguo/p/4960776.html)

## 一、选择器规则

- QSS的语法规则几乎与CSS相同。一条QSS的样式是由两部分组成的，一部分是选择器指定了哪些控件会受到影响，另一部分是指定了属性的值，表示这些控件的哪些属性会受到影响。

| 选择器 类型 | 示例                      | 说明                                                         | 推荐 | 说明                                                         |
| ----------- | ------------------------- | ------------------------------------------------------------ | ---- | ------------------------------------------------------------ |
| ID选择器    | \#myBtn                   | 匹配所有id为myButton的控件实例，id为objectName指定的值       | ☆☆☆  |                                                              |
| 类型选择器  | QPushButton               | 匹配所有QPushButton和其<u>子类</u>的实例                     | ☆☆☆  | QWidget选择器会对QWidget、QLabel、QPushButton等同时起作用    |
| 类选择器    | .QPushButton              | 匹配所有QPushButton的实例，但是并不匹配其子类                |      | .QWidget选择器会仅对QWidget起作用，但不会对其子类QLabel、QPushButton等起作用 |
| 后代选择器  | QDialog QPushButton       | 所有QDialog容器中包含的QPushButton，不管是直接的还是间接的   |      |                                                              |
| 子选择器    | QDialog > QPushButton     | 所有QDialog容器下面的QPushButton，其中要求QPushButt样式会对on的<u>直接父容器</u>是QDialog |      |                                                              |
| 属性选择器  | QPushButton[flat="false"] | 匹配所有flat属性是false的QPushButton实例，该属性可以是自定义的属性，不一定非要是类本身具有的属性 | ☆☆☆  |                                                              |
| 通配选择器  | *                         | 匹配所有的控件                                               |      |                                                              |

> 注：上面所有的这些选择器可以联合使用，并且支持一次设置多个选择器类型，用逗号隔开，这点与CSS一样，例如##frameCut,#frameInterrupt,#frameJoin 表示所有这些id使用一个规则。#mytable QPushButton 表示选择所有id为mytable的容器下面的QPushButton实例



> 在不清楚级联和冲突规则情况下，建议优先使用ID选择器（ID的类型不要是QWidget）→ID选择器+类型选择器→后代选择器/子选择器

## 二、QSS级联与冲突

### 1、**背景**

QSS中的级联包含几个方面的概念：

- **冲突问题：**当在<u>同一个控件上</u>应用两个不同的规则，那么应该应用哪一个规则的问题
- **级联问题：**当<u>在多个父容器上对同一个/类型的控件</u>都设置设置样式，即一个控件被层层父容器包裹，并且在每一层的父容器上都有对该控件的样式设置的时候，控件最终是什么效果的问题（该控件的最终效果是合并这些父容器上的QSS效果）

### 2、冲突问题

- 概念
  - 特异性：如同CSS的权重概念
- 总结

| 规则                                         | 示例                                                         | 优先级                |
| -------------------------------------------- | ------------------------------------------------------------ | --------------------- |
| 特异性高者优先<br />（一般选择器、类选择器） | ①QPushButton##okButton { color: gray } <br />②QPushButton { color: red }<br />③QPushButton { color: red } <br />④QAbstractButton { color: gray } <br />⑤QWidget {color: black}<br />⑥QPushButton {color:red} | ①>②<br />③>④<br />⑤<⑥ |
| 特异性相同，后者优先                         | ①QPushButton:hover { color: white } <br />②QPushButton:enabled { color: red } <br />说明：这种设置下，鼠标经过控件是不会切换①的样式，但交换顺序则效果不同 | ①<②                   |
| 伪状态优先                                   | ①QPushButton:hover { color: white } <br />②QPushButton { color: red } | ①>②                   |

### 3、级联问题

- QSS的设置位置：

  - QApplication
  - 一个部件的容器部件
  - 子孙部件

- 级联效果：

  效果叠加，即：合并了他的所有父容器，祖父容器等上面设置的所有样式的结果

- 冲突与解决：

  - 示例：

    ```c++
    qApplication->setStyleSheet("QPushButton { color: white; font-size:14px; }");
    myPushButton->setStyleSheet("* { color: blue }")
    ```

  - 最终效果：

    ```c++
    /*myPushButton的效果等价于如下语句*/
    myPushButton->setStyleSheet("* { color: blue; font-size:14px; }")
    ```

> 在控件上设置样式时，需要注意控件的父子关系，从而影响控件效果的继承。特别是QWidget类型，因为QLabel、QPushButton等常用控件的父类均为QWidget，直接用类型选择器设置QWidget的样式，会对这些控件均产生作用！

## 三、样式模板

- 主要针对子控件的参考，如：QComboBox, QCheckBox

### QWidget

```c++
##widget_Button QPushButton{
	height:54px;
	width:172px;
	font-family: "Microsoft YaHei";
	font-weight: 400;
	font-size: 14px;
	color: ##8e9fc4;
	background-color: ##2c344b;
	border: 3px solid ##2c344b;
	border-left:3px solid ##2c344b;
}
```

### QLabel

```c++
##label{
	font-family: "Microsoft YaHei";
	font-weight: 400;
	font-size: 16px;
	line-height: 14px;
	color: ##ebf6ff;
}
```

### QSpinBox

![image-20220502130217987](/YoferVuePressHome/styles/image-20220502130217987.png)

```c++
QSpinBox{
width: 84px;
height: 40px;
background: ##252b41;
color: ##99a5be;
padding-left:12px;
border:none;
}

QSpinBox::up-arrow
{
background-image:url(:/resources/上箭头.png);
background-repeat: no-repeat;
height: 15px;
margin-left:10px;
margin-top:10px;
}
QSpinBox::down-arrow{
background-image:url(:/resources/下箭头.png);
background-repeat: no-repeat;
height: 15px;
margin-left:10px;
margin-top:10px;
}
QSpinBox::up-button{
border:none;
}
QSpinBox::up-button:hover
{
/*background-image:url(:/resources/上箭头.png);*/
background-repeat: no-repeat;
background:#1f2537;
}
QSpinBox::up-button:pressed{

}
QSpinBox::down-button{
border:none;
}
QSpinBox::down-button:hover
{
/*background-image:url(:/resources/下箭头.png);*/
background:#1f2537;
background-repeat: no-repeat;
}
QSpinBox::down-button:pressed{

}
```



### QPushButton/QToolButton

- 基本样式

```c++
/*正常情况下的样式*/
##widget_Button QPushButton{
	height:54px;
	width:172px;
	font-family: "Microsoft YaHei";
	font-weight: 400;
	font-size: 14px;
	color: ##8e9fc4;
	background-color: ##2c344b;
	border: 3px solid ##2c344b;
	border-left:3px solid ##2c344b;
}

/*鼠标悬浮样式*/
##widget_Button QPushButton:hover{
	border-left:3px solid ##00a4ff;
	color: ##dcefff;
}
```

- 可选中样式

  > 属性中的checkable需要设置为True，选中的按钮需要设置checked为True
  >
  > 可选中状态下绑定的事件为toggled，按钮状态切换时需要重新设定以下样式才能生效！
  >
  > 为避免任意一个按钮都同时可以切换状态，按钮选中后设为不可选状态
  
  ![image-20220427005442315](/YoferVuePressHome/styles/image-20220427005442315.png)

```c++
##widgetTab QPushButton[checked='false']{
width: 390px;
height: 40px;
background: ##323a53;
border:none;
font-family: "Microsoft YaHei";
font-weight: 400;
font-size: 12px;
color: ##8e9fc4;
}
##widgetTab QPushButton[checked='true']{
width: 390px;
height: 40px;
background: ##1e2537;
border:none;
font-family: "Microsoft YaHei Bold";
font-weight: bold;
font-size: 12px;
color: ##4a90e8;
}
```

```python
## 示例代码
class WidgetWindow(QWidget):
    def __init__(self):
        super(WidgetWindow, self).__init__()
        self.ui = Ui_PushButtonChecked()
        self.ui.setupUi(self)


        self.ui.pBtn1.toggled.connect(self.slotBtnToggle1)
        self.ui.pBtn2.toggled.connect(self.slotBtnToggle2)

    def setBtnCheckedStyle(self):
        self.setStyleSheet('''
        QPushButton[checked='false']{
            width: 390px;
            height: 40px;
            background: ##323a53;
            border:none;
            font-family: "Microsoft YaHei";
            font-weight: 400;
            font-size: 12px;
            color: ##8e9fc4;
            }
            QPushButton[checked='true']{
            width: 390px;
            height: 40px;
            background: ##1e2537;
            border:none;
            font-family: "Microsoft YaHei Bold";
            font-weight: bold;
            font-size: 12px;
            color: ##4a90e8;
            }
        ''')

    def slotBtnToggle1(self,state):
        print('btn1:',state)
        if state:
            self.ui.pBtn2.setChecked(False)
            self.ui.pBtn1.setEnabled(False)
        else:
            self.ui.pBtn2.setChecked(True)
            self.ui.pBtn1.setEnabled(True)
        self.setBtnCheckedStyle()  ## 重新设置样式才生效

    def slotBtnToggle2(self,state):
        print('btn2:',state)
        if state:
            self.ui.pBtn1.setChecked(False)
            self.ui.pBtn2.setEnabled(False)
        else:
            self.ui.pBtn1.setCheckable(True)
            self.ui.pBtn2.setEnabled(True)
        self.setBtnCheckedStyle()  ## 重新设置样式才生效


```



### QCheckBox

![image-20220415200857610](/YoferVuePressHome/styles/image-20220415200857610.png)

```c++
/*复选框*/
QCheckBox{
	font-family: "Microsoft YaHei";
	font-weight: 400;
	font-size: 12px;
	line-height: 14px;
	color: ##8e9fc4;
}
/*复选框按钮*/
QCheckBox::indicator{
	width:14px;
	height:14px;
	border-radius: 2px;
	background: ##252b41;
	border: 1px solid rgba(153, 165, 190, 0.3);
}
/*复选框按钮-选中*/
QCheckBox::indicator:checked{
	image:url(:/resources/勾选.png);
}
/*复选框按钮-未选中*/
QCheckBox::indicator:unchecked{
	border-radius: 2px;
	background: ##252b41;
	border: 1px solid rgba(153, 165, 190, 0.3);
}
```

### QRadioBox

![image-20220427203911338](/YoferVuePressHome/styles/image-20220427203911338.png)

```c++
QRadioButton{
	font-family: "Microsoft YaHei";
	font-weight: 400;
	font-size: 14px;
	color:#99A5BE
}
QRadioButton::indicator:checked{
	image:url(:/resources/复选框按钮-选中.png)
}
QRadioButton::indicator:unchecked{
	image:url(:/resources/复选框按钮-未选中.png)
}
```

### QComboBox

![image-20220415200731441](/YoferVuePressHome/styles/image-20220415200731441.png)

> 注：要是列表项样式生效，需要设置`self.ui.comboBox.setView(QListView())`

```c++
/*下拉列表*/
QComboBox{
	height: 40px;
	background: ##252b41;
	font-family: "Microsoft YaHei";
	font-weight: 400;
	font-size: 14px;
    padding-left:12px;
	color: ##99a5be;
	border: 0px;
}
/*下拉列表面板（最外层）*/
QComboBox::drop-down{
	border: 0px;
}
/*下拉箭头*/
QComboBox::down-arrow{
	width:8px;
	padding-right:8px;
	image: url(:/resources/下拉箭头.png);
}
/*注：下方的设置需要在代码中为对象绑定一个QAbstractItemView*/

/*下拉列表面板（自定义样式）*/
QComboBox QAbstractItemView{
	background-color: ##2c344b;
	font-family: "Microsoft YaHei";
	font-weight: 400;
	font-size: 12px;
	color: ##8e9fc4;
	outline:0px;
	padding-left:12px;
	border: 0px;
}
/*下拉列表项-未选中*/
QComboBox QAbstractItemView::item{
	min-height:35px;
}
/*下拉列表项-选中*/
QComboBox QAbstractItemView::item:selected{
	border: 0px;
	color: ##4a90e8;
}
```

### QSlider

![image-20220415200635971](/YoferVuePressHome/styles/image-20220415200635971.png)

```c++
/*整体尺寸*/
QSlider::groove:horizontal {
border: 1px solid ##4A90E8;
background: ##4A90E8;
height: 5px;
border-radius: 3px;
padding-left:-1px;
padding-right:-1px;
}
/*滑过的颜色*/
QSlider::sub-page:horizontal {
background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
    stop:0 ##B1B1B1, stop:1 ##c4c4c4);
background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,
    stop: 0 ##5DCCFF, stop: 1 ##1874CD);
border: 1px solid ##4A708B;
height: 10px;
border-radius: 2px;
}
/*未滑过的颜色*/
QSlider::add-page:horizontal {
background: ##141A2B;
border: 0px solid ##777;
height: 10px;
border-radius: 2px;
}

/*滑块形状颜色*/
QSlider::handle:horizontal 
{
    background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, 
    stop:0.6 rgba(255, 255, 255, 255), stop:0.778409 ##45ADED);

    width: 11px;
    margin-top: -3px;
    margin-bottom: -3px;
    border-radius: 5px;
}

QSlider::handle:horizontal:hover {
    background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.6 ##2A8BDA, 
    stop:0.778409 rgba(255, 255, 255, 255));

    width: 11px;
    margin-top: -3px;
    margin-bottom: -3px;
    border-radius: 5px;
}

QSlider::sub-page:horizontal:disabled {
background: ##00009C;
border-color: ##999;
}

QSlider::add-page:horizontal:disabled {
background: ##eee;
border-color: ##999;
}

QSlider::handle:horizontal:disabled {
background: ##eee;
border: 1px solid ##aaa;
border-radius: 4px;
}

```



### QScrollBar

- 子组件

![image-20220415223707967](/YoferVuePressHome/styles/image-20220415223707967.png)

- 竖向滚动条

  ![image-20220505124634451](/YoferVuePressHome/styles/image-20220505124634451.png)

```c++
/*竖向滚动条*/
QScrollBar:vertical
{
    width:8px;
    background:rgba(0,0,0,0%);
    margin:0px,0px,0px,0px;
    padding-top:9px;  
    padding-bottom:9px;
}
/*滑块*/
QScrollBar::handle:vertical
{
    width:8px;
    /*background:rgba(0,0,0,25%);*/
    background:#99A5BE;
    border-radius:4px;  
    min-height:20;
}
/*滑块-鼠标悬浮*/
QScrollBar::handle:vertical:hover
{
    width:8px;
    background:rgba(0,0,0,50%); 
    border-radius:4px;
    min-height:20;
}
/*下方端点*/
QScrollBar::add-line:vertical 
{
    height:9px;width:8px;
    border-image:url(:/images/a/3.png);
    subcontrol-position:bottom;
}
/*上方端点*/
QScrollBar::sub-line:vertical 
{
    height:9px;width:8px;
    border-image:url(:/images/a/1.png);
    subcontrol-position:top;
}
/*下方端点-鼠标悬浮*/
QScrollBar::add-line:vertical:hover 
{
    height:9px;width:8px;
    border-image:url(:/images/a/4.png);
    subcontrol-position:bottom;
}
/*上方端点-鼠标悬浮*/
QScrollBar::sub-line:vertical:hover
{
    height:9px;width:8px;
    border-image:url(:/images/a/2.png);
    subcontrol-position:top;
}
/*滑块未到达区域*/
QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical 
{
    background:rgba(0,0,0,10%);
    border-radius:4px;
}

```

- 水平滚动条

```cpp
/*水平滚动条*/
QScrollBar:horizontal
{
    height:8px;
    background:rgba(0,0,0,0%);
    margin:0px,0px,0px,0px;
    padding-left:9px;  
    padding-right:9px;
}
/*滑块*/
QScrollBar::handle:horizontal
{
    height:8px;
    /*background:rgba(0,0,0,25%);*/
    background:#99A5BE;
    border-radius:4px;  
    min-width:20;
}
/*滑块-鼠标悬浮*/
QScrollBar::handle:horizontal:hover
{
    height:8px;
    background:rgba(0,0,0,50%); 
    border-radius:4px;
    min-width:20;
}
/*下方端点*/
QScrollBar::add-line:horizontal 
{
    width:9px;height:8px;
    border-image:url(:/images/a/3.png);
    subcontrol-position:right;
}
/*上方端点*/
QScrollBar::sub-line:horizontal 
{
    width:9px;height:8px;
    border-image:url(:/images/a/1.png);
    subcontrol-position:left;
}
/*下方端点-鼠标悬浮*/
QScrollBar::add-line:horizontal:hover 
{
    width:9px;height:8px;
    border-image:url(:/images/a/4.png);
    subcontrol-position:right;
}
/*上方端点-鼠标悬浮*/
QScrollBar::sub-line:horizontal:hover
{
    width:9px;height:8px;
    border-image:url(:/images/a/2.png);
    subcontrol-position:left;
}
/*滑块未到达区域*/
QScrollBar::add-page:horizontal,QScrollBar::sub-page:horizontal 
{
    background:rgba(0,0,0,10%);
    border-radius:4px;
}
```





### QTableWidget

- 参考：

  [QTableWidget的用法总结 - findumars - 博客园 (cnblogs.com)](https://www.cnblogs.com/findumars/p/5553367.html)

  [Qt QTableWidget 样式表_漫步繁华街的博客-CSDN博客_qtablewidget样式表](https://blog.csdn.net/xiezhongyuan07/article/details/79538446)

  [QTableWidget、QTableView样式表参考 - 代码先锋网 (codeleading.com)](https://codeleading.com/article/8937285929/)

- 样式表

```cpp
/*表头*/
QHeaderView                    /* QTableWidget 标题头整个区域*/
{
    background:transparent;        /* 整个标题头区域背景色*/
}
/*表头单元格*/
QHeaderView::section           /* 标题头 每个单独的标题区域*/
{
    font-size:14px; 
    font-family:"Microsoft YaHei"; /* 每个标题的字体类型*/
    color:#FFFFFF;                 /* 每个标题的字体颜色*/
 
    background:#60669B;            /* 每个标题区域的背景色*/
    border:none;                   /* 每个标题区域的边框*/
    text-align:left;               /* 每个标题的对齐方式（貌似不能用）。建议使用tableWidget->horizontalHeader()->setDefaultAlignment(Qt::AlignLeft | Qt::AlignVCenter)*/
 
 
    min-height:49px;               /* 标题区域的高度*/
    max-height:49px;              
 
    margin-left:0px;               /* 每个标题区域的margin*/
    padding-left:0px;              /* 每个标题区域的padding*/
}
/*表格控件*/
QTableWidget
{
    background:#252b41;
    alternate-background-color:#323A53;  /*单元格行之间颜色交替；注：需要设置表格的AlternatingRowColors属性为True才生效*/
    border:none;
    font-family: "Microsoft YaHei";
    font-weight: 400;
    font-size: 14px;
    color: ##99a5be;
}
 /*单元格*/
QTableWidget::item                /* 每个单元格*/
{
    border-bottom:1px solid ##EEF1F7; /* 只显示每个单元格下边框*/
}
/*单元格选中状态*/
QTableWidget::item::selected      /* 每个单元格被选中状态*/
{
    color:red;                        /* 每个单元格被选中时 字体颜色*/
    background:#EFF4FF;               /* 每个单元格被选中时 背景颜色*/
}


```

- 模板

  ![image-20220425112217480](/YoferVuePressHome/styles/image-20220425112217480.png)

  > 包含：水平、竖直滚动条、表格、表头、复选框样式
  >
  > 注：
  >
  > - 由于代码中设置了水平宽度自适应，因此水平滚动条不显示
  > - 隐藏表格单元格之间的边框，需要设置showGrid属性
  > - 单元格交替颜色需要设置AlternatingRowColors属性
  > - 单元格字体居中需要在代码设置tableWidget->horizontalHeader()->setDefaultAlignment(Qt::AlignLeft | Qt::AlignVCenter)
  > - 表头、单元格复选框添加代码见：[PyQt5开发之QTableWidget表头自定义与美化Demo-Python文档类资源-CSDN文库](https://download.csdn.net/download/weixin_44002829/85204211?spm=1001.2014.3001.5501)

```c++
/*表格整体*/
QTableWidget,QTableView{
background:#252b41;
alternate-background-color:#323A53;
border:none;
font-family: "Microsoft YaHei";
font-weight: 400;
font-size: 14px;
color: ##99a5be;
}
/*单元格*/
QTableWidget::item,QTableView::item{
border:none;
}
/*表头*/
QHeaderView{  /*表头整体（无数据）*/
background:#1f2537;
font-family: "Microsoft YaHei";
font-weight: 400;
font-size: 14px;
color: ##8e9fc4;
}
/*表头单元格*/
QHeaderView::section{ /*有数据的表头*/
background:transparent;
}
/*表头拐角*/
QTableCornerButton:section{  /*当包含水平垂直表头时，左上角的小拐角*/
background:#1f2537;
}

/*全局*/
/*复选框*/
QCheckBox{
	font-family: "Microsoft YaHei";
	font-weight: 400;
	font-size: 12px;
	line-height: 14px;
	color: ##8e9fc4;
}
/*复选框按钮*/
QCheckBox::indicator{
	width:14px;
	height:14px;
	border-radius: 2px;
	background: ##252b41;
	border: 1px solid rgba(153, 165, 190, 0.3);
}
/*复选框按钮-选中*/
QCheckBox::indicator:checked{
	image:url(:/resources/勾选.png);
}
/*复选框按钮-未选中*/
QCheckBox::indicator:unchecked{
	border-radius: 2px;
	background: ##252b41;
	border: 1px solid rgba(153, 165, 190, 0.3);
}

/*竖向滚动条*/
QScrollBar:vertical
{
    width:8px;
    background:rgba(0,0,0,0%);
    margin:0px,0px,0px,0px;
    padding-top:9px;  
    padding-bottom:9px;
}
/*滑块*/
QScrollBar::handle:vertical
{
    width:8px;
    background:#99A5BE;
    border-radius:4px;  
    min-height:20px;
}
/*滑块-鼠标悬浮*/
QScrollBar::handle:vertical:hover
{
    width:8px;
    background:rgba(0,0,0,50%); 
    border-radius:4px;
    min-height:20;
}
/*下方端点*/
QScrollBar::add-line:vertical 
{
    height:9px;width:8px;
    border-image:url(:/images/a/3.png);
    subcontrol-position:bottom;
}
/*上方端点*/
QScrollBar::sub-line:vertical 
{
    height:9px;width:8px;
    border-image:url(:/images/a/1.png);
    subcontrol-position:top;
}
/*下方端点-鼠标悬浮*/
QScrollBar::add-line:vertical:hover 
{
    height:9px;width:8px;
    border-image:url(:/images/a/4.png);
    subcontrol-position:bottom;
}
/*上方端点-鼠标悬浮*/
QScrollBar::sub-line:vertical:hover
{
    height:9px;width:8px;
    border-image:url(:/images/a/2.png);
    subcontrol-position:top;
}
/*滑块未到达区域*/
QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical 
{
    background:rgba(0,0,0,10%);
    border-radius:4px;
}

/*水平滚动条*/
QScrollBar:horizontal
{
    height:8px;
    background:rgba(0,0,0,0%);
    margin:0px,0px,0px,0px;
    padding-left:9px;  
    padding-right:9px;
}
/*滑块*/
QScrollBar::handle:horizontal
{
    height:8px;
    background:rgba(0,0,0,25%);
    border-radius:4px;  
    min-width:20;
}
/*滑块-鼠标悬浮*/
QScrollBar::handle:horizontal:hover
{
    height:8px;
    background:rgba(0,0,0,50%); 
    border-radius:4px;
    min-width:20;
}
/*下方端点*/
QScrollBar::add-line:horizontal 
{
    width:9px;height:8px;
    border-image:url(:/images/a/3.png);
    subcontrol-position:right;
}
/*上方端点*/
QScrollBar::sub-line:horizontal 
{
    width:9px;height:8px;
    border-image:url(:/images/a/1.png);
    subcontrol-position:left;
}
/*下方端点-鼠标悬浮*/
QScrollBar::add-line:horizontal:hover 
{
    width:9px;height:8px;
    border-image:url(:/images/a/4.png);
    subcontrol-position:right;
}
/*上方端点-鼠标悬浮*/
QScrollBar::sub-line:horizontal:hover
{
    width:9px;height:8px;
    border-image:url(:/images/a/2.png);
    subcontrol-position:left;
}
/*滑块未到达区域*/
QScrollBar::add-page:horizontal,QScrollBar::sub-page:horizontal 
{
    background:rgba(0,0,0,10%);
    border-radius:4px;
}
```



- 属性

```cpp
//隐藏单元格边框
tableWidget->setShowGrid(False);//显示表格线
//设置单元格高度：
tableWidget->verticalHeader()->setDefaultSectionSize()
//设置表头内容对齐方式
tableWidget->horizontalHeader()->setDefaultAlignment(Qt::AlignLeft | Qt::AlignVCenter);
//设置表头内容样式
QTableWidgetItem *item = tableWidget->horizontalHeaderItem(0); //获得水平方向表头的Item对象  
item->setFont(QFont("Helvetica")); //设置字体  
item->setBackgroundColor(QColor(0,60,10)); //设置单元格背景颜色  
item->setTextColor(QColor(200,111,30)); //设置文字颜色
//设置选择单元格 不出现虚线框（虚框）
tableWidget->setFocusPolicy(Qt::NoFocus);
//设置表格为整行选择
tableWidget->setSelectionBehavior(QAbstractItemView::SelectRows);  //整行选中的方式
//单元格选中模式
tableWidget->setSelectionMode(QAbstractItemView::ExtendedSelection);  //设置为可以选中多个目标
//指定单元格样式设置
QTableWidgetItem *item = new QTableWidgetItem("Apple");
item->setBackgroundColor(QColor(0,60,10));
item->setForeground(QColor('#4A90E8'));
item->setTextColor(QColor(200,111,100));
item->setFont(QFont("Helvetica"));
tableWidget->setItem(0,3,item);
//设置单元格内文字的对齐方式
QTableWidgetItem *item = new QTableWidgetItem("Apple");
item.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
//合并单元格
tableWidget->setSpan(0, 0, 3, 1)  //参数为： 改变单元格的行、列，合并行数、列数
//设置单元格的大小（某行某列）
tableWidget->setColumnWidth(3,200);
tableWidget->setRowHeight(3,60);
//单元格大小与内容自适应
tableWidget->resizeColumnsToContents();
tableWidget->resizeRowsToContents();
//调整表格行宽（主要模式有Stretch和Fixed）【☆☆☆】
tableWidget->horizontalHeader()->setResizeMode(QHeaderView::Stretch);//使列完全填充并平分
tableWidget->verticalHeader()->setResizeMode(QHeaderView::Stretch);//行自适应宽度           
tableWidget->resizeColumnsToContents(); //根据内容调整列宽
tableWidget->resizeColumnToContents(int col);//根据内容自动调整给定列宽
tableWidget->horizontalHeader()->setResizeMode//把给定列设置为给定模式
//添加表头内容
QStringList header;
header<<""<<tr("1")<<tr("2")<<tr("3")<<tr("4)<<tr("5");
tableWidget->setHorizontalHeaderLabels(header);
//清除或删除全部数据
tableWidget->clear();//清除所有可见数据（包括表头），行还在
tableWidget->clearContents();//只清除表中数据，不清除表头内容
tableWidget->setRowCount(0)；//连行也清除掉        
//添加或删除行
tableWidget->setRowCount(row+1);//添加一行
tableWidget->removeRow(row);//清除已有的行列 
//其他属性
int row = tableWidget->rowCount();//获取表格中当前行数
Int row1 = tableWidget->currentItem()->row();//当前选中行
bool focus = tableWidget->isItemSelected(tableWidget->currentItem());//判断是否选中一行
QString proName = tableWidget->item(row, col)->text();//获取某一格内容
setShowGrid(true);//显示表格线
verticalHeader()->setVisible(false);//隐藏左边垂直
QHeaderView *headerView = horizontalHeader();
headerView->setMovable(false);//去除表头的移动
headerView->resizeSection(0,284);//设置第一列宽
headerView->resizeSection(1,127);//设置第二列宽
headerView->setResizeMode(QHeaderView::Fixed);//列表不能移动
headerView->setClickable(false);//不响应鼠标单击
setEditTriggers(QTableWidget::NoEditTriggers);//不能编辑
setSelectionBehavior(QTableWidget::SelectRows);//一次选中一行
setSelectionMode(QAbstractItemView::SingleSelection);//只能单选
/*QScrollBar *scrollBar = horizontalScrollBar();scrollBar->hide();*/
setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);//去掉水平滚动条
setVerticalScrollMode(QAbstractItemView::ScrollPerItem);//垂直滚动条按项移动
setAutoScroll(false);//去掉自动滚动
```

-  向单元格添加数据/控件

```python
## 单元格添加数据，并设置样式
item=QTableWidgetItem(rowData[i])
item.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
self.ui.tableWidget.setItem(rowIndex, columnIndex,item)

```

```cpp
//单元格中添加控件
QComboBox *comBox = new QComboBox();
comBox->addItem("Y");
comBox->addItem("N");
tableWidget->setCellWidget(0,2,comBox); 
```

- 表头添加控件（如全选QCheckBox）

  - 不用重写QHeaderView：[Qt之数据表头增加控件_字母丶数字丶下划线_的博客-CSDN博客_qt表头添加控件](https://blog.csdn.net/zl_95520/article/details/86573671)
  - 重写QHeaderView：[ qtablewidget表头设置控件 - CSDN](https://www.csdn.net/tags/OtDaYg2sMDQzMi1ibG9n.html)
  - 通过其他替换方法实现类似效果：[QTableWidget自定义表头QHeaderView加全选复选框 - 走看看 (zoukankan.com)](http://t.zoukankan.com/bclshuai-p-9800550.html)

- 表格列宽设置

  > 参考：[PyQt5QTableWidget（表单控件）自适应窗口大小、栏位大小调整及布局 - 百度文库 (baidu.com)](https://wenku.baidu.com/view/75e58d723f1ec5da50e2524de518964bce84d245.html)

  ```python
  ## 宽度根据窗口大小平分
  self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) 
  ## 指定第一列根据内容自适应
  self.ui.tableWidget.horizontalHeader().setSectionResizeMode(0,QHeaderView.Fixed)
  ```

- 实现的Demo

  [PyQt5开发之QTableWidget表头自定义与美化Demo-Python文档类资源-CSDN文库](https://download.csdn.net/download/weixin_44002829/85204211?spm=1001.2014.3001.5503)

### QTabWidget

- 隐藏右侧和下方边框：属性documentMode设为True
- 隐藏标签栏：`self.ui.tabWidget.tabBar().setVisible(False)`
- 基本样式

```c++
QTabWidget,#tab1,#tab2{
background: ##2c344b;
border:none;
}
```

###  QScrollArea

- QScrollArea是一种容器，并且其中又嵌了一个QWidget的内部容器（无限长的幕布），外层容器时一个固定大小的窗口，而内部容器可以伸长，当内部容器大于外部容器时，就会出现滚动条。

- 样式设置在它的自身以及子控件QWidget上

```c++
##scrollArea,#scrollAreaWidgetContents{
background: ##262D43;
border:none;
}
```

### QLineEdit



```c++
QLineEdit{
height: 40px;
background: ##252b41;
font-family: "Microsoft YaHei";
font-weight: 400;
font-size: 14px;
color: ##99a5be;
border:none;
padding-left:12px;
}
```



### QListWidget

- 模板

  ![image-20220427181830801](/YoferVuePressHome/styles/image-20220427181830801.png)

  ```c++
              QListWidget{
                  background: ##2c344b;
                  border:none;
                  outline:0px;  /*去除选中item外轮廓虚线*/
              }
              QListWidget::item:selected{
                  background: ##21273C;
                  border:none;
              }
  ```


### QPlainTextEdit

```c++
QPlainTextEdit{
    background: ##252b41;
    border:none
    font-family: "Microsoft YaHei";
    font-weight: 400;
    font-size: 12px;
    color: ##ebf6ff;
}
```



## 四、其他细节

### 渐变色





## 五、拓展：控件功能定制

### QPushButton



## 六、窗口模板（Frameless模式）

### 窗口可缩放

- QWidget版

### 窗口可移动

- QMainWindow版



### QListWidget+QTabWidget窗口布局

- 效果

  > 右侧QTableWidget的QTabBar使用时设置为隐藏即可，通过左侧按钮控制Tab的切换

  ![image-20220427200525010](/YoferVuePressHome/styles/image-20220427200525010.png)

- UI布局代码：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>LeftMenuRightTabWidget</class>
 <widget class="QWidget" name="LeftMenuRightTabWidget">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1105</width>
    <height>560</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>LeftMenuRightTabWidget</string>
  </property>
  <property name="windowIcon">
   <iconset resource="resources.qrc">
    <normaloff>:/resources/logo_52.png</normaloff>:/resources/logo_52.png</iconset>
  </property>
  <property name="styleSheet">
   <string notr="true">/*上方标题*/
##widgetTitle{
height: 44px;
background: ##333b56;
}
##widgetTitle QLabel{
font-family: &quot;Microsoft YaHei&quot;;
font-weight: 400;
font-size: 16px;
line-height: 14px;
color: ##ebf6ff;
}
##widgetTitle QToolButton{
background:transparent;
}
##widgetTitle QToolButton:hover{
background:#252d44;
}
/*下方设置区域*/
##widgetMain{
background:#252d44;
}
/*左侧菜单栏*/
QListWidget{
    background: ##2c344b;
    border:none;
    outline:0px;  /*去除选中item外轮廓虚线*/
}
QListWidget::item:selected{
    background: ##21273C;
    border:none;
}</string>
  </property>
  <layout class="QVBoxLayout" name="verticalLayout">
   <property name="spacing">
    <number>0</number>
   </property>
   <property name="leftMargin">
    <number>0</number>
   </property>
   <property name="topMargin">
    <number>0</number>
   </property>
   <property name="rightMargin">
    <number>0</number>
   </property>
   <property name="bottomMargin">
    <number>0</number>
   </property>
   <item>
    <widget class="QFrame" name="frame">
     <property name="frameShape">
      <enum>QFrame::StyledPanel</enum>
     </property>
     <property name="frameShadow">
      <enum>QFrame::Raised</enum>
     </property>
     <layout class="QVBoxLayout" name="verticalLayout_2">
      <property name="spacing">
       <number>0</number>
      </property>
      <property name="leftMargin">
       <number>0</number>
      </property>
      <property name="topMargin">
       <number>0</number>
      </property>
      <property name="rightMargin">
       <number>0</number>
      </property>
      <property name="bottomMargin">
       <number>0</number>
      </property>
      <item>
       <widget class="QWidget" name="widgetTitle" native="true">
        <property name="sizePolicy">
         <sizepolicy hsizetype="Preferred" vsizetype="Fixed">
          <horstretch>0</horstretch>
          <verstretch>0</verstretch>
         </sizepolicy>
        </property>
        <layout class="QHBoxLayout" name="horizontalLayout">
         <item>
          <widget class="QLabel" name="labelTitle">
           <property name="text">
            <string>模型推理</string>
           </property>
          </widget>
         </item>
         <item>
          <spacer name="horizontalSpacer">
           <property name="orientation">
            <enum>Qt::Horizontal</enum>
           </property>
           <property name="sizeHint" stdset="0">
            <size>
             <width>346</width>
             <height>20</height>
            </size>
           </property>
          </spacer>
         </item>
         <item>
          <widget class="QToolButton" name="tBtnClose">
           <property name="text">
            <string>...</string>
           </property>
           <property name="icon">
            <iconset resource="resources.qrc">
             <normaloff>:/resources/关闭.png</normaloff>:/resources/关闭.png</iconset>
           </property>
          </widget>
         </item>
        </layout>
       </widget>
      </item>
      <item>
       <widget class="QWidget" name="widgetMain" native="true">
        <layout class="QHBoxLayout" name="horizontalLayout_2">
         <property name="spacing">
          <number>0</number>
         </property>
         <property name="leftMargin">
          <number>0</number>
         </property>
         <property name="topMargin">
          <number>0</number>
         </property>
         <property name="rightMargin">
          <number>0</number>
         </property>
         <property name="bottomMargin">
          <number>0</number>
         </property>
         <item>
          <widget class="QListWidget" name="listWidgetMenu">
           <property name="sizePolicy">
            <sizepolicy hsizetype="Fixed" vsizetype="Expanding">
             <horstretch>0</horstretch>
             <verstretch>0</verstretch>
            </sizepolicy>
           </property>
           <property name="minimumSize">
            <size>
             <width>200</width>
             <height>0</height>
            </size>
           </property>
          </widget>
         </item>
         <item>
          <widget class="QTabWidget" name="tabWidget">
           <property name="styleSheet">
            <string notr="true">QTabWidget,#tabModelSetting,#tabReasoningParam{
background: ##262D43;
border:none;
}</string>
           </property>
           <property name="currentIndex">
            <number>0</number>
           </property>
           <property name="documentMode">
            <bool>true</bool>
           </property>
           <widget class="QWidget" name="tabModelSetting">
            <attribute name="title">
             <string>模型设置</string>
            </attribute>
           </widget>
           <widget class="QWidget" name="tabReasoningParam">
            <attribute name="title">
             <string>推理参数</string>
            </attribute>
           </widget>
          </widget>
         </item>
        </layout>
       </widget>
      </item>
     </layout>
    </widget>
   </item>
  </layout>
 </widget>
 <resources>
  <include location="resources.qrc"/>
 </resources>
 <connections/>
</ui>
```

- 实例化代码：

```python
from PyQt5.QtWidgets import *
from PyQt5.Qt import Qt
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QPoint
from common.UITemplate.UI_LeftMenuRightTabWidget import Ui_LeftMenuRightTabWidget
import sys
import wisdom_store.ui.main.resources_qt5


class MenuItem(QWidget):
    def __init__(self, text, icon):
        super(MenuItem, self).__init__()

        lay = QHBoxLayout()
        labelIcon = QLabel()
        labelIcon.setPixmap(QtGui.QPixmap(icon))
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


class LeftMenuRightTabWidget(QWidget):
    def __init__(self):
        super(LeftMenuRightTabWidget, self).__init__()

        ## 初始化窗口
        self.ui = Ui_LeftMenuRightTabWidget()
        self.ui.setupUi(self)
        ## 给combobox加上view，不加不能正常显示combobox样式
        ## self.ui.comboBox_Sort.setView(QListView())
        ## 设置关闭按钮事件
        self.ui.tBtnClose.clicked.connect(self.close)

        ## 设置边框区域宽度，在此宽度内长按鼠标并拖动可实现缩放
        self._padding = 20  ## 可直接设为指定数值，如20
        ## 获取标题栏高度，用于识别可拖拽窗口的区域
        self.titleHeight = self.ui.widgetTitle.height()

        ## 隐藏系统默认框架
        self.setWindowFlags(Qt.FramelessWindowHint)
        ## 设置QFrame的边框，以便在未点击时能够鼠标追踪事件生效
        self.ui.frame.setFrameStyle(QFrame.Panel)

        ## 初始化鼠标状态
        self.initDrag()  ## 设置鼠标跟踪判断默认值

        ## 设置鼠标追踪（QMainWidget需要从子组件依次向父组件设置追踪才能生效，QWidget对self设置即可）
        self.ui.frame.setMouseTracking(True)
        self.setMouseTracking(True)  ## 设置widget鼠标跟踪

        ## 事件绑定
        self.signalConnect()

        ## 控件状态初始化
        self.stateInit()

        self.menuItemModelSetting = self.addMenuItem('模型设置', ":/resources/模型设置.png")
        self.menuItemReasoningParam = self.addMenuItem('推理参数', ":/resources/推理参数.png")

    def signalConnect(self):
        '''
        事件绑定（信号与槽绑定）
        :return:
        '''
        ## 左侧按钮控制右侧tab切换
        self.ui.listWidgetMenu.currentRowChanged.connect(self.setCurrentTab)

    def stateInit(self):
        '''
        初始化控件状态（手动设定初始追/根据配置文件设置）
        :return:
        '''
        ## self.ui.tabWidget.tabBar().setVisible(False)

        pass

    def addMenuItem(self, text, icon):
        item = QListWidgetItem()
        self.ui.listWidgetMenu.addItem(item)
        item.setSizeHint(QtCore.QSize(100, 60))
        menuItem = MenuItem(text, icon)
        self.ui.listWidgetMenu.setItemWidget(item, menuItem)
        return menuItem

    def setCurrentTab(self, row):
        self.ui.tabWidget.setCurrentIndex(row)

    '''
        以下重写窗口拖拽事件
    '''

    def initDrag(self):
        ## 设置鼠标跟踪判断扳机默认值
        self._moveDrag = False
        self._cornerDrag = False
        self._bottomDrag = False
        self._rightDrag = False

    def resizeEvent(self, QResizeEvent):
        ## 重新调整边界范围以备实现鼠标拖放缩放窗口大小，采用三个列表生成式生成三个列表
        self._rightRect = [QPoint(x, y) for x in range(self.width() - self._padding, self.width() + 1)
                           for y in range(1, self.height() - self._padding)]
        self._bottomRect = [QPoint(x, y) for x in range(1, self.width() - self._padding)
                            for y in range(self.height() - self._padding, self.height() + 1)]
        self._cornerRect = [QPoint(x, y) for x in range(self.width() - self._padding, self.width() + 1)
                            for y in range(self.height() - self._padding, self.height() + 1)]

    def mousePressEvent(self, event):
        ## 重写鼠标点击的事件
        if (event.button() == Qt.LeftButton) and (event.pos() in self._cornerRect):
            ## 鼠标左键点击右下角边界区域
            self._cornerDrag = True
            event.accept()
        elif (event.button() == Qt.LeftButton) and (event.pos() in self._rightRect):
            ## 鼠标左键点击右侧边界区域
            self._rightDrag = True
            event.accept()
        elif (event.button() == Qt.LeftButton) and (event.pos() in self._bottomRect):
            ## 鼠标左键点击下侧边界区域
            self._bottomDrag = True
            event.accept()
        elif (event.button() == Qt.LeftButton) and (event.y() < self.titleHeight):
            ## 鼠标左键点击标题栏区域
            self._moveDrag = True
            self.moveDragPosition = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        print(QMouseEvent.x(), ',', QMouseEvent.y())
        ## 判断鼠标位置切换鼠标手势
        if QMouseEvent.pos() in self._cornerRect:
            self.setCursor(Qt.SizeFDiagCursor)
        elif QMouseEvent.pos() in self._bottomRect:
            self.setCursor(Qt.SizeVerCursor)
        elif QMouseEvent.pos() in self._rightRect:
            self.setCursor(Qt.SizeHorCursor)
        else:
            self.setCursor(Qt.ArrowCursor)
        ## 当鼠标左键点击不放及满足点击区域的要求后，分别实现不同的窗口调整
        ## 没有定义左方和上方相关的5个方向，主要是因为实现起来不难，但是效果很差，拖放的时候窗口闪烁，再研究研究是否有更好的实现
        if Qt.LeftButton and self._rightDrag:
            ## 右侧调整窗口宽度
            self.resize(QMouseEvent.pos().x(), self.height())
            QMouseEvent.accept()
        elif Qt.LeftButton and self._bottomDrag:
            ## 下侧调整窗口高度
            self.resize(self.width(), QMouseEvent.pos().y())
            QMouseEvent.accept()
        elif Qt.LeftButton and self._cornerDrag:
            ## 右下角同时调整高度和宽度
            self.resize(QMouseEvent.pos().x(), QMouseEvent.pos().y())
            QMouseEvent.accept()
        elif Qt.LeftButton and self._moveDrag:
            ## 标题栏拖放窗口位置
            self.move(QMouseEvent.globalPos() - self.moveDragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        ## 鼠标释放后，各扳机复位
        self.initDrag()


if __name__ == '__main__':
    ## 自适应高分辨率屏幕（注意放在QApplication创建之前）
    QtCore.QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)  ## 适应windows缩放
    QtGui.QGuiApplication.setAttribute(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)  ## 设置支持小数放大比例（适应如125%的缩放比）
    app = QApplication(sys.argv)
    myWin = LeftMenuRightTabWidget()
    myWin.show()
    sys.exit(app.exec_())

```







