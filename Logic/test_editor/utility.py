import sys
import re
import json
import requests
from PySide6.QtCore import Qt, QTime
from PySide6.QtWidgets import (QApplication, QMainWindow, QStackedWidget, QDialog, QDockWidget, QWidget, 
                               QVBoxLayout, QTextEdit, QCheckBox, QPlainTextEdit, QComboBox, QPushButton)
from PySide6.QtWidgets import QLabel, QPushButton, QFileDialog
from Logic.setup import question_count, main_window, error_dialog_ui, main_ui, dialog_window, get_index

worker = requests.Session()

def back_to_start():
    main_window.setCurrentIndex(0)

def launch_test_editor():
    #main_ui.dockWidget.setTitleBarWidget(QWidget(None))
    #title_bar = main_ui.dockWidget.titleBarWidget()
    main_window.setCurrentIndex(1)

def show_dialog(header: str, message: str):
    global dialog_window
    error_dialog_ui.setupUi(dialog_window)
    error_dialog_ui.header_label.setText(header)
    error_dialog_ui.description_label.setText(message)
    dialog_window.show()

def get_total_points(index):
    question = main_ui.test_area.itemAt(index).widget()
    total_points = question.findChildren(QPlainTextEdit, "total_points")[0].toPlainText()
    try:
        total_points = float(total_points)
        if total_points.is_integer() == True:
            total_points = int(total_points)
            if total_points >= 0:
                final = round(total_points, 1)
                return final
            else: 
                return None
        else:
            return None
    except:
        return None
    
def clean_the_slate():
    global question_count
    for i in reversed(range(main_ui.test_area.count())): 
        main_ui.test_area.itemAt(i).widget().setParent(None)
    main_ui.test_name.setPlainText("")
    main_ui.timeEdit.setTime(QTime(0, 0))
    question_count = 0