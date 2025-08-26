# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'questionTextTest.ui'
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
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(700, 600)
        Form.setMinimumSize(QSize(700, 600))
        Form.setStyleSheet(u"background-color: rgb(48, 48, 48);")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.label)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 200))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.question_text = QLabel(self.widget)
        self.question_text.setObjectName(u"question_text")
        self.question_text.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.question_text.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.question_text)


        self.verticalLayout.addWidget(self.widget)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.label_3)

        self.answer_input = QTextEdit(Form)
        self.answer_input.setObjectName(u"answer_input")
        self.answer_input.setMinimumSize(QSize(0, 150))

        self.verticalLayout.addWidget(self.answer_input)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 40))
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(527, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.submit_answer = QPushButton(self.widget_2)
        self.submit_answer.setObjectName(u"submit_answer")
        self.submit_answer.setMinimumSize(QSize(120, 28))
        self.submit_answer.setMaximumSize(QSize(120, 28))
        self.submit_answer.setStyleSheet(u"background-color: rgb(86, 73, 255); color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.submit_answer)


        self.verticalLayout.addWidget(self.widget_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Question:", None))
        self.question_text.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Enter your answer:", None))
        self.submit_answer.setText(QCoreApplication.translate("Form", u"Submit", None))
    # retranslateUi

