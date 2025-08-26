# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sessionRecord.ui'
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
    QSizePolicy, QWidget)

class Ui_session_widget(object):
    def setupUi(self, session_widget):
        if not session_widget.objectName():
            session_widget.setObjectName(u"session_widget")
        session_widget.resize(600, 100)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(session_widget.sizePolicy().hasHeightForWidth())
        session_widget.setSizePolicy(sizePolicy)
        session_widget.setMinimumSize(QSize(500, 100))
        session_widget.setMaximumSize(QSize(16777215, 200))
        session_widget.setStyleSheet(u"background-color: rgb(70, 70, 70);\n"
"border-color: rgb(192, 192, 192);")
        self.horizontalLayout = QHBoxLayout(session_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.test_title = QLabel(session_widget)
        self.test_title.setObjectName(u"test_title")
        self.test_title.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.test_title)

        self.timestamp_label = QLabel(session_widget)
        self.timestamp_label.setObjectName(u"timestamp_label")
        self.timestamp_label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.timestamp_label)

        self.session_load_button = QPushButton(session_widget)
        self.session_load_button.setObjectName(u"session_load_button")
        self.session_load_button.setMinimumSize(QSize(100, 35))
        self.session_load_button.setMaximumSize(QSize(150, 35))
        self.session_load_button.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.session_load_button)


        self.retranslateUi(session_widget)

        QMetaObject.connectSlotsByName(session_widget)
    # setupUi

    def retranslateUi(self, session_widget):
        session_widget.setWindowTitle(QCoreApplication.translate("session_widget", u"Form", None))
        self.test_title.setText(QCoreApplication.translate("session_widget", u"TextLabel", None))
        self.timestamp_label.setText(QCoreApplication.translate("session_widget", u"TextLabel", None))
        self.session_load_button.setText(QCoreApplication.translate("session_widget", u"Load", None))
    # retranslateUi

