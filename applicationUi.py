# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'applicationUi.ui'
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
from PySide6.QtWidgets import (QApplication, QDockWidget, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QTabWidget, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        if not StackedWidget.objectName():
            StackedWidget.setObjectName(u"StackedWidget")
        StackedWidget.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(StackedWidget.sizePolicy().hasHeightForWidth())
        StackedWidget.setSizePolicy(sizePolicy)
        StackedWidget.setMinimumSize(QSize(800, 600))
        StackedWidget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.03, y1:0.063, x2:0.921182, y2:1, stop:0.0935961 rgba(24, 108, 128, 255), stop:1 rgba(255, 184, 127, 255));")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.page_1.sizePolicy().hasHeightForWidth())
        self.page_1.setSizePolicy(sizePolicy1)
        self.page_1.setMinimumSize(QSize(800, 600))
        self.page_1.setMouseTracking(False)
        self.page_1.setAutoFillBackground(False)
        self.horizontalLayout = QHBoxLayout(self.page_1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 12, -1)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.teacher_button = QPushButton(self.page_1)
        self.teacher_button.setObjectName(u"teacher_button")
        self.teacher_button.setMinimumSize(QSize(320, 160))
        self.teacher_button.setMaximumSize(QSize(16777215, 200))
        self.teacher_button.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.980296, y2:0.972, stop:0 rgba(33, 33, 33, 255), stop:1 rgba(93, 82, 120, 255));\n"
