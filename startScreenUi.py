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
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.page_1.sizePolicy().hasHeightForWidth())
        self.page_1.setSizePolicy(sizePolicy1)
        self.page_1.setMinimumSize(QSize(800, 600))
        self.page_1.setMouseTracking(False)
        self.page_1.setAutoFillBackground(False)
        self.horizontalLayout = QHBoxLayout(self.page_1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 12, -1)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.teacher_button = QPushButton(self.page_1)
        self.teacher_button.setObjectName(u"teacher_button")
        self.teacher_button.setMinimumSize(QSize(320, 160))
        self.teacher_button.setMaximumSize(QSize(16777215, 200))
        self.teacher_button.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.980296, y2:0.972, stop:0 rgba(33, 33, 33, 255), stop:1 rgba(93, 82, 120, 255));\n"
"border-color: rgb(13, 3, 16);\n"
"color: white")

        self.horizontalLayout.addWidget(self.teacher_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.student_button = QPushButton(self.page_1)
        self.student_button.setObjectName(u"student_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.student_button.sizePolicy().hasHeightForWidth())
        self.student_button.setSizePolicy(sizePolicy2)
        self.student_button.setMinimumSize(QSize(320, 160))
        self.student_button.setMaximumSize(QSize(16777215, 200))
        self.student_button.setBaseSize(QSize(320, 160))
        self.student_button.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.980296, y2:0.972, stop:0 rgba(33, 33, 33, 255), stop:1 rgba(93, 82, 120, 255));\n"
"color: white")

        self.horizontalLayout.addWidget(self.student_button)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        StackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout = QGridLayout(self.page_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(self.page_2)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(400, 260))
        self.widget.setStyleSheet(u"background-color: rgb(48, 48, 48);")
        self.name_label = QLabel(self.widget)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setGeometry(QRect(100, 40, 201, 31))
        self.name_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.textEdit_name = QTextEdit(self.widget)
        self.textEdit_name.setObjectName(u"textEdit_name")
        self.textEdit_name.setGeometry(QRect(100, 70, 200, 30))
        font = QFont()
        font.setFamilies([u"Impact"])
        font.setPointSize(15)
        self.textEdit_name.setFont(font)
        self.textEdit_name.setStyleSheet(u"background-color: rgb(97, 97, 97);\n"
"color: rgb(255, 255, 255);")
        self.textEdit_name.setPlaceholderText(u"")
        self.connection_label = QLabel(self.widget)
        self.connection_label.setObjectName(u"connection_label")
        self.connection_label.setGeometry(QRect(100, 130, 201, 31))
        self.connection_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.textEdit_conn = QTextEdit(self.widget)
        self.textEdit_conn.setObjectName(u"textEdit_conn")
        self.textEdit_conn.setGeometry(QRect(100, 160, 200, 30))
        self.textEdit_conn.setFont(font)
        self.textEdit_conn.setStyleSheet(u"background-color: rgb(97, 97, 97);\n"
"color: rgb(255, 255, 255);")
        self.submit_button = QPushButton(self.widget)
        self.submit_button.setObjectName(u"submit_button")
        self.submit_button.setGeometry(QRect(140, 210, 113, 32))
        self.submit_button.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(70, 70, 70);")
        self.back_button = QPushButton(self.widget)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setGeometry(QRect(10, 10, 70, 20))
        font1 = QFont()
        font1.setPointSize(11)
        self.back_button.setFont(font1)
        self.back_button.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(70, 70, 70);")
        self.name_descriptor = QLabel(self.widget)
        self.name_descriptor.setObjectName(u"name_descriptor")
        self.name_descriptor.setGeometry(QRect(100, 100, 201, 31))
        font2 = QFont()
        font2.setPointSize(9)
        self.name_descriptor.setFont(font2)
        self.name_descriptor.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        StackedWidget.addWidget(self.page_2)

        self.retranslateUi(StackedWidget)

        StackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(StackedWidget)
    # setupUi

    def retranslateUi(self, StackedWidget):
        StackedWidget.setWindowTitle(QCoreApplication.translate("StackedWidget", u"StackedWidget", None))
        self.teacher_button.setText(QCoreApplication.translate("StackedWidget", u"I am a teacher", None))
        self.student_button.setText(QCoreApplication.translate("StackedWidget", u"I am a student", None))
        self.name_label.setText(QCoreApplication.translate("StackedWidget", u"Name:", None))
        self.connection_label.setText(QCoreApplication.translate("StackedWidget", u"Connection ID:", None))
        self.submit_button.setText(QCoreApplication.translate("StackedWidget", u"Submit", None))
        self.back_button.setText(QCoreApplication.translate("StackedWidget", u"< Back", None))
        self.name_descriptor.setText(QCoreApplication.translate("StackedWidget", u"Must insclude only latin letters and be\n"
"between 2 and 25 characters", None))
    # retranslateUi

