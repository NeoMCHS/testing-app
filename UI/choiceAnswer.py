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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QSizePolicy,
    QTextEdit, QWidget)

class Ui_answer_choice(object):
    def setupUi(self, answer_choice):
        if not answer_choice.objectName():
            answer_choice.setObjectName(u"answer_choice")
        answer_choice.resize(400, 50)
        answer_choice.setMinimumSize(QSize(0, 50))
        answer_choice.setMaximumSize(QSize(16777215, 50))
        answer_choice.setStyleSheet(u"background-color: rgb(70, 70, 70);\n"
"border-color: rgb(192, 192, 192);")
        self.horizontalLayout = QHBoxLayout(answer_choice)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.is_right = QCheckBox(answer_choice)
        self.is_right.setObjectName(u"is_right")

        self.horizontalLayout.addWidget(self.is_right)

        self.answer_choice_edit = QTextEdit(answer_choice)
        self.answer_choice_edit.setObjectName(u"answer_choice_edit")
        self.answer_choice_edit.setMinimumSize(QSize(0, 20))
        self.answer_choice_edit.setMaximumSize(QSize(16777215, 30))
        self.answer_choice_edit.setStyleSheet(u"background-color: rgb(97, 97, 97);")

        self.horizontalLayout.addWidget(self.answer_choice_edit)


        self.retranslateUi(answer_choice)

        QMetaObject.connectSlotsByName(answer_choice)
    # setupUi

    def retranslateUi(self, answer_choice):
        answer_choice.setWindowTitle(QCoreApplication.translate("answer_choice", u"Form", None))
        self.is_right.setText("")
    # retranslateUi

