# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'applicationUi.ui'
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
from PySide6.QtWidgets import (QApplication, QDockWidget, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QTabWidget, QTextEdit,
    QTimeEdit, QVBoxLayout, QWidget)

class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        if not StackedWidget.objectName():
            StackedWidget.setObjectName(u"StackedWidget")
        StackedWidget.resize(830, 613)
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
        self.tabWidget.setMinimumSize(QSize(180, 0))
        self.tabWidget.setMaximumSize(QSize(300, 16777215))
        self.add_questions_tab = QWidget()
        self.add_questions_tab.setObjectName(u"add_questions_tab")
        self.gridLayout_3 = QGridLayout(self.add_questions_tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.addSingleButton = QPushButton(self.add_questions_tab)
        self.addSingleButton.setObjectName(u"addSingleButton")
        self.addSingleButton.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.addSingleButton, 0, 0, 1, 1)

        self.addTextQuestion = QPushButton(self.add_questions_tab)
        self.addTextQuestion.setObjectName(u"addTextQuestion")
        self.addTextQuestion.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.addTextQuestion, 2, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.tabWidget.addTab(self.add_questions_tab, "")
        self.settings_tab = QWidget()
        self.settings_tab.setObjectName(u"settings_tab")
        self.verticalLayout_2 = QVBoxLayout(self.settings_tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_2 = QWidget(self.settings_tab)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.widget_2.setMinimumSize(QSize(1, 50))
        self.widget_2.setMaximumSize(QSize(16777215, 85))
        self.widget_2.setSizeIncrement(QSize(0, 0))
        self.widget_2.setStyleSheet(u"\n"
"background-color: rgb(70, 70, 70);")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.label)

        self.test_name = QTextEdit(self.widget_2)
        self.test_name.setObjectName(u"test_name")
        font = QFont()
        font.setPointSize(10)
        self.test_name.setFont(font)

        self.verticalLayout_3.addWidget(self.test_name)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.verticalSpacer_3 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.widget_3 = QWidget(self.settings_tab)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 45))
        self.widget_3.setMaximumSize(QSize(16777215, 45))
        self.widget_3.setStyleSheet(u"background-color: rgb(70, 70, 70);")
        self.time_limit_layout = QHBoxLayout(self.widget_3)
        self.time_limit_layout.setObjectName(u"time_limit_layout")
        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(40, 0))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.time_limit_layout.addWidget(self.label_2)

        self.timeEdit = QTimeEdit(self.widget_3)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setMinimumSize(QSize(70, 0))

        self.time_limit_layout.addWidget(self.timeEdit)


        self.verticalLayout_2.addWidget(self.widget_3)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.pushButton_4 = QPushButton(self.settings_tab)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_2.addWidget(self.pushButton_4)

        self.tabWidget.addTab(self.settings_tab, "")

        self.gridLayout_2.addWidget(self.tabWidget, 1, 0, 1, 1)

        self.scrollArea = QScrollArea(self.dockWidgetContents)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(550, 0))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 548, 493))
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
        font1 = QFont()
        font1.setPointSize(11)
        self.back_button_editor.setFont(font1)
        self.back_button_editor.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(70, 70, 70);")

        self.horizontalLayout_5.addWidget(self.back_button_editor)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.test_validation = QPushButton(self.dockWidgetContents)
        self.test_validation.setObjectName(u"test_validation")

        self.horizontalLayout_5.addWidget(self.test_validation)


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
        font2 = QFont()
        font2.setFamilies([u"Impact"])
        font2.setPointSize(15)
        self.textEdit_name.setFont(font2)
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
        self.textEdit_conn.setFont(font2)
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
        self.back_button_student.setFont(font1)
        self.back_button_student.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(70, 70, 70);")
        self.name_descriptor = QLabel(self.widget)
        self.name_descriptor.setObjectName(u"name_descriptor")
        self.name_descriptor.setGeometry(QRect(100, 100, 201, 31))
        font3 = QFont()
        font3.setPointSize(9)
        self.name_descriptor.setFont(font3)
        self.name_descriptor.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        StackedWidget.addWidget(self.student_registration)

        self.retranslateUi(StackedWidget)

        StackedWidget.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(StackedWidget)
    # setupUi

    def retranslateUi(self, StackedWidget):
        StackedWidget.setWindowTitle(QCoreApplication.translate("StackedWidget", u"StackedWidget", None))
        self.teacher_button.setText(QCoreApplication.translate("StackedWidget", u"Create/edit tests", None))
        self.student_button.setText(QCoreApplication.translate("StackedWidget", u"Take a test", None))
        self.dockWidget.setWindowTitle(QCoreApplication.translate("StackedWidget", u"Test editor", None))
        self.addSingleButton.setText(QCoreApplication.translate("StackedWidget", u"Choice question", None))
        self.addTextQuestion.setText(QCoreApplication.translate("StackedWidget", u"Free form question", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.add_questions_tab), QCoreApplication.translate("StackedWidget", u"Questions", None))
        self.label.setText(QCoreApplication.translate("StackedWidget", u"Name of the Test:", None))
        self.test_name.setHtml(QCoreApplication.translate("StackedWidget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("StackedWidget", u"Time limit:", None))
        self.pushButton_4.setText(QCoreApplication.translate("StackedWidget", u"PushButton", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings_tab), QCoreApplication.translate("StackedWidget", u"Settings", None))
        self.back_button_editor.setText(QCoreApplication.translate("StackedWidget", u"< Back", None))
        self.test_validation.setText(QCoreApplication.translate("StackedWidget", u"PushButton", None))
        self.name_label.setText(QCoreApplication.translate("StackedWidget", u"Name:", None))
        self.connection_label.setText(QCoreApplication.translate("StackedWidget", u"Connection ID:", None))
        self.submit_button.setText(QCoreApplication.translate("StackedWidget", u"Submit", None))
        self.back_button_student.setText(QCoreApplication.translate("StackedWidget", u"< Back", None))
        self.name_descriptor.setText(QCoreApplication.translate("StackedWidget", u"Must insclude only latin letters and be\n"
"between 2 and 25 characters", None))
    # retranslateUi

