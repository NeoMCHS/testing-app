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
from PySide6.QtWidgets import (QApplication, QComboBox, QDockWidget, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QTextBrowser, QTextEdit,
    QTimeEdit, QVBoxLayout, QWidget)

class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        if not StackedWidget.objectName():
            StackedWidget.setObjectName(u"StackedWidget")
        StackedWidget.resize(823, 706)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(StackedWidget.sizePolicy().hasHeightForWidth())
        StackedWidget.setSizePolicy(sizePolicy)
        StackedWidget.setMinimumSize(QSize(800, 600))
        StackedWidget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.03, y1:0.063, x2:0.921182, y2:1, stop:0.0935961 rgba(24, 108, 128, 255), stop:1 rgba(255, 184, 127, 255));")
        self.intro_page = QWidget()
        self.intro_page.setObjectName(u"intro_page")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.intro_page.sizePolicy().hasHeightForWidth())
        self.intro_page.setSizePolicy(sizePolicy1)
        self.intro_page.setMinimumSize(QSize(800, 600))
        self.intro_page.setMouseTracking(False)
        self.intro_page.setAutoFillBackground(False)
        self.horizontalLayout = QHBoxLayout(self.intro_page)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 12, -1)
        self.login_widget = QWidget(self.intro_page)
        self.login_widget.setObjectName(u"login_widget")
        self.login_widget.setMinimumSize(QSize(500, 300))
        self.login_widget.setMaximumSize(QSize(500, 300))
        self.login_widget.setStyleSheet(u"background-color: rgb(48, 48, 48);")
        self.username_input = QTextEdit(self.login_widget)
        self.username_input.setObjectName(u"username_input")
        self.username_input.setGeometry(QRect(135, 60, 230, 30))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(14)
        self.username_input.setFont(font)
        self.username_input.setStyleSheet(u"background-color: rgb(97, 97, 97);\n"
"color: rgb(255, 255, 255);")
        self.ip_input = QTextEdit(self.login_widget)
        self.ip_input.setObjectName(u"ip_input")
        self.ip_input.setGeometry(QRect(135, 200, 130, 30))
        self.ip_input.setStyleSheet(u"background-color: rgb(97, 97, 97);\n"
"color: rgb(255, 255, 255);")
        self.port_input = QTextEdit(self.login_widget)
        self.port_input.setObjectName(u"port_input")
        self.port_input.setGeometry(QRect(285, 200, 71, 30))
        self.port_input.setStyleSheet(u"background-color: rgb(97, 97, 97);\n"
"color: rgb(255, 255, 255);")
        self.connection_label_2 = QLabel(self.login_widget)
        self.connection_label_2.setObjectName(u"connection_label_2")
        self.connection_label_2.setGeometry(QRect(135, 180, 141, 16))
        font1 = QFont()
        font1.setPointSize(14)
        self.connection_label_2.setFont(font1)
        self.connection_label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.password_label = QLabel(self.login_widget)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setGeometry(QRect(135, 110, 100, 16))
        self.password_label.setFont(font1)
        self.password_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.username_label = QLabel(self.login_widget)
        self.username_label.setObjectName(u"username_label")
        self.username_label.setGeometry(QRect(135, 40, 100, 16))
        self.username_label.setFont(font1)
        self.username_label.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);")
        self.separator = QLabel(self.login_widget)
        self.separator.setObjectName(u"separator")
        self.separator.setGeometry(QRect(270, 190, 10, 41))
        font2 = QFont()
        font2.setPointSize(28)
        font2.setBold(True)
        self.separator.setFont(font2)
        self.separator.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.login_button = QPushButton(self.login_widget)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setGeometry(QRect(195, 250, 110, 32))
        self.login_button.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(70, 70, 70);")
        self.password_input = QLineEdit(self.login_widget)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setGeometry(QRect(135, 130, 230, 30))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(16)
        self.password_input.setFont(font3)
        self.password_input.setStyleSheet(u"background-color: rgb(97, 97, 97);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.login_widget)

        StackedWidget.addWidget(self.intro_page)
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
        font4 = QFont()
        font4.setPointSize(10)
        self.test_name.setFont(font4)

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

        self.tabWidget.addTab(self.settings_tab, "")

        self.gridLayout_2.addWidget(self.tabWidget, 1, 0, 1, 1)

        self.scrollArea = QScrollArea(self.dockWidgetContents)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(550, 0))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 548, 585))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.test_area = QVBoxLayout()
        self.test_area.setObjectName(u"test_area")

        self.verticalLayout.addLayout(self.test_area)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 1, 1, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.editor_logout = QPushButton(self.dockWidgetContents)
        self.editor_logout.setObjectName(u"editor_logout")
        self.editor_logout.setMinimumSize(QSize(75, 24))
        self.editor_logout.setMaximumSize(QSize(75, 24))
        self.editor_logout.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.editor_logout)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.clear_test = QPushButton(self.dockWidgetContents)
        self.clear_test.setObjectName(u"clear_test")
        self.clear_test.setMinimumSize(QSize(75, 0))
        self.clear_test.setStyleSheet(u"color: rgb(255, 255, 255);background-color: rgb(255, 0, 0); color: rgb(0, 0, 0);")

        self.horizontalLayout_5.addWidget(self.clear_test)

        self.widget_4 = QWidget(self.dockWidgetContents)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(3, 21))
        self.widget_4.setMaximumSize(QSize(3, 16777215))
        self.widget_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.widget_4)

        self.load_test = QPushButton(self.dockWidgetContents)
        self.load_test.setObjectName(u"load_test")
        self.load_test.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.load_test)

        self.save_test = QPushButton(self.dockWidgetContents)
        self.save_test.setObjectName(u"save_test")
        self.save_test.setStyleSheet(u"background-color: rgb(86, 73, 255); color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.save_test)

        self.widget_5 = QWidget(self.dockWidgetContents)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(3, 21))
        self.widget_5.setMaximumSize(QSize(3, 16777202))
        self.widget_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.widget_5)

        self.editor_to_session_button = QPushButton(self.dockWidgetContents)
        self.editor_to_session_button.setObjectName(u"editor_to_session_button")
        self.editor_to_session_button.setMinimumSize(QSize(75, 24))
        self.editor_to_session_button.setMaximumSize(QSize(70, 24))
        font5 = QFont()
        font5.setPointSize(13)
        self.editor_to_session_button.setFont(font5)
        self.editor_to_session_button.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")

        self.horizontalLayout_5.addWidget(self.editor_to_session_button)

        self.host_test = QPushButton(self.dockWidgetContents)
        self.host_test.setObjectName(u"host_test")
        self.host_test.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.host_test)


        self.gridLayout_2.addLayout(self.horizontalLayout_5, 0, 0, 1, 2)

        self.dockWidget.setWidget(self.dockWidgetContents)

        self.horizontalLayout_2.addWidget(self.dockWidget)

        StackedWidget.addWidget(self.test_editor)
        self.session_selection = QWidget()
        self.session_selection.setObjectName(u"session_selection")
        self.gridLayout = QGridLayout(self.session_selection)
        self.gridLayout.setObjectName(u"gridLayout")
        self.student_session_dock = QDockWidget(self.session_selection)
        self.student_session_dock.setObjectName(u"student_session_dock")
        self.student_session_dock.setStyleSheet(u"background-color: rgb(48, 48, 48);")
        self.student_session_dock.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.student_session_widget = QWidget()
        self.student_session_widget.setObjectName(u"student_session_widget")
        self.verticalLayout_5 = QVBoxLayout(self.student_session_widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.student_session_top_bar = QWidget(self.student_session_widget)
        self.student_session_top_bar.setObjectName(u"student_session_top_bar")
        self.student_session_top_bar.setMinimumSize(QSize(0, 40))
        self.student_session_top_bar.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_3 = QHBoxLayout(self.student_session_top_bar)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.session_selection_logout = QPushButton(self.student_session_top_bar)
        self.session_selection_logout.setObjectName(u"session_selection_logout")
        self.session_selection_logout.setMinimumSize(QSize(75, 28))
        self.session_selection_logout.setMaximumSize(QSize(16777215, 30))
        self.session_selection_logout.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.session_selection_logout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.students_refresh_button = QPushButton(self.student_session_top_bar)
        self.students_refresh_button.setObjectName(u"students_refresh_button")
        self.students_refresh_button.setMinimumSize(QSize(100, 0))
        self.students_refresh_button.setMaximumSize(QSize(100, 30))
        self.students_refresh_button.setStyleSheet(u"background-color: rgb(86, 73, 255); color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.students_refresh_button)


        self.verticalLayout_5.addWidget(self.student_session_top_bar)

        self.students_session_scroll_area = QScrollArea(self.student_session_widget)
        self.students_session_scroll_area.setObjectName(u"students_session_scroll_area")
        self.students_session_scroll_area.setWidgetResizable(True)
        self.student_session_scroll_contents = QWidget()
        self.student_session_scroll_contents.setObjectName(u"student_session_scroll_contents")
        self.student_session_scroll_contents.setGeometry(QRect(0, 0, 773, 584))
        self.verticalLayout_7 = QVBoxLayout(self.student_session_scroll_contents)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.student_session_area = QVBoxLayout()
        self.student_session_area.setObjectName(u"student_session_area")

        self.verticalLayout_7.addLayout(self.student_session_area)

        self.students_session_scroll_area.setWidget(self.student_session_scroll_contents)

        self.verticalLayout_5.addWidget(self.students_session_scroll_area)

        self.student_session_dock.setWidget(self.student_session_widget)

        self.gridLayout.addWidget(self.student_session_dock, 0, 0, 1, 1)

        StackedWidget.addWidget(self.session_selection)
        self.session_history = QWidget()
        self.session_history.setObjectName(u"session_history")
        self.gridLayout_4 = QGridLayout(self.session_history)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.session_history_dock = QDockWidget(self.session_history)
        self.session_history_dock.setObjectName(u"session_history_dock")
        self.session_history_dock.setStyleSheet(u"background-color: rgb(48, 48, 48);")
        self.session_history_dock.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.session_history_widget = QWidget()
        self.session_history_widget.setObjectName(u"session_history_widget")
        self.verticalLayout_6 = QVBoxLayout(self.session_history_widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.session_history_top_bar = QWidget(self.session_history_widget)
        self.session_history_top_bar.setObjectName(u"session_history_top_bar")
        self.session_history_top_bar.setMinimumSize(QSize(0, 40))
        self.session_history_top_bar.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_4 = QHBoxLayout(self.session_history_top_bar)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.session_history_logout = QPushButton(self.session_history_top_bar)
        self.session_history_logout.setObjectName(u"session_history_logout")
        self.session_history_logout.setMinimumSize(QSize(75, 28))
        self.session_history_logout.setMaximumSize(QSize(75, 30))
        self.session_history_logout.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.session_history_logout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.session_to_editor_button = QPushButton(self.session_history_top_bar)
        self.session_to_editor_button.setObjectName(u"session_to_editor_button")
        self.session_to_editor_button.setMinimumSize(QSize(100, 0))
        self.session_to_editor_button.setMaximumSize(QSize(100, 30))
        self.session_to_editor_button.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.session_to_editor_button)

        self.session_history_refresh_button = QPushButton(self.session_history_top_bar)
        self.session_history_refresh_button.setObjectName(u"session_history_refresh_button")
        self.session_history_refresh_button.setMinimumSize(QSize(100, 0))
        self.session_history_refresh_button.setMaximumSize(QSize(100, 30))
        self.session_history_refresh_button.setStyleSheet(u"background-color: rgb(86, 73, 255); color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.session_history_refresh_button)


        self.verticalLayout_6.addWidget(self.session_history_top_bar)

        self.session_history_scroll_area = QScrollArea(self.session_history_widget)
        self.session_history_scroll_area.setObjectName(u"session_history_scroll_area")
        self.session_history_scroll_area.setWidgetResizable(True)
        self.session_history_scroll_contents = QWidget()
        self.session_history_scroll_contents.setObjectName(u"session_history_scroll_contents")
        self.session_history_scroll_contents.setGeometry(QRect(0, 0, 773, 584))
        self.verticalLayout_8 = QVBoxLayout(self.session_history_scroll_contents)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.session_history_area = QVBoxLayout()
        self.session_history_area.setObjectName(u"session_history_area")

        self.verticalLayout_8.addLayout(self.session_history_area)

        self.session_history_scroll_area.setWidget(self.session_history_scroll_contents)

        self.verticalLayout_6.addWidget(self.session_history_scroll_area)

        self.session_history_dock.setWidget(self.session_history_widget)

        self.gridLayout_4.addWidget(self.session_history_dock, 0, 0, 1, 1)

        StackedWidget.addWidget(self.session_history)
        self.test_taking = QWidget()
        self.test_taking.setObjectName(u"test_taking")
        self.verticalLayout_4 = QVBoxLayout(self.test_taking)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget = QWidget(self.test_taking)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(48, 48, 48);")
        self.verticalLayout_11 = QVBoxLayout(self.widget)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.test_taking_top_bar = QWidget(self.widget)
        self.test_taking_top_bar.setObjectName(u"test_taking_top_bar")
        self.test_taking_top_bar.setMinimumSize(QSize(0, 40))
        self.test_taking_top_bar.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_7 = QHBoxLayout(self.test_taking_top_bar)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)

        self.label_3 = QLabel(self.test_taking_top_bar)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 28))
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_7.addWidget(self.label_3)

        self.test_current_question_label = QLabel(self.test_taking_top_bar)
        self.test_current_question_label.setObjectName(u"test_current_question_label")
        self.test_current_question_label.setMinimumSize(QSize(0, 28))
        self.test_current_question_label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_7.addWidget(self.test_current_question_label)

        self.test_timer_label = QLabel(self.test_taking_top_bar)
        self.test_timer_label.setObjectName(u"test_timer_label")
        self.test_timer_label.setMinimumSize(QSize(0, 28))
        self.test_timer_label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_7.addWidget(self.test_timer_label)

        self.test_timer = QLabel(self.test_taking_top_bar)
        self.test_timer.setObjectName(u"test_timer")
        self.test_timer.setMinimumSize(QSize(0, 28))
        self.test_timer.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_7.addWidget(self.test_timer)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)


        self.verticalLayout_11.addWidget(self.test_taking_top_bar)

        self.test_questions_area = QStackedWidget(self.widget)
        self.test_questions_area.setObjectName(u"test_questions_area")

        self.verticalLayout_11.addWidget(self.test_questions_area)


        self.verticalLayout_4.addWidget(self.widget)

        StackedWidget.addWidget(self.test_taking)
        self.hosted_session = QWidget()
        self.hosted_session.setObjectName(u"hosted_session")
        self.gridLayout_5 = QGridLayout(self.hosted_session)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.hosted_session_dock = QDockWidget(self.hosted_session)
        self.hosted_session_dock.setObjectName(u"hosted_session_dock")
        self.hosted_session_dock.setStyleSheet(u"background-color: rgb(48, 48, 48);")
        self.hosted_session_dock.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.hosted_session_widget = QWidget()
        self.hosted_session_widget.setObjectName(u"hosted_session_widget")
        self.verticalLayout_9 = QVBoxLayout(self.hosted_session_widget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.hosted_session_top_bar = QWidget(self.hosted_session_widget)
        self.hosted_session_top_bar.setObjectName(u"hosted_session_top_bar")
        self.hosted_session_top_bar.setMinimumSize(QSize(0, 40))
        self.hosted_session_top_bar.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_6 = QHBoxLayout(self.hosted_session_top_bar)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.hosted_session_refresh_button = QPushButton(self.hosted_session_top_bar)
        self.hosted_session_refresh_button.setObjectName(u"hosted_session_refresh_button")
        self.hosted_session_refresh_button.setMinimumSize(QSize(100, 0))
        self.hosted_session_refresh_button.setMaximumSize(QSize(100, 30))
        self.hosted_session_refresh_button.setStyleSheet(u"background-color: rgb(86, 73, 255); color: rgb(255, 255, 255);")

        self.horizontalLayout_6.addWidget(self.hosted_session_refresh_button)

        self.end_session_button = QPushButton(self.hosted_session_top_bar)
        self.end_session_button.setObjectName(u"end_session_button")
        self.end_session_button.setMinimumSize(QSize(100, 0))
        self.end_session_button.setMaximumSize(QSize(100, 30))
        self.end_session_button.setStyleSheet(u"color: rgb(255, 255, 255);background-color: rgb(255, 0, 0); color: rgb(0, 0, 0);")

        self.horizontalLayout_6.addWidget(self.end_session_button)


        self.verticalLayout_9.addWidget(self.hosted_session_top_bar)

        self.students_session_scroll_area_2 = QScrollArea(self.hosted_session_widget)
        self.students_session_scroll_area_2.setObjectName(u"students_session_scroll_area_2")
        self.students_session_scroll_area_2.setWidgetResizable(True)
        self.student_session_scroll_contents_2 = QWidget()
        self.student_session_scroll_contents_2.setObjectName(u"student_session_scroll_contents_2")
        self.student_session_scroll_contents_2.setGeometry(QRect(0, 0, 773, 584))
        self.verticalLayout_10 = QVBoxLayout(self.student_session_scroll_contents_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.hosted_session_answers_area = QVBoxLayout()
        self.hosted_session_answers_area.setObjectName(u"hosted_session_answers_area")

        self.verticalLayout_10.addLayout(self.hosted_session_answers_area)

        self.students_session_scroll_area_2.setWidget(self.student_session_scroll_contents_2)

        self.verticalLayout_9.addWidget(self.students_session_scroll_area_2)

        self.hosted_session_dock.setWidget(self.hosted_session_widget)

        self.gridLayout_5.addWidget(self.hosted_session_dock, 0, 0, 1, 1)

        StackedWidget.addWidget(self.hosted_session)
        self.cheat_triggered = QWidget()
        self.cheat_triggered.setObjectName(u"cheat_triggered")
        self.horizontalLayout_8 = QHBoxLayout(self.cheat_triggered)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.widget_6 = QWidget(self.cheat_triggered)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(500, 300))
        self.widget_6.setMaximumSize(QSize(500, 300))
        self.widget_6.setStyleSheet(u"background-color: rgb(48, 48, 48);")
        self.cheating_trigger_password_input = QLineEdit(self.widget_6)
        self.cheating_trigger_password_input.setObjectName(u"cheating_trigger_password_input")
        self.cheating_trigger_password_input.setGeometry(QRect(135, 140, 230, 30))
        self.cheating_trigger_password_input.setFont(font3)
        self.cheating_trigger_password_input.setStyleSheet(u"background-color: rgb(97, 97, 97);\n"
"color: rgb(255, 255, 255);")
        self.cheating_resolve_button = QPushButton(self.widget_6)
        self.cheating_resolve_button.setObjectName(u"cheating_resolve_button")
        self.cheating_resolve_button.setGeometry(QRect(260, 230, 110, 32))
        self.cheating_resolve_button.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(70, 70, 70);")
        self.cheating_exit_button = QPushButton(self.widget_6)
        self.cheating_exit_button.setObjectName(u"cheating_exit_button")
        self.cheating_exit_button.setGeometry(QRect(130, 230, 110, 32))
        self.cheating_exit_button.setStyleSheet(u"color: rgb(255, 255, 255);background-color: rgb(255, 0, 0); color: rgb(0, 0, 0);")
        self.textBrowser = QTextBrowser(self.widget_6)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(100, 40, 300, 91))
        self.textBrowser.setFocusPolicy(Qt.NoFocus)
        self.textBrowser.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.textBrowser.setFrameShape(QFrame.NoFrame)
        self.textBrowser.setFrameShadow(QFrame.Plain)
        self.textBrowser.setLineWidth(0)

        self.horizontalLayout_8.addWidget(self.widget_6)

        StackedWidget.addWidget(self.cheat_triggered)
        self.admin_panel = QWidget()
        self.admin_panel.setObjectName(u"admin_panel")
        self.horizontalLayout_10 = QHBoxLayout(self.admin_panel)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.admin_panel_dock = QDockWidget(self.admin_panel)
        self.admin_panel_dock.setObjectName(u"admin_panel_dock")
        self.admin_panel_dock.setStyleSheet(u"background-color: rgb(48, 48, 48);")
        self.admin_panel_dock.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.student_session_widget_2 = QWidget()
        self.student_session_widget_2.setObjectName(u"student_session_widget_2")
        self.verticalLayout_12 = QVBoxLayout(self.student_session_widget_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.student_session_top_bar_2 = QWidget(self.student_session_widget_2)
        self.student_session_top_bar_2.setObjectName(u"student_session_top_bar_2")
        self.student_session_top_bar_2.setMinimumSize(QSize(0, 40))
        self.student_session_top_bar_2.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_9 = QHBoxLayout(self.student_session_top_bar_2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.admin_panel_logout = QPushButton(self.student_session_top_bar_2)
        self.admin_panel_logout.setObjectName(u"admin_panel_logout")
        self.admin_panel_logout.setMinimumSize(QSize(75, 28))
        self.admin_panel_logout.setMaximumSize(QSize(16777215, 30))
        self.admin_panel_logout.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_9.addWidget(self.admin_panel_logout)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_7)

        self.admin_panel_refresh_button = QPushButton(self.student_session_top_bar_2)
        self.admin_panel_refresh_button.setObjectName(u"admin_panel_refresh_button")
        self.admin_panel_refresh_button.setMinimumSize(QSize(100, 0))
        self.admin_panel_refresh_button.setMaximumSize(QSize(100, 30))
        self.admin_panel_refresh_button.setStyleSheet(u"background-color: rgb(86, 73, 255); color: rgb(255, 255, 255);")

        self.horizontalLayout_9.addWidget(self.admin_panel_refresh_button)

        self.register_user = QPushButton(self.student_session_top_bar_2)
        self.register_user.setObjectName(u"register_user")
        self.register_user.setMinimumSize(QSize(130, 0))
        self.register_user.setMaximumSize(QSize(130, 30))
        self.register_user.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_9.addWidget(self.register_user)


        self.verticalLayout_12.addWidget(self.student_session_top_bar_2)

        self.students_session_scroll_area_3 = QScrollArea(self.student_session_widget_2)
        self.students_session_scroll_area_3.setObjectName(u"students_session_scroll_area_3")
        self.students_session_scroll_area_3.setWidgetResizable(True)
        self.student_session_scroll_contents_3 = QWidget()
        self.student_session_scroll_contents_3.setObjectName(u"student_session_scroll_contents_3")
        self.student_session_scroll_contents_3.setGeometry(QRect(0, 0, 773, 584))
        self.verticalLayout_13 = QVBoxLayout(self.student_session_scroll_contents_3)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.registered_users_area = QVBoxLayout()
        self.registered_users_area.setObjectName(u"registered_users_area")

        self.verticalLayout_13.addLayout(self.registered_users_area)

        self.students_session_scroll_area_3.setWidget(self.student_session_scroll_contents_3)

        self.verticalLayout_12.addWidget(self.students_session_scroll_area_3)

        self.admin_panel_dock.setWidget(self.student_session_widget_2)

        self.horizontalLayout_10.addWidget(self.admin_panel_dock)

        StackedWidget.addWidget(self.admin_panel)
        self.new_user_registration = QWidget()
        self.new_user_registration.setObjectName(u"new_user_registration")
        self.horizontalLayout_11 = QHBoxLayout(self.new_user_registration)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.login_widget_2 = QWidget(self.new_user_registration)
        self.login_widget_2.setObjectName(u"login_widget_2")
        self.login_widget_2.setMinimumSize(QSize(500, 300))
        self.login_widget_2.setMaximumSize(QSize(500, 300))
        self.login_widget_2.setStyleSheet(u"background-color: rgb(48, 48, 48);")
        self.username_input_register = QTextEdit(self.login_widget_2)
        self.username_input_register.setObjectName(u"username_input_register")
        self.username_input_register.setGeometry(QRect(135, 60, 230, 30))
        self.username_input_register.setFont(font)
        self.username_input_register.setStyleSheet(u"background-color: rgb(97, 97, 97);\n"
"color: rgb(255, 255, 255);")
        self.connection_label_3 = QLabel(self.login_widget_2)
        self.connection_label_3.setObjectName(u"connection_label_3")
        self.connection_label_3.setGeometry(QRect(135, 180, 141, 16))
        self.connection_label_3.setFont(font1)
        self.connection_label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.password_label_2 = QLabel(self.login_widget_2)
        self.password_label_2.setObjectName(u"password_label_2")
        self.password_label_2.setGeometry(QRect(135, 110, 100, 16))
        self.password_label_2.setFont(font1)
        self.password_label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.username_label_2 = QLabel(self.login_widget_2)
        self.username_label_2.setObjectName(u"username_label_2")
        self.username_label_2.setGeometry(QRect(135, 40, 100, 16))
        self.username_label_2.setFont(font1)
        self.username_label_2.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);")
        self.register_confirm_button = QPushButton(self.login_widget_2)
        self.register_confirm_button.setObjectName(u"register_confirm_button")
        self.register_confirm_button.setGeometry(QRect(195, 250, 110, 32))
        self.register_confirm_button.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(70, 70, 70);")
        self.password_input_register = QLineEdit(self.login_widget_2)
        self.password_input_register.setObjectName(u"password_input_register")
        self.password_input_register.setGeometry(QRect(135, 130, 230, 30))
        self.password_input_register.setFont(font3)
        self.password_input_register.setStyleSheet(u"background-color: rgb(97, 97, 97);\n"
"color: rgb(255, 255, 255);")
        self.role_selection_register = QComboBox(self.login_widget_2)
        self.role_selection_register.addItem("")
        self.role_selection_register.addItem("")
        self.role_selection_register.addItem("")
        self.role_selection_register.setObjectName(u"role_selection_register")
        self.role_selection_register.setGeometry(QRect(135, 200, 230, 30))
        self.role_selection_register.setFont(font3)
        self.role_selection_register.setStyleSheet(u"background-color: rgb(97, 97, 97);\n"
"color: rgb(255, 255, 255);")
        self.new_user_back_button = QPushButton(self.login_widget_2)
        self.new_user_back_button.setObjectName(u"new_user_back_button")
        self.new_user_back_button.setGeometry(QRect(10, 10, 75, 28))
        self.new_user_back_button.setMinimumSize(QSize(75, 28))
        self.new_user_back_button.setMaximumSize(QSize(16777215, 30))
        self.new_user_back_button.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(70, 70, 70);")

        self.horizontalLayout_11.addWidget(self.login_widget_2)

        StackedWidget.addWidget(self.new_user_registration)
        self.password_changing = QWidget()
        self.password_changing.setObjectName(u"password_changing")
        self.horizontalLayout_12 = QHBoxLayout(self.password_changing)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.login_widget_3 = QWidget(self.password_changing)
        self.login_widget_3.setObjectName(u"login_widget_3")
        self.login_widget_3.setMinimumSize(QSize(500, 300))
        self.login_widget_3.setMaximumSize(QSize(500, 300))
        self.login_widget_3.setStyleSheet(u"background-color: rgb(48, 48, 48);")
        self.password_label_3 = QLabel(self.login_widget_3)
        self.password_label_3.setObjectName(u"password_label_3")
        self.password_label_3.setGeometry(QRect(135, 110, 100, 16))
        self.password_label_3.setFont(font1)
        self.password_label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.change_password_confirm_button = QPushButton(self.login_widget_3)
        self.change_password_confirm_button.setObjectName(u"change_password_confirm_button")
        self.change_password_confirm_button.setGeometry(QRect(195, 250, 110, 32))
        self.change_password_confirm_button.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(70, 70, 70);")
        self.change_password_input = QLineEdit(self.login_widget_3)
        self.change_password_input.setObjectName(u"change_password_input")
        self.change_password_input.setGeometry(QRect(135, 130, 230, 30))
        self.change_password_input.setFont(font3)
        self.change_password_input.setStyleSheet(u"background-color: rgb(97, 97, 97);\n"
"color: rgb(255, 255, 255);")
        self.change_password_back_button = QPushButton(self.login_widget_3)
        self.change_password_back_button.setObjectName(u"change_password_back_button")
        self.change_password_back_button.setGeometry(QRect(10, 10, 75, 28))
        self.change_password_back_button.setMinimumSize(QSize(75, 28))
        self.change_password_back_button.setMaximumSize(QSize(16777215, 30))
        self.change_password_back_button.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(70, 70, 70);")

        self.horizontalLayout_12.addWidget(self.login_widget_3)

        StackedWidget.addWidget(self.password_changing)

        self.retranslateUi(StackedWidget)

        StackedWidget.setCurrentIndex(5)
        self.tabWidget.setCurrentIndex(1)
        self.role_selection_register.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(StackedWidget)
    # setupUi

    def retranslateUi(self, StackedWidget):
        StackedWidget.setWindowTitle(QCoreApplication.translate("StackedWidget", u"Net Test", None))
        self.connection_label_2.setText(QCoreApplication.translate("StackedWidget", u"Connection details:", None))
        self.password_label.setText(QCoreApplication.translate("StackedWidget", u"Password:", None))
        self.username_label.setText(QCoreApplication.translate("StackedWidget", u"Username:", None))
        self.separator.setText(QCoreApplication.translate("StackedWidget", u":", None))
        self.login_button.setText(QCoreApplication.translate("StackedWidget", u"Login", None))
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings_tab), QCoreApplication.translate("StackedWidget", u"Settings", None))
        self.editor_logout.setText(QCoreApplication.translate("StackedWidget", u"Logout", None))
        self.clear_test.setText(QCoreApplication.translate("StackedWidget", u"Clear Test", None))
        self.load_test.setText(QCoreApplication.translate("StackedWidget", u"Load Test", None))
        self.save_test.setText(QCoreApplication.translate("StackedWidget", u"Save Test", None))
        self.editor_to_session_button.setText(QCoreApplication.translate("StackedWidget", u"History", None))
        self.host_test.setText(QCoreApplication.translate("StackedWidget", u"Host", None))
        self.student_session_dock.setWindowTitle(QCoreApplication.translate("StackedWidget", u"Sessions", None))
        self.session_selection_logout.setText(QCoreApplication.translate("StackedWidget", u"Logout", None))
        self.students_refresh_button.setText(QCoreApplication.translate("StackedWidget", u"Refresh", None))
        self.session_history_dock.setWindowTitle(QCoreApplication.translate("StackedWidget", u"Session history", None))
        self.session_history_logout.setText(QCoreApplication.translate("StackedWidget", u"Logout", None))
        self.session_to_editor_button.setText(QCoreApplication.translate("StackedWidget", u"Editor", None))
        self.session_history_refresh_button.setText(QCoreApplication.translate("StackedWidget", u"Refresh", None))
        self.label_3.setText(QCoreApplication.translate("StackedWidget", u"Question:", None))
        self.test_current_question_label.setText(QCoreApplication.translate("StackedWidget", u"0/0", None))
        self.test_timer_label.setText(QCoreApplication.translate("StackedWidget", u"Time remaining:", None))
        self.test_timer.setText(QCoreApplication.translate("StackedWidget", u"00:00:00", None))
        self.hosted_session_dock.setWindowTitle(QCoreApplication.translate("StackedWidget", u"Hosting session", None))
        self.hosted_session_refresh_button.setText(QCoreApplication.translate("StackedWidget", u"Refresh", None))
        self.end_session_button.setText(QCoreApplication.translate("StackedWidget", u"End session", None))
        self.cheating_resolve_button.setText(QCoreApplication.translate("StackedWidget", u"Continue", None))
        self.cheating_exit_button.setText(QCoreApplication.translate("StackedWidget", u"Exit", None))
        self.textBrowser.setHtml(QCoreApplication.translate("StackedWidget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">It seems you minimized the window while taking a test. The program considers this an attempt at cheating. Please ask the teacher who hosted this test to enter their password below:</p></body></html>", None))
        self.admin_panel_dock.setWindowTitle(QCoreApplication.translate("StackedWidget", u"Admin panel", None))
        self.admin_panel_logout.setText(QCoreApplication.translate("StackedWidget", u"Logout", None))
        self.admin_panel_refresh_button.setText(QCoreApplication.translate("StackedWidget", u"Refresh", None))
        self.register_user.setText(QCoreApplication.translate("StackedWidget", u"Register new user", None))
        self.connection_label_3.setText(QCoreApplication.translate("StackedWidget", u"Role:", None))
        self.password_label_2.setText(QCoreApplication.translate("StackedWidget", u"Password:", None))
        self.username_label_2.setText(QCoreApplication.translate("StackedWidget", u"Username:", None))
        self.register_confirm_button.setText(QCoreApplication.translate("StackedWidget", u"Register", None))
        self.role_selection_register.setItemText(0, QCoreApplication.translate("StackedWidget", u"student", None))
        self.role_selection_register.setItemText(1, QCoreApplication.translate("StackedWidget", u"teacher", None))
        self.role_selection_register.setItemText(2, QCoreApplication.translate("StackedWidget", u"admin", None))

        self.role_selection_register.setCurrentText(QCoreApplication.translate("StackedWidget", u"student", None))
        self.new_user_back_button.setText(QCoreApplication.translate("StackedWidget", u"Back", None))
        self.password_label_3.setText(QCoreApplication.translate("StackedWidget", u"New password:", None))
        self.change_password_confirm_button.setText(QCoreApplication.translate("StackedWidget", u"Set password", None))
        self.change_password_back_button.setText(QCoreApplication.translate("StackedWidget", u"Back", None))
    # retranslateUi

