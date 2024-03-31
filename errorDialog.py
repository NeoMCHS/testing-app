# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'errorDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QSizePolicy, QWidget)

class Ui_dialog(object):
    def setupUi(self, dialog):
        if not dialog.objectName():
            dialog.setObjectName(u"dialog")
        dialog.resize(400, 200)
        dialog.setMinimumSize(QSize(400, 200))
        dialog.setMaximumSize(QSize(400, 200))
        dialog.setStyleSheet(u"background-color: rgb(48, 48, 48);")
        self.buttonBox = QDialogButtonBox(dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 160, 341, 31))
        self.buttonBox.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)
        self.header_label = QLabel(dialog)
        self.header_label.setObjectName(u"header_label")
        self.header_label.setGeometry(QRect(50, 20, 281, 31))
        font = QFont()
        font.setPointSize(17)
        self.header_label.setFont(font)
        self.header_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.description_label = QLabel(dialog)
        self.description_label.setObjectName(u"description_label")
        self.description_label.setGeometry(QRect(50, 60, 281, 81))
        self.description_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.description_label.setWordWrap(True)

        self.retranslateUi(dialog)
        self.buttonBox.accepted.connect(dialog.accept)
        self.buttonBox.rejected.connect(dialog.reject)

        QMetaObject.connectSlotsByName(dialog)
    # setupUi

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(QCoreApplication.translate("dialog", u"Dialog", None))
        self.header_label.setText(QCoreApplication.translate("dialog", u"Connection failure", None))
        self.description_label.setText(QCoreApplication.translate("dialog", u"Something went wrong :(", None))
    # retranslateUi

