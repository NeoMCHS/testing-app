# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'choiceAnswer.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QPlainTextEdit,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 50)
        Form.setMinimumSize(QSize(0, 50))
        Form.setMaximumSize(QSize(16777215, 50))
        Form.setStyleSheet(u"background-color: rgb(70, 70, 70);\n"
"border-color: rgb(192, 192, 192);")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.is_right = QCheckBox(Form)
        self.is_right.setObjectName(u"is_right")
        self.is_right.setMinimumSize(QSize(0, 20))

        self.horizontalLayout.addWidget(self.is_right)

        self.answer_choice_edit = QPlainTextEdit(Form)
        self.answer_choice_edit.setObjectName(u"answer_choice_edit")
        self.answer_choice_edit.setMinimumSize(QSize(0, 20))
        self.answer_choice_edit.setMaximumSize(QSize(15000000, 30))
        self.answer_choice_edit.setSizeIncrement(QSize(0, 0))
        self.answer_choice_edit.setStyleSheet(u"background-color: rgb(97, 97, 97);")
        self.answer_choice_edit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout.addWidget(self.answer_choice_edit)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.is_right.setText("")
    # retranslateUi

