# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sessionInactiveHistory.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(500, 100)
        Form.setMinimumSize(QSize(500, 100))
        Form.setMaximumSize(QSize(16777215, 100))
        Form.setStyleSheet(u"background-color: rgb(70, 70, 70);\n"
"border-color: rgb(192, 192, 192);")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(30, 16777215))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.label_2)

        self.test_title = QLabel(Form)
        self.test_title.setObjectName(u"test_title")
        self.test_title.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.test_title)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(32, 16777215))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.label)

        self.date_started_hosting = QLabel(Form)
        self.date_started_hosting.setObjectName(u"date_started_hosting")
        self.date_started_hosting.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.date_started_hosting)

        self.session_show_responses_button = QPushButton(Form)
        self.session_show_responses_button.setObjectName(u"session_show_responses_button")
        self.session_show_responses_button.setMinimumSize(QSize(100, 35))
        self.session_show_responses_button.setMaximumSize(QSize(150, 35))
        self.session_show_responses_button.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.session_show_responses_button)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Test:", None))
        self.test_title.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("Form", u"Date:", None))
        self.date_started_hosting.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.session_show_responses_button.setText(QCoreApplication.translate("Form", u"Show responses", None))
    # retranslateUi

