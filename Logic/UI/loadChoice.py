# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loadChoice.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QPushButton, QSizePolicy, QWidget)

class Ui_file_object(object):
    def setupUi(self, file_object):
        if not file_object.objectName():
            file_object.setObjectName(u"file_object")
        file_object.resize(430, 50)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(file_object.sizePolicy().hasHeightForWidth())
        file_object.setSizePolicy(sizePolicy)
        file_object.setMinimumSize(QSize(430, 50))
        file_object.setMaximumSize(QSize(430, 150))
        file_object.setStyleSheet(u"background-color: rgb(48, 48, 48);\n"
"border-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.horizontalLayout = QHBoxLayout(file_object)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
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

        self.delete_button = QPushButton(file_object)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setStyleSheet(u"color: rgb(255, 255, 255);background-color: rgb(255, 0, 0); color: rgb(0, 0, 0);")

        self.horizontalLayout.addWidget(self.delete_button)

        self.confirm_button = QPushButton(file_object)
        self.confirm_button.setObjectName(u"confirm_button")
        self.confirm_button.setStyleSheet(u"background-color: rgb(86, 73, 255); color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.confirm_button)


        self.retranslateUi(file_object)

        QMetaObject.connectSlotsByName(file_object)
    # setupUi

    def retranslateUi(self, file_object):
        file_object.setWindowTitle(QCoreApplication.translate("file_object", u"Form", None))
        self.name.setText(QCoreApplication.translate("file_object", u"TextLabel", None))
        self.delete_button.setText(QCoreApplication.translate("file_object", u"Delete", None))
        self.confirm_button.setText(QCoreApplication.translate("file_object", u"Load", None))
    # retranslateUi

