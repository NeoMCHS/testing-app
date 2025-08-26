# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sessionActive.ui'
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

class Ui_sessionActive(object):
    def setupUi(self, sessionActive):
        if not sessionActive.objectName():
            sessionActive.setObjectName(u"sessionActive")
        sessionActive.resize(500, 100)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(sessionActive.sizePolicy().hasHeightForWidth())
        sessionActive.setSizePolicy(sizePolicy)
        sessionActive.setMinimumSize(QSize(500, 100))
        sessionActive.setMaximumSize(QSize(16777215, 100))
        sessionActive.setStyleSheet(u"background-color: rgb(70, 70, 70);\n"
"border-color: rgb(192, 192, 192);")
        self.horizontalLayout = QHBoxLayout(sessionActive)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(sessionActive)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(30, 16777215))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.label_2)

        self.test_title = QLabel(sessionActive)
        self.test_title.setObjectName(u"test_title")
        self.test_title.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.test_title)

        self.label = QLabel(sessionActive)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(32, 16777215))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.label)

        self.tester_username = QLabel(sessionActive)
        self.tester_username.setObjectName(u"tester_username")
        self.tester_username.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.tester_username)

        self.session_join_button = QPushButton(sessionActive)
        self.session_join_button.setObjectName(u"session_join_button")
        self.session_join_button.setMinimumSize(QSize(100, 35))
        self.session_join_button.setMaximumSize(QSize(150, 35))
        self.session_join_button.setStyleSheet(u"background-color: rgb(86, 73, 255); color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.session_join_button)


        self.retranslateUi(sessionActive)

        QMetaObject.connectSlotsByName(sessionActive)
    # setupUi

    def retranslateUi(self, sessionActive):
        sessionActive.setWindowTitle(QCoreApplication.translate("sessionActive", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("sessionActive", u"Test:", None))
        self.test_title.setText(QCoreApplication.translate("sessionActive", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("sessionActive", u"Host:", None))
        self.tester_username.setText(QCoreApplication.translate("sessionActive", u"TextLabel", None))
        self.session_join_button.setText(QCoreApplication.translate("sessionActive", u"Join", None))
    # retranslateUi

