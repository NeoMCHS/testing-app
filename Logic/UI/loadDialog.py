# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loadDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLayout, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(500, 400)
        Dialog.setMaximumSize(QSize(500, 400))
        Dialog.setStyleSheet(u"background-color: rgb(70, 70, 70);\n"
"border-color: rgb(192, 192, 192);")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.filenames = QScrollArea(Dialog)
        self.filenames.setObjectName(u"filenames")
        self.filenames.setStyleSheet(u"border-color: rgb(255, 255, 255);")
        self.filenames.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.filenames.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.filenames.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 458, 374))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.file_layout = QVBoxLayout()
        self.file_layout.setSpacing(0)
        self.file_layout.setObjectName(u"file_layout")
        self.file_layout.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.file_layout.addItem(self.verticalSpacer)


        self.verticalLayout_3.addLayout(self.file_layout)

        self.filenames.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.filenames)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
    # retranslateUi

