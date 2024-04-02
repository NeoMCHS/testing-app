# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'questionSingleChoice.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHBoxLayout,
    QLabel, QPlainTextEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(488, 280)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(0, 280))
        Form.setMaximumSize(QSize(1500000, 1500000))
        Form.setStyleSheet(u"background-color: rgb(70, 70, 70);\n"
"border-color: rgb(192, 192, 192);")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.main_area = QVBoxLayout()
        self.main_area.setObjectName(u"main_area")
        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(16777215, 80))
        self.textEdit.setStyleSheet(u"background-color: rgb(97, 97, 97);")

        self.main_area.addWidget(self.textEdit)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget_3 = QWidget(Form)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(160, 45))
        self.widget_3.setMaximumSize(QSize(0, 45))
        self.widget_3.setStyleSheet(u"background-color: rgb(97, 97, 97);")
        self.point_destribution = QComboBox(self.widget_3)
        self.point_destribution.addItem("")
        self.point_destribution.addItem("")
        self.point_destribution.setObjectName(u"point_destribution")
        self.point_destribution.setGeometry(QRect(20, 10, 120, 23))
        self.point_destribution.setMaximumSize(QSize(16777215, 23))
        font = QFont()
        font.setPointSize(9)
        self.point_destribution.setFont(font)
        self.point_destribution.setStyleSheet(u"background-color: rgb(70, 70, 70);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.widget_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

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
        self.plainTextEdit_2 = QPlainTextEdit(self.widget_2)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setGeometry(QRect(138, 12, 50, 24))
        self.plainTextEdit_2.setMinimumSize(QSize(50, 24))
        self.plainTextEdit_2.setMaximumSize(QSize(50, 24))
        self.plainTextEdit_2.setStyleSheet(u"background-color: rgb(70, 70, 70);\n"
"color: rgb(255, 255, 255);")
        self.plainTextEdit_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_2.addWidget(self.widget_2)


        self.main_area.addLayout(self.horizontalLayout_2)

        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 445, 76))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.answers_area = QVBoxLayout()
        self.answers_area.setObjectName(u"answers_area")
        self.answer_choice = QWidget(self.scrollAreaWidgetContents)
        self.answer_choice.setObjectName(u"answer_choice")
        self.answer_choice.setMinimumSize(QSize(0, 50))
        self.answer_choice.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_3 = QHBoxLayout(self.answer_choice)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.is_right = QCheckBox(self.answer_choice)
        self.is_right.setObjectName(u"is_right")
        self.is_right.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_3.addWidget(self.is_right)

        self.answer_choice_edit = QPlainTextEdit(self.answer_choice)
        self.answer_choice_edit.setObjectName(u"answer_choice_edit")
        self.answer_choice_edit.setMinimumSize(QSize(0, 20))
        self.answer_choice_edit.setMaximumSize(QSize(15000000, 30))
        self.answer_choice_edit.setSizeIncrement(QSize(0, 0))
        self.answer_choice_edit.setStyleSheet(u"background-color: rgb(97, 97, 97);")
        self.answer_choice_edit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_3.addWidget(self.answer_choice_edit)


        self.answers_area.addWidget(self.answer_choice)


        self.verticalLayout_4.addLayout(self.answers_area)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.main_area.addWidget(self.scrollArea)


        self.verticalLayout.addLayout(self.main_area)

        self.bottom_bar = QWidget(Form)
        self.bottom_bar.setObjectName(u"bottom_bar")
        self.bottom_bar.setMinimumSize(QSize(0, 30))
        self.horizontalLayout_4 = QHBoxLayout(self.bottom_bar)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.delete_button = QPushButton(self.bottom_bar)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setStyleSheet(u"background-color: rgb(255, 0, 0);")

        self.horizontalLayout_4.addWidget(self.delete_button)

        self.remove_answer_button = QPushButton(self.bottom_bar)
        self.remove_answer_button.setObjectName(u"remove_answer_button")
        self.remove_answer_button.setStyleSheet(u"background-color: rgb(97, 97, 97);")

        self.horizontalLayout_4.addWidget(self.remove_answer_button)

        self.add_answer_button = QPushButton(self.bottom_bar)
        self.add_answer_button.setObjectName(u"add_answer_button")
        self.add_answer_button.setStyleSheet(u"background-color: rgb(97, 97, 97);")

        self.horizontalLayout_4.addWidget(self.add_answer_button)

        self.validate_button = QPushButton(self.bottom_bar)
        self.validate_button.setObjectName(u"validate_button")
        self.validate_button.setStyleSheet(u"background-color: rgb(86, 73, 255);")

        self.horizontalLayout_4.addWidget(self.validate_button)


        self.verticalLayout.addWidget(self.bottom_bar)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.point_destribution.setItemText(0, QCoreApplication.translate("Form", u"Split the points", None))
        self.point_destribution.setItemText(1, QCoreApplication.translate("Form", u"Give all points ", None))

        self.label.setText(QCoreApplication.translate("Form", u"Points for question:", None))
        self.is_right.setText("")
        self.delete_button.setText(QCoreApplication.translate("Form", u"Delete", None))
        self.remove_answer_button.setText(QCoreApplication.translate("Form", u"Remove answer", None))
        self.add_answer_button.setText(QCoreApplication.translate("Form", u"Add answer", None))
        self.validate_button.setText(QCoreApplication.translate("Form", u"Confirm", None))
    # retranslateUi

