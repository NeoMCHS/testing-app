# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'questionText.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPlainTextEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(500, 320)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(500, 320))
        Form.setMaximumSize(QSize(1500000, 320))
        Form.setStyleSheet(u"background-color: rgb(70, 70, 70);\n"
"border-color: rgb(192, 192, 192);")
        self.question_area = QVBoxLayout(Form)
        self.question_area.setObjectName(u"question_area")
        self.main_area = QVBoxLayout()
        self.main_area.setObjectName(u"main_area")
        self.question_text_field = QTextEdit(Form)
        self.question_text_field.setObjectName(u"question_text_field")
        self.question_text_field.setMaximumSize(QSize(16777215, 80))
        self.question_text_field.setStyleSheet(u"background-color: rgb(97, 97, 97);")
        self.question_text_field.setLineWidth(0)

        self.main_area.addWidget(self.question_text_field)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(200, 45))
        self.widget_2.setMaximumSize(QSize(0, 45))
        self.widget_2.setStyleSheet(u"background-color: rgb(97, 97, 97);")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 120, 24))
        self.label.setMinimumSize(QSize(120, 24))
        self.label.setMaximumSize(QSize(120, 16777215))
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.total_points = QPlainTextEdit(self.widget_2)
        self.total_points.setObjectName(u"total_points")
        self.total_points.setGeometry(QRect(138, 12, 50, 24))
        self.total_points.setMinimumSize(QSize(50, 24))
        self.total_points.setMaximumSize(QSize(50, 24))
        self.total_points.setStyleSheet(u"background-color: rgb(70, 70, 70);\n"
"color: rgb(255, 255, 255);")
        self.total_points.setLineWidth(0)
        self.total_points.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.total_points.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_2.addWidget(self.widget_2)


        self.main_area.addLayout(self.horizontalLayout_2)

        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(0, 100))
        self.scrollArea.setMaximumSize(QSize(16777215, 100))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 472, 98))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.text_answers = QTextEdit(self.scrollAreaWidgetContents)
        self.text_answers.setObjectName(u"text_answers")
        self.text_answers.setMaximumSize(QSize(16777215, 150))

        self.verticalLayout_4.addWidget(self.text_answers)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.main_area.addWidget(self.scrollArea)


        self.question_area.addLayout(self.main_area)

        self.bottom_bar = QWidget(Form)
        self.bottom_bar.setObjectName(u"bottom_bar")
        self.bottom_bar.setMinimumSize(QSize(0, 30))
        self.horizontalLayout_4 = QHBoxLayout(self.bottom_bar)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.delete_button = QPushButton(self.bottom_bar)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_4.addWidget(self.delete_button)

        self.validate_button = QPushButton(self.bottom_bar)
        self.validate_button.setObjectName(u"validate_button")
        self.validate_button.setStyleSheet(u"background-color: rgb(86, 73, 255);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.validate_button)


        self.question_area.addWidget(self.bottom_bar)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Points for question:", None))
        self.delete_button.setText(QCoreApplication.translate("Form", u"Delete", None))
        self.validate_button.setText(QCoreApplication.translate("Form", u"Confirm", None))
    # retranslateUi

