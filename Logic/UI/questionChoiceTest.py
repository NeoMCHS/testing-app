# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'questionChoiceTest.ui'
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
    QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_choice_form_test(object):
    def setupUi(self, choice_form_test):
        if not choice_form_test.objectName():
            choice_form_test.setObjectName(u"choice_form_test")
        choice_form_test.resize(700, 600)
        choice_form_test.setMinimumSize(QSize(700, 600))
        choice_form_test.setStyleSheet(u"background-color: rgb(48, 48, 48);")
        self.verticalLayout = QVBoxLayout(choice_form_test)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(choice_form_test)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.label_2)

        self.widget = QWidget(choice_form_test)
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

        self.label = QLabel(choice_form_test)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.label)

        self.scrollArea = QScrollArea(choice_form_test)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 674, 266))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.choice_answers_area = QVBoxLayout()
        self.choice_answers_area.setObjectName(u"choice_answers_area")

        self.verticalLayout_4.addLayout(self.choice_answers_area)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.widget_2 = QWidget(choice_form_test)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 40))
        self.widget_2.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.submit_answer = QPushButton(self.widget_2)
        self.submit_answer.setObjectName(u"submit_answer")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(28)
        sizePolicy.setHeightForWidth(self.submit_answer.sizePolicy().hasHeightForWidth())
        self.submit_answer.setSizePolicy(sizePolicy)
        self.submit_answer.setMinimumSize(QSize(120, 28))
        self.submit_answer.setMaximumSize(QSize(120, 28))
        self.submit_answer.setStyleSheet(u"background-color: rgb(86, 73, 255); color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.submit_answer)


        self.verticalLayout.addWidget(self.widget_2)


        self.retranslateUi(choice_form_test)

        QMetaObject.connectSlotsByName(choice_form_test)
    # setupUi

    def retranslateUi(self, choice_form_test):
        choice_form_test.setWindowTitle(QCoreApplication.translate("choice_form_test", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("choice_form_test", u"Question:", None))
        self.question_text.setText(QCoreApplication.translate("choice_form_test", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("choice_form_test", u"Answer choices:", None))
        self.submit_answer.setText(QCoreApplication.translate("choice_form_test", u"Submit", None))
    # retranslateUi

