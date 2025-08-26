# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'choiceAnswerTest.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 60)
        Form.setMinimumSize(QSize(0, 50))
        Form.setMaximumSize(QSize(16777215, 70))
        Form.setStyleSheet(u"background-color: rgb(48, 48, 48);")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.is_chosen = QCheckBox(Form)
        self.is_chosen.setObjectName(u"is_chosen")
        self.is_chosen.setMinimumSize(QSize(0, 0))
        self.is_chosen.setMaximumSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.is_chosen)

        self.answer_text = QLabel(Form)
        self.answer_text.setObjectName(u"answer_text")
        self.answer_text.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.answer_text)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.is_chosen.setText("")
        self.answer_text.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