"background-color: rgb(70, 70, 70);\n"
"color: white")

        self.horizontalLayout.addWidget(self.teacher_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.student_button = QPushButton(self.page_1)
        self.student_button.setObjectName(u"student_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.student_button.sizePolicy().hasHeightForWidth())
        self.student_button.setSizePolicy(sizePolicy2)
        self.student_button.setMinimumSize(QSize(320, 160))
        self.student_button.setMaximumSize(QSize(16777215, 200))
        self.student_button.setBaseSize(QSize(320, 160))
        self.student_button.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(206, 235, 106, 255), stop:1 rgba(255, 86, 86, 255));\n"
"background-color: rgb(70, 70, 70);\n"
"color: white")

        self.horizontalLayout.addWidget(self.student_button)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        StackedWidget.addWidget(self.page_1)
        self.test_editor = QWidget()
        self.test_editor.setObjectName(u"test_editor")
        self.horizontalLayout_2 = QHBoxLayout(self.test_editor)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.dockWidget = QDockWidget(self.test_editor)
        self.dockWidget.setObjectName(u"dockWidget")
        self.dockWidget.setStyleSheet(u"background-color: rgb(48, 48, 48);\n"
"")
        self.dockWidget.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.gridLayout_2 = QGridLayout(self.dockWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget = QTabWidget(self.dockWidgetContents)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(200, 0))
        self.tabWidget.setMaximumSize(QSize(300, 16777215))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_3 = QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.addSingleButton = QPushButton(self.tab)
        self.addSingleButton.setObjectName(u"addSingleButton")

        self.gridLayout_3.addWidget(self.addSingleButton, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_2.addWidget(self.tabWidget, 1, 0, 1, 1)

        self.scrollArea = QScrollArea(self.dockWidgetContents)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(500, 0))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 498, 480))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.test_area = QVBoxLayout()
        self.test_area.setObjectName(u"test_area")

        self.verticalLayout.addLayout(self.test_area)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 1, 1, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.back_button_editor = QPushButton(self.dockWidgetContents)
        self.back_button_editor.setObjectName(u"back_button_editor")
        self.back_button_editor.setMaximumSize(QSize(70, 20))
        font = QFont()
        font.setPointSize(11)
        self.back_button_editor.setFont(font)
        self.back_button_editor.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(70, 70, 70);")

        self.horizontalLayout_5.addWidget(self.back_button_editor)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.pushButton_2 = QPushButton(self.dockWidgetContents)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_5.addWidget(self.pushButton_2)


        self.gridLayout_2.addLayout(self.horizontalLayout_5, 0, 0, 1, 2)

        self.dockWidget.setWidget(self.dockWidgetContents)

        self.horizontalLayout_2.addWidget(self.dockWidget)

        StackedWidget.addWidget(self.test_editor)
        self.student_registration = QWidget()
        self.student_registration.setObjectName(u"student_registration")
        self.gridLayout = QGridLayout(self.student_registration)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(self.student_registration)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(400, 260))
        self.widget.setStyleSheet(u"background-color: rgb(48, 48, 48);")
        self.name_label = QLabel(self.widget)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setGeometry(QRect(100, 40, 201, 31))
        self.name_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.textEdit_name = QTextEdit(self.widget)
        self.textEdit_name.setObjectName(u"textEdit_name")
        self.textEdit_name.setGeometry(QRect(100, 70, 200, 30))
        font1 = QFont()
        font1.setFamilies([u"Impact"])
        font1.setPointSize(15)
        self.textEdit_name.setFont(font1)
        self.textEdit_name.setStyleSheet(u"background-color: rgb(97, 97, 97);\n"
"color: rgb(255, 255, 255);")
        self.textEdit_name.setPlaceholderText(u"")
        self.connection_label = QLabel(self.widget)
        self.connection_label.setObjectName(u"connection_label")
        self.connection_label.setGeometry(QRect(100, 130, 201, 31))
        self.connection_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.textEdit_conn = QTextEdit(self.widget)
        self.textEdit_conn.setObjectName(u"textEdit_conn")
        self.textEdit_conn.setGeometry(QRect(100, 160, 200, 30))
        self.textEdit_conn.setFont(font1)
        self.textEdit_conn.setStyleSheet(u"background-color: rgb(97, 97, 97);\n"
"color: rgb(255, 255, 255);")
        self.submit_button = QPushButton(self.widget)
        self.submit_button.setObjectName(u"submit_button")
        self.submit_button.setGeometry(QRect(140, 210, 113, 32))
        self.submit_button.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(70, 70, 70);")
        self.back_button_student = QPushButton(self.widget)
        self.back_button_student.setObjectName(u"back_button_student")
        self.back_button_student.setGeometry(QRect(10, 10, 70, 20))
        self.back_button_student.setFont(font)
        self.back_button_student.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(70, 70, 70);")
        self.name_descriptor = QLabel(self.widget)
        self.name_descriptor.setObjectName(u"name_descriptor")
        self.name_descriptor.setGeometry(QRect(100, 100, 201, 31))
        font2 = QFont()
        font2.setPointSize(9)
        self.name_descriptor.setFont(font2)
        self.name_descriptor.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        StackedWidget.addWidget(self.student_registration)

        self.retranslateUi(StackedWidget)

        StackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(StackedWidget)
    # setupUi

    def retranslateUi(self, StackedWidget):
        StackedWidget.setWindowTitle(QCoreApplication.translate("StackedWidget", u"StackedWidget", None))
        self.teacher_button.setText(QCoreApplication.translate("StackedWidget", u"Create/edit tests", None))
        self.student_button.setText(QCoreApplication.translate("StackedWidget", u"Take a test", None))
        self.dockWidget.setWindowTitle(QCoreApplication.translate("StackedWidget", u"Test editor", None))
        self.addSingleButton.setText(QCoreApplication.translate("StackedWidget", u"PushButton", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("StackedWidget", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("StackedWidget", u"Tab 2", None))
        self.back_button_editor.setText(QCoreApplication.translate("StackedWidget", u"< Back", None))
        self.pushButton_2.setText(QCoreApplication.translate("StackedWidget", u"PushButton", None))
        self.name_label.setText(QCoreApplication.translate("StackedWidget", u"Name:", None))
        self.connection_label.setText(QCoreApplication.translate("StackedWidget", u"Connection ID:", None))
        self.submit_button.setText(QCoreApplication.translate("StackedWidget", u"Submit", None))
        self.back_button_student.setText(QCoreApplication.translate("StackedWidget", u"< Back", None))
        self.name_descriptor.setText(QCoreApplication.translate("StackedWidget", u"Must insclude only latin letters and be\n"
"between 2 and 25 characters", None))
    # retranslateUi

