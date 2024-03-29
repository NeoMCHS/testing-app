# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'startScreenUi.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTextEdit, QWidget)

class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        if not StackedWidget.objectName():
            StackedWidget.setObjectName(u"StackedWidget")
        StackedWidget.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(StackedWidget.sizePolicy().hasHeightForWidth())
        StackedWidget.setSizePolicy(sizePolicy)
        StackedWidget.setMinimumSize(QSize(800, 600))
        StackedWidget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.03, y1:0.063, x2:0.921182, y2:1, stop:0.0935961 rgba(24, 108, 128, 255), stop:1 rgba(255, 184, 127, 255));")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.page.sizePolicy().hasHeightForWidth())
        self.page.setSizePolicy(sizePolicy1)
        self.page.setMinimumSize(QSize(800, 600))
        self.page.setMouseTracking(False)
        self.page.setAutoFillBackground(False)
        self.horizontalLayout = QHBoxLayout(self.page)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 12, -1)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.pushButton = QPushButton(self.page)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(320, 160))
        self.pushButton.setMaximumSize(QSize(16777215, 200))
        self.pushButton.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.980296, y2:0.972, stop:0 rgba(33, 33, 33, 255), stop:1 rgba(93, 82, 120, 255));\n"
"border-color: rgb(13, 3, 16);\n"
"color: white")

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_2 = QPushButton(self.page)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy2)
        self.pushButton_2.setMinimumSize(QSize(320, 160))
        self.pushButton_2.setMaximumSize(QSize(16777215, 200))
        self.pushButton_2.setBaseSize(QSize(320, 160))
        self.pushButton_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.980296, y2:0.972, stop:0 rgba(33, 33, 33, 255), stop:1 rgba(93, 82, 120, 255));\n"
"color: white")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        StackedWidget.addWidget(self.page)
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.gridLayout = QGridLayout(self.page1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(self.page1)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(400, 260))
        self.widget.setStyleSheet(u"background-color: rgb(48, 48, 48);")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 40, 201, 31))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.textEdit = QTextEdit(self.widget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(110, 70, 200, 30))
        font = QFont()
        font.setFamilies([u"Impact"])
        font.setPointSize(15)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet(u"background-color: rgb(97, 97, 97);\n"
"color: rgb(255, 255, 255);")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 130, 201, 31))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.textEdit_2 = QTextEdit(self.widget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(110, 160, 200, 30))
        self.textEdit_2.setFont(font)
        self.textEdit_2.setStyleSheet(u"background-color: rgb(97, 97, 97);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)

        StackedWidget.addWidget(self.page1)

        self.retranslateUi(StackedWidget)

        StackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(StackedWidget)
    # setupUi

    def retranslateUi(self, StackedWidget):
        StackedWidget.setWindowTitle(QCoreApplication.translate("StackedWidget", u"StackedWidget", None))
        self.pushButton.setText(QCoreApplication.translate("StackedWidget", u"I am a teacher", None))
        self.pushButton_2.setText(QCoreApplication.translate("StackedWidget", u"I am a student", None))
        self.label.setText(QCoreApplication.translate("StackedWidget", u"Name:", None))
        self.label_2.setText(QCoreApplication.translate("StackedWidget", u"Connection ID:", None))
    # retranslateUi

