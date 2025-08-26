# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hostChoice.ui'
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
    QSizePolicy, QSpacerItem, QWidget)

class Ui_file_object(object):
    def setupUi(self, file_object):
        if not file_object.objectName():
            file_object.setObjectName(u"file_object")
        file_object.resize(430, 50)
        file_object.setMinimumSize(QSize(430, 50))
        file_object.setMaximumSize(QSize(430, 150))
        file_object.setStyleSheet(u"background-color: rgb(48, 48, 48);\n"
"border-color: rgb(255, 255, 255);")
        self.horizontalLayout = QHBoxLayout(file_object)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.name = QLabel(file_object)
        self.name.setObjectName(u"name")
        self.name.setStyleSheet(u"background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.name)

        self.widget_2 = QWidget(file_object)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(3, 16777215))
        self.widget_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.widget_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.host_button = QPushButton(file_object)
        self.host_button.setObjectName(u"host_button")
        self.host_button.setStyleSheet(u"background-color: rgb(86, 73, 255); color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.host_button)


        self.retranslateUi(file_object)

        QMetaObject.connectSlotsByName(file_object)
    # setupUi

    def retranslateUi(self, file_object):
        file_object.setWindowTitle(QCoreApplication.translate("file_object", u"Form", None))
        self.name.setText(QCoreApplication.translate("file_object", u"TextLabel", None))
        self.host_button.setText(QCoreApplication.translate("file_object", u"Host", None))
    # retranslateUi

