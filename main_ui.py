# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTextEdit, QVBoxLayout, QWidget)

class Ui_main_wandows(object):
    def setupUi(self, main_wandows):
        if not main_wandows.objectName():
            main_wandows.setObjectName(u"main_wandows")
        main_wandows.resize(949, 613)
        self.verticalLayout_2 = QVBoxLayout(main_wandows)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(main_wandows)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(100, 30))
        self.label.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_2.addWidget(self.label)

        self.filepath_line = QLineEdit(main_wandows)
        self.filepath_line.setObjectName(u"filepath_line")
        self.filepath_line.setMinimumSize(QSize(300, 30))
        self.filepath_line.setMaximumSize(QSize(16777215, 30))
        self.filepath_line.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.filepath_line)

        self.os_list = QComboBox(main_wandows)
        self.os_list.addItem("")
        self.os_list.addItem("")
        self.os_list.addItem("")
        self.os_list.setObjectName(u"os_list")
        self.os_list.setMinimumSize(QSize(100, 30))
        self.os_list.setMaximumSize(QSize(100, 30))
        self.os_list.setSizeIncrement(QSize(0, 0))

        self.horizontalLayout_2.addWidget(self.os_list)

        self.start_but = QPushButton(main_wandows)
        self.start_but.setObjectName(u"start_but")
        self.start_but.setMinimumSize(QSize(100, 30))
        self.start_but.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_2.addWidget(self.start_but)

        self.sd_but = QPushButton(main_wandows)
        self.sd_but.setObjectName(u"sd_but")
        self.sd_but.setMinimumSize(QSize(100, 30))
        self.sd_but.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_2.addWidget(self.sd_but)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.pid_input = QLineEdit(main_wandows)
        self.pid_input.setObjectName(u"pid_input")
        self.pid_input.setMinimumSize(QSize(200, 30))
        self.pid_input.setMaximumSize(QSize(200, 30))

        self.horizontalLayout_18.addWidget(self.pid_input)

        self.tiqu_but = QPushButton(main_wandows)
        self.tiqu_but.setObjectName(u"tiqu_but")
        self.tiqu_but.setMinimumSize(QSize(100, 30))
        self.tiqu_but.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_18.addWidget(self.tiqu_but)

        self.mem_but = QPushButton(main_wandows)
        self.mem_but.setObjectName(u"mem_but")
        self.mem_but.setMinimumSize(QSize(100, 30))
        self.mem_but.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_18.addWidget(self.mem_but)

        self.file_dump = QPushButton(main_wandows)
        self.file_dump.setObjectName(u"file_dump")
        self.file_dump.setMinimumSize(QSize(100, 30))
        self.file_dump.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_18.addWidget(self.file_dump)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_18)

        self.tabWidget = QTabWidget(main_wandows)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout = QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.echo = QTextEdit(self.tab)
        self.echo.setObjectName(u"echo")

        self.horizontalLayout.addWidget(self.echo)

        self.tabWidget.addTab(self.tab, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(main_wandows)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(main_wandows)
    # setupUi

    def retranslateUi(self, main_wandows):
        main_wandows.setWindowTitle(QCoreApplication.translate("main_wandows", u"SQM\u7684\u5185\u5b58\u5206\u6790\u5de5\u5177", None))
        self.label.setText(QCoreApplication.translate("main_wandows", u"\u955c\u50cf\u62d6\u62fd\u8f93\u5165", None))
        self.os_list.setItemText(0, QCoreApplication.translate("main_wandows", u"windows", None))
        self.os_list.setItemText(1, QCoreApplication.translate("main_wandows", u"linux", None))
        self.os_list.setItemText(2, QCoreApplication.translate("main_wandows", u"macos", None))

        self.os_list.setCurrentText(QCoreApplication.translate("main_wandows", u"windows", None))
        self.start_but.setText(QCoreApplication.translate("main_wandows", u"\u5f00\u59cb\u5206\u6790", None))
        self.sd_but.setText(QCoreApplication.translate("main_wandows", u"\u624b\u52a8\u5206\u6790", None))
        self.pid_input.setText(QCoreApplication.translate("main_wandows", u"\u8bf7\u8f93\u5165PID", None))
        self.tiqu_but.setText(QCoreApplication.translate("main_wandows", u"\u6587\u4ef6\u63d0\u53d6", None))
        self.mem_but.setText(QCoreApplication.translate("main_wandows", u"\u5185\u5b58\u63d0\u53d6", None))
        self.file_dump.setText(QCoreApplication.translate("main_wandows", u"\u8f6c\u50a8\u5168\u90e8\u6587\u4ef6", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("main_wandows", u"\u8f93\u51fa\u4fe1\u606f", None))
    # retranslateUi

