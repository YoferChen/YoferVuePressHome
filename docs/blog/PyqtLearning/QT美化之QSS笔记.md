# QT美化之QSS笔记

- Author: 浅若清风cyf

[toc]



# 官方文档

- [PyQt5 Reference Guide — PyQt v5.15 Reference Guide (riverbankcomputing.com)](https://www.riverbankcomputing.com/static/Docs/PyQt5/index.html)
- [Qt 5.15](https://doc.qt.io/qt-5/index.html)

# 参考资料

- [QSS - 简书 (jianshu.com)](https://www.jianshu.com/p/2c7db2f6c458)
- [QSS总结以及最近做的Qt项目 - 薰衣草的旋律 - 博客园 (cnblogs.com)](https://www.cnblogs.com/wangqiguo/p/4960776.html#_label0)
- （☆☆☆）[Qt Style Sheets Reference | Qt Widgets 5.15.8](https://doc.qt.io/qt-5/stylesheet-reference.html)

# 一、QSS选择器

| 选择器类型 | 举例                      | 说明                                                         |
| ---------- | ------------------------- | ------------------------------------------------------------ |
| 通配选择器 | *                         | 匹配所有控件                                                 |
| 类型选择器 | QPushButton               | 匹配所有QPushButton和其子类的对象                            |
| 属性选择器 | QPushButton[flat="flase"] | 匹配所有属性flat的值为flase的QPushButton类型对象             |
| 类选择器   | .QPushButton              | 匹配所有QPushButton的对象,但是不匹配其子类的对象             |
| ID选择器   | #myBtn                    | 匹配所有ID为`myBtn`的控件对象,此ID为对象的objectName属性     |
| 后代选择器 | QDialog QPushButton       | 所有QDialog容器中包含QPushButton类型的对象,不管直接或间接包含 |
| 子选择器   | QDialog > QPushButton     | 所有QDialog容器下所有QPushButton对象,必须是直接包含          |



# 二、QSS属性设置

> 官方文档：
>
> - 样式表属性：[List of Properties](https://doc.qt.io/qt-5/stylesheet-reference.html#list-of-properties)
> - 样式表属性可选值：[List of Property Types](https://doc.qt.io/qt-5/stylesheet-reference.html#list-of-property-types)

在QSS中设置的属性分为两种:

- 样式表的属性, 如border、border-radius、background-color等属性
- QObject系统的属性（QtDesigner中的属性/对象属性），如QLabel::alignment、QLabel::text、QLabel::wordWrap等属性，即在QObject框架中使用“Q_PROPERTY”申明的属性。

>  **注：**
>
> - 设置QOjbect属性时，需要在属性名前面加上"qproperty-"。比如要设置QLabel::alignment属性时在QSS中需要写成`qproperty-alignment`
> - 如果属性有多个值组成，需要将这个值用单引号和双引号括起来

以下是使用QSS属性和QObject属性的示例。



```css
QLabel {
  border-radius: 3px;
  background-color: white;
  qproperty-alignment: AlignCenter; /*或者是 "AlignHCenter|AlignVCenter"*/
  qproperty-text:'This is a Text Mesage';
}
```

# 三、子控件（::）

> 官方文档：
>
> - [List of Sub-Controls](https://doc.qt.io/qt-5/stylesheet-reference.html#list-of-sub-controls)

- 示例：下拉列表控件未展开状态下右侧的图标：``QComboBox::drop-down { image: url(dropdown.png) }``
- 翻译版本：

|  **Sub-Control**   |                       **Description**                        |
| :----------------: | :----------------------------------------------------------: |
|    `::add-line`    | 用于添加 [QScrollBar](https://doc.qt.io/qt-5/qscrollbar.html) 行的按钮。 |
|    `::add-page`    | 控点（滑块）和 [QScrollBar](https://doc.qt.io/qt-5/qscrollbar.html) [的附加行](https://doc.qt.io/qt-5/stylesheet-reference.html#add-line-sub)之间的区域。 |
|     `::branch`     | [QTreeView](https://doc.qt.io/qt-5/qtreeview.html) 的分支指标。 |
|     `::chunk`      | [QProgressBar](https://doc.qt.io/qt-5/qprogressbar.html) 的进度块。 |
|  `::close-button`  | [QDockWidget](https://doc.qt.io/qt-5/qdockwidget.html) 的关闭按钮或 [QTabBar](https://doc.qt.io/qt-5/qtabbar.html) 的选项卡 |
|     `::corner`     | [QAbstractScrollArea](https://doc.qt.io/qt-5/qabstractscrollarea.html) 中两个滚动条之间的角 |
|   `::down-arrow`   | [QComboBox](https://doc.qt.io/qt-5/qcombobox.html)、[QHeaderView](https://doc.qt.io/qt-5/qheaderview.html)（排序指示器）、[QScrollBar](https://doc.qt.io/qt-5/qscrollbar.html) 或 [QSpinBox](https://doc.qt.io/qt-5/qspinbox.html) 的下拉箭头。 |
|  `::down-button`   | [QScrollBar](https://doc.qt.io/qt-5/qscrollbar.html) 或 [QSpinBox 的下](https://doc.qt.io/qt-5/qspinbox.html)拉按钮。 |
|   `::drop-down`    | [QComboBox](https://doc.qt.io/qt-5/qcombobox.html) 的下拉按钮。 |
|  `::float-button`  | [QDockWidget](https://doc.qt.io/qt-5/qdockwidget.html)的浮动按钮 |
|     `::groove`     |    [QS滑块](https://doc.qt.io/qt-5/qslider.html)的凹槽。     |
|   `::indicator`    | [QAbstractItemView](https://doc.qt.io/qt-5/qabstractitemview.html)、[QCheckBox](https://doc.qt.io/qt-5/qcheckbox.html)、[QRadioButton](https://doc.qt.io/qt-5/qradiobutton.html)、可检查 [QMenu](https://doc.qt.io/qt-5/qmenu.html) 项或可检查 [QGroupBox](https://doc.qt.io/qt-5/qgroupbox.html) 的指示器。 |
|     `::handle`     | [QScrollBar](https://doc.qt.io/qt-5/qscrollbar.html)、[QSplitter 或 QSlider](https://doc.qt.io/qt-5/qsplitter.html) 的手柄（滑块）。 |
|      `::icon`      | [QAbstractItemView](https://doc.qt.io/qt-5/qabstractitemview.html) 或 [QMenu](https://doc.qt.io/qt-5/qmenu.html) 的图标。 |
|      `::item`      | [QAbstractItemView](https://doc.qt.io/qt-5/qabstractitemview.html)、[QMenuBar](https://doc.qt.io/qt-5/qmenubar.html)、[QMenu](https://doc.qt.io/qt-5/qmenu.html) 或 [QStatusBar](https://doc.qt.io/qt-5/qstatusbar.html) 中的项。 |
|   `::left-arrow`   | [QScrollBar](https://doc.qt.io/qt-5/qscrollbar.html) 的左箭头。 |
|  `::left-corner`   | [QTabWidget](https://doc.qt.io/qt-5/qtabwidget.html) 的左角。例如，此控件可用于控制 [QTabWidget](https://doc.qt.io/qt-5/qtabwidget.html) 中左角小部件的位置。 |
|   `::menu-arrow`   | 带有菜单的 [QToolButton](https://doc.qt.io/qt-5/qtoolbutton.html) 的箭头。 |
|  `::menu-button`   | [QToolButton](https://doc.qt.io/qt-5/qtoolbutton.html) 的菜单按钮。 |
| `::menu-indicator` | [QPushButton](https://doc.qt.io/qt-5/qpushbutton.html) 的菜单指示器。 |
|  `::right-arrow`   | [QMenu](https://doc.qt.io/qt-5/qmenu.html) 或 [QScrollBar](https://doc.qt.io/qt-5/qscrollbar.html) 的右箭头。 |
|      `::pane`      | [QTabWidget](https://doc.qt.io/qt-5/qtabwidget.html) 的窗格（框架）。 |
|  `::right-corner`  | [QTabWidget](https://doc.qt.io/qt-5/qtabwidget.html) 的右上角。例如，此控件可用于控制 [QTabWidget](https://doc.qt.io/qt-5/qtabwidget.html) 中右角小部件的位置。 |
|    `::scroller`    | [QMenu](https://doc.qt.io/qt-5/qmenu.html) 或 [QTabBar](https://doc.qt.io/qt-5/qtabbar.html) 的滚动条。 |
|    `::section`     | [QHeaderView 的一](https://doc.qt.io/qt-5/qheaderview.html)部分。 |
|   `::separator`    | [QMenu](https://doc.qt.io/qt-5/qmenu.html) 或 [QMainWindow](https://doc.qt.io/qt-5/qmainwindow.html) 中的分隔符。 |
|    `::sub-line`    | 用于减去 [QScrollBar](https://doc.qt.io/qt-5/qscrollbar.html) 的一行的按钮。 |
|    `::sub-page`    | 控点（滑块）和 [QScrollBar](https://doc.qt.io/qt-5/qscrollbar.html) [子行](https://doc.qt.io/qt-5/stylesheet-reference.html#sub-line-sub)之间的区域。 |
|      `::tab`       | [QTabBar](https://doc.qt.io/qt-5/qtabbar.html) 或 [QToolBox](https://doc.qt.io/qt-5/qtoolbox.html) 的选项卡。 |
|    `::tab-bar`     | [QTabWidget](https://doc.qt.io/qt-5/qtabwidget.html) 的选项卡栏。此子控件仅用于控制 [QTabWidget](https://doc.qt.io/qt-5/qtabbar.html) 中 [QTabBar](https://doc.qt.io/qt-5/qtabwidget.html) 的位置。使用 [：：tab](https://doc.qt.io/qt-5/stylesheet-reference.html#tab-sub) 子控件设置选项卡的样式。 |
|      `::tear`      | [QTabBar](https://doc.qt.io/qt-5/qtabbar.html) 的撕裂指示器。 |
|    `::tearoff`     |  [QMenu](https://doc.qt.io/qt-5/qmenu.html) 的撕裂指示器。   |
|      `::text`      | [QAbstractItemView](https://doc.qt.io/qt-5/qabstractitemview.html) 的文本。 |
|     `::title`      | [QGroupBox](https://doc.qt.io/qt-5/qgroupbox.html) 或 [QDockWidget](https://doc.qt.io/qt-5/qdockwidget.html) 的标题。 |
|    `::up-arrow`    | [QHeaderView](https://doc.qt.io/qt-5/qheaderview.html)（排序指示器）、[QScrollBar](https://doc.qt.io/qt-5/qscrollbar.html) 或 [QSpinBox 的](https://doc.qt.io/qt-5/qspinbox.html)向上箭头。 |
|   `::up-button`    | [QSpinBox](https://doc.qt.io/qt-5/qspinbox.html)的向上按钮。 |

# 四、伪状态（:）

> 官方文档：
>
> - [List of Pseudo-States](https://doc.qt.io/qt-5/stylesheet-reference.html#list-of-pseudo-states)

- 翻译版本：

|     Pseudo-State     |                       **Description**                        |
| :------------------: | :----------------------------------------------------------: |
|      `:active`       |           当微件驻留在活动窗口中时，将设置此状态。           |
|   `:adjoins-item`    | 当 [QTreeView](https://doc.qt.io/qt-5/qtreeview.html) 的 [：：分支](https://doc.qt.io/qt-5/stylesheet-reference.html#branch-sub)与项目相邻时，将设置此状态。 |
|     `:alternate`     | 当 [QAbstractItemView](https://doc.qt.io/qt-5/qabstractitemview.html)[：：alternatingRowColors（） 设置为 true 时，对于绘制 QAbstractItemView](https://doc.qt.io/qt-5/qabstractitemview.html#alternatingRowColors-prop) 行的每个交替行都设置此状态。 |
|      `:bottom`       | 该项目位于底部。例如，其选项卡位于底部的 [QTabBar](https://doc.qt.io/qt-5/qtabbar.html)。 |
|      `:checked`      | 该项目已选中。例如，[QAbstractButton](https://doc.qt.io/qt-5/qabstractbutton.html) 的[已检查](https://doc.qt.io/qt-5/qabstractbutton.html#checked-prop)状态。 |
|     `:closable`      | 可以关闭这些项目。例如，[QDockWidget](https://doc.qt.io/qt-5/qdockwidget.html) 打开了 [QDockWidget：:DockWidgetClosable](https://doc.qt.io/qt-5/qdockwidget.html#DockWidgetFeature-enum) 功能。 |
|      `:closed`       | 项目处于关闭状态。例如，[QTreeView](https://doc.qt.io/qt-5/qtreeview.html) 中的非展开项 |
|      `:default`      | 该项目是默认项目。例如，[默认](https://doc.qt.io/qt-5/qpushbutton.html#default-prop) [QPushButton](https://doc.qt.io/qt-5/qpushbutton.html) 或 [QMenu](https://doc.qt.io/qt-5/qmenu.html) 中的默认操作。 |
|     `:disabled`      | 该项目已[禁用](https://doc.qt.io/qt-5/qwidget.html#enabled-prop)。 |
|     `:editable`      | [QComboBox](https://doc.qt.io/qt-5/qcombobox.html)是可编辑的。 |
|    `:edit-focus`     | 该项目具有编辑焦点（请参阅 [QStyle：：State_HasEditFocus](https://doc.qt.io/qt-5/qstyle.html#StateFlag-enum)）。此状态仅适用于 Qt 扩展应用程序。 |
|      `:enabled`      | 该项目[已启用](https://doc.qt.io/qt-5/qwidget.html#enabled-prop)。 |
|     `:exclusive`     | 该项是独占项组的一部分。例如，独占 [QAction 组中](https://doc.qt.io/qt-5/qactiongroup.html)的菜单项。 |
|       `:first`       | 该项目是第一个（在列表中）。例如，[QTabBar](https://doc.qt.io/qt-5/qtabbar.html) 中的第一个选项卡。 |
|       `:flat`        | 项目是扁平的。例如，一个[扁平](https://doc.qt.io/qt-5/qpushbutton.html#flat-prop)[的 QPushButton](https://doc.qt.io/qt-5/qpushbutton.html)。 |
|     `:floatable`     | 项目可以浮动。例如，[QDockWidget](https://doc.qt.io/qt-5/qdockwidget.html) 打开了 [QDockWidget：:D ockWidgetFloatable](https://doc.qt.io/qt-5/qdockwidget.html#DockWidgetFeature-enum) 功能。 |
|       `:focus`       | 该项目具有[输入焦点](https://doc.qt.io/qt-5/qwidget.html#focus-prop)。 |
|   `:has-children`    | 该项目具有子项。例如，[QTreeView](https://doc.qt.io/qt-5/qtreeview.html) 中具有子项的项目。 |
|   `:has-siblings`    | 该项目具有同级。例如，[QTreeView](https://doc.qt.io/qt-5/qtreeview.html) 中同级的项目。 |
|    `:horizontal`     |                       项目具有水平方向                       |
|       `:hover`       |                      鼠标悬停在项目上。                      |
|   `:indeterminate`   | 项目具有不确定状态。例如，[QCheckBox](https://doc.qt.io/qt-5/qcheckbox.html) 或 [QRadioButton](https://doc.qt.io/qt-5/qradiobutton.html) [被部分选中](https://doc.qt.io/qt-5/qt.html#CheckState-enum)。 |
|       `:last`        | 该项目是最后一个（在列表中）。例如，[QTabBar](https://doc.qt.io/qt-5/qtabbar.html) 中的最后一个选项卡。 |
|       `:left`        | 项目位于左侧。例如，其选项卡位于左侧的 [QTabBar](https://doc.qt.io/qt-5/qtabbar.html)。 |
|     `:maximized`     | 项目将最大化。例如，最大化的 [QMdiSubWindow](https://doc.qt.io/qt-5/qmdisubwindow.html)。 |
|      `:middle`       | 项目位于中间（在列表中）。例如，不在 [QTabBar](https://doc.qt.io/qt-5/qtabbar.html) 的开头或结尾的选项卡。 |
|     `:minimized`     | 该项目将被最小化。例如，最小化的 [QMdiSubWindow](https://doc.qt.io/qt-5/qmdisubwindow.html)。 |
|      `:movable`      | 项目可以四处移动。例如，[QDockWidget](https://doc.qt.io/qt-5/qdockwidget.html) 打开了 [QDockWidget：:D ockWidgetMovable](https://doc.qt.io/qt-5/qdockwidget.html#DockWidgetFeature-enum) 功能。 |
|     `:no-frame`      | 该项目没有框架。例如，无帧 [QSpinBox](https://doc.qt.io/qt-5/qspinbox.html) 或 [QLineEdit](https://doc.qt.io/qt-5/qlineedit.html)。 |
|   `:non-exclusive`   | 物料是非独占物料组的一部分。例如，非独占 [QAction 组中](https://doc.qt.io/qt-5/qactiongroup.html)的菜单项。 |
|        `:off`        |      对于可以切换的项目，这适用于处于"关闭"状态的项目。      |
|        `:on`         |     对于可以切换的项目，这适用于处于"打开"状态的小部件。     |
|     `:only-one`      | 该项目是唯一的（在列表中）。例如，[QTabBar](https://doc.qt.io/qt-5/qtabbar.html) 中的一个单独选项卡。 |
|       `:open`        | 项目处于打开状态。例如，[QTreeView](https://doc.qt.io/qt-5/qtreeview.html) 中的展开项，或者具有打开菜单的 [QComboBox](https://doc.qt.io/qt-5/qcombobox.html) 或 [QPushButton](https://doc.qt.io/qt-5/qpushbutton.html)。 |
|   `:next-selected`   | 下一项（在列表中）处于选中状态。例如，[QTabBar](https://doc.qt.io/qt-5/qtabbar.html) 的选定选项卡位于此项旁边。 |
|      `:pressed`      |                    正在使用鼠标按下项目。                    |
| `:previous-selected` | 上一项（在列表中）处于选中状态。例如，[QTabBar](https://doc.qt.io/qt-5/qtabbar.html) 中所选选项卡旁边的选项卡。 |
|     `:read-only`     | 该项目被标记为只读或不可编辑。例如，只读 [QLineEdit](https://doc.qt.io/qt-5/qlineedit.html) 或不可编辑的 [QComboBox](https://doc.qt.io/qt-5/qcombobox.html)。 |
|       `:right`       | 项目位于右侧。例如，其选项卡位于右侧的 [QTabBar](https://doc.qt.io/qt-5/qtabbar.html)。 |
|     `:selected`      | 项目已被选中。例如，[QTabBar](https://doc.qt.io/qt-5/qtabbar.html) 中的选定选项卡或 [QMenu](https://doc.qt.io/qt-5/qmenu.html) 中的选定项。 |
|        `:top`        | 项目位于顶部。例如，其选项卡位于顶部的 [QTabBar](https://doc.qt.io/qt-5/qtabbar.html)。 |
|     `:unchecked`     | 该项目[处于未选中状态](https://doc.qt.io/qt-5/qabstractbutton.html#checked-prop)。 |
|     `:vertical`      |                      项目具有垂直方向。                      |
|      `:window`       |               小部件是一个窗口（即顶级小部件）               |

#









