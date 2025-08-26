# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'userForm.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QTextBrowser, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(500, 100)
        Form.setMinimumSize(QSize(500, 100))
        Form.setMaximumSize(QSize(16777215, 100))
        Form.setStyleSheet(u"background-color: rgb(70, 70, 70);\n"
"border-color: rgb(192, 192, 192);")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(70, 16777215))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.label_2)

        self.username_field = QTextBrowser(Form)
        self.username_field.setObjectName(u"username_field")
        self.username_field.setMaximumSize(QSize(16777215, 24))
        self.username_field.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.username_field.setFrameShape(QFrame.NoFrame)
        self.username_field.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout.addWidget(self.username_field)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(70, 16777215))
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.label_3)

        self.role_field = QTextBrowser(Form)
        self.role_field.setObjectName(u"role_field")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.role_field.sizePolicy().hasHeightForWidth())
        self.role_field.setSizePolicy(sizePolicy)
        self.role_field.setMinimumSize(QSize(50, 0))
        self.role_field.setMaximumSize(QSize(100000, 24))
        self.role_field.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.role_field.setFrameShape(QFrame.NoFrame)
        self.role_field.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout.addWidget(self.role_field)

        self.set_new_password_button = QPushButton(Form)
        self.set_new_password_button.setObjectName(u"set_new_password_button")
        self.set_new_password_button.setMinimumSize(QSize(130, 35))
        self.set_new_password_button.setMaximumSize(QSize(130, 35))
        self.set_new_password_button.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.set_new_password_button)

        self.delete_user_button = QPushButton(Form)
        self.delete_user_button.setObjectName(u"delete_user_button")
        self.delete_user_button.setMinimumSize(QSize(100, 35))
        self.delete_user_button.setMaximumSize(QSize(100, 35))
        self.delete_user_button.setStyleSheet(u"background-color: rgb(255, 0, 0); color: rgb(0, 0, 0);")

        self.horizontalLayout.addWidget(self.delete_user_button)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Username:", None))
        self.username_field.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Role:", None))
        self.role_field.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.set_new_password_button.setText(QCoreApplication.translate("Form", u"Set new password", None))
        self.delete_user_button.setText(QCoreApplication.translate("Form", u"Delete", None))
    # retranslateUi

