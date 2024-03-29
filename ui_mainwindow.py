# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QStackedWidget, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.03, y1:0.063, x2:0.921182, y2:1, stop:0.0935961 rgba(24, 108, 128, 255), stop:1 rgba(255, 184, 127, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(800, 600))
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setGeometry(QRect(0, 0, 800, 600))
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        sizePolicy.setHeightForWidth(self.page.sizePolicy().hasHeightForWidth())
        self.page.setSizePolicy(sizePolicy)
        self.teacher_button = QPushButton(self.page)
        self.teacher_button.setObjectName(u"teacher_button")
        self.teacher_button.setGeometry(QRect(60, 200, 320, 160))
        self.teacher_button.setCursor(QCursor(Qt.OpenHandCursor))
        self.teacher_button.setMouseTracking(False)
        self.teacher_button.setFocusPolicy(Qt.ClickFocus)
        self.teacher_button.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.980296, y2:0.972, stop:0 rgba(33, 33, 33, 255), stop:1 rgba(93, 82, 120, 255));\n"
"border-color: rgb(13, 3, 16);\n"
"color: white")
        self.student_button = QPushButton(self.page)
        self.student_button.setObjectName(u"student_button")
        self.student_button.setGeometry(QRect(420, 200, 320, 160))
        self.student_button.setCursor(QCursor(Qt.OpenHandCursor))
        self.student_button.setFocusPolicy(Qt.ClickFocus)
        self.student_button.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.980296, y2:0.972, stop:0 rgba(33, 33, 33, 255), stop:1 rgba(93, 82, 120, 255));\n"
"color: white")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        sizePolicy.setHeightForWidth(self.page_2.sizePolicy().hasHeightForWidth())
        self.page_2.setSizePolicy(sizePolicy)
        self.widget = QWidget(self.page_2)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 800, 600))
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 69, 94, 255), stop:1 rgba(92, 147, 170, 255));")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(200, 150, 400, 260))
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setStyleSheet(u"background-color: rgb(48, 48, 48);")
        self.textEdit = QTextEdit(self.widget_2)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(100, 70, 200, 30))
        font = QFont()
        font.setFamilies([u"Impact"])
        font.setPointSize(15)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet(u"background-color: rgb(97, 97, 97);\n"
"color: rgb(255, 255, 255);")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 40, 201, 31))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 130, 201, 31))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.textEdit_2 = QTextEdit(self.widget_2)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(100, 160, 200, 30))
        self.textEdit_2.setFont(font)
        self.textEdit_2.setStyleSheet(u"background-color: rgb(97, 97, 97);\n"
"color: rgb(255, 255, 255);")
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.teacher_button.setText(QCoreApplication.translate("MainWindow", u"I am a teacher", None))
        self.student_button.setText(QCoreApplication.translate("MainWindow", u"I am a student", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Connection ID:", None))
    # retranslateUi