# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '04_myFirstWin.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_window(object):
    def setupUi(self, window):
        if not window.objectName():
            window.setObjectName(u"window")
        window.resize(327, 140)
        self.centralwidget = QWidget(window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.btn = QPushButton(self.groupBox)
        self.btn.setObjectName(u"btn")

        self.horizontalLayout.addWidget(self.btn)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 4)
        self.horizontalLayout.setStretch(2, 2)
        self.horizontalLayout.setStretch(3, 4)

        self.verticalLayout.addWidget(self.groupBox)

        window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 327, 23))
        window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(window)
        self.statusbar.setObjectName(u"statusbar")
        window.setStatusBar(self.statusbar)

        self.retranslateUi(window)

        QMetaObject.connectSlotsByName(window)
    # setupUi

    def retranslateUi(self, window):
        window.setWindowTitle(QCoreApplication.translate("window", u"MyFirstWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("window", u"Add Group Box", None))
        self.label.setText(QCoreApplication.translate("window", u"\u8ba1\u6570\u5668\uff1a0", None))
        self.btn.setText(QCoreApplication.translate("window", u"\u70b9\u51fb\u6211\uff0c\u8ba1\u6570\u5668+1", None))
    # retranslateUi

