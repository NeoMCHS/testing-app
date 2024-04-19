import sys
import re
import json
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QStackedWidget, QDialog, QDockWidget, QWidget, 
                               QVBoxLayout, QTextEdit, QCheckBox, QPlainTextEdit, QComboBox, QPushButton)
import UI.applicationUi as applicationUi
import UI.errorDialog as errorDialog
import UI.questionChoice as questionChoice
import UI.choiceAnswer as choiceAnswer
import UI.questionText as questionText
from PySide6.QtWidgets import QLabel, QPushButton, QFileDialog
from Logic.app import main_ui
from Logic.test_editor.utility import show_error_dialog

def student_name_validation(name: str):
    if re.fullmatch('[A-Za-z ]{2,25}', name) == None:
        return False
    return True

def validate_student_connection():
    name = main_ui.textEdit_name.toPlainText()
    connection_details = main_ui.textEdit_conn.toPlainText()
    if student_name_validation(name) == False:
        show_error_dialog("Invalid name", "Name must include only latin letters and be between 2 and 25 characters")

main_ui.submit_button.clicked.connect(validate_student_connection)