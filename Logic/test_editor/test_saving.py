from PySide6.QtGui import QInputMethodEvent
from Logic.setup import *
from Logic.test_editor.choice_question_logic import generate_json_choice
from Logic.test_editor.text_question_logic import generate_json_text
from Logic.test_editor.utility import show_dialog, worker
import json
import requests
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QStackedWidget, QDialog, QDockWidget, QWidget, 
                               QVBoxLayout, QTextEdit, QCheckBox, QPlainTextEdit, QComboBox, QPushButton)
from PySide6.QtWidgets import QLabel, QPushButton, QFileDialog

def assemble_test():
    minutes, hours = read_time()
    name = read_name()
    questions = generate_question_jsons()
    dict = {"time_hours": hours, "time_minutes": minutes, "name": name, "questions": questions}
    final_obj = dict
    #show_dialog("yo", str(final_obj))
    return final_obj

def generate_question_jsons():
    json_question_list = []
    for i in range(main_ui.test_area.count()):
        question = main_ui.test_area.itemAt(i).widget()
        if question.findChildren(QPushButton, "add_answer_button") == []:
            question_obj = json.loads(generate_json_text(i))
        else:
            question_obj = json.loads(generate_json_choice(i))
        json_question_list.append(question_obj)
    return json_question_list

def read_time():
    minutes = main_ui.timeEdit.time().toPython().minute
    hours = main_ui.timeEdit.time().toPython().hour
    if hours == 0 and minutes == 0:
        show_dialog("Please set time limits", "You can set the time in the settings tab of the editor. Please note the the time format is HH:MM.")
        return None
    return minutes, hours

def read_name():
    name = main_ui.test_name.toPlainText()
    if name == "":
        show_dialog("Please name the test", "You can name the test in the settings tab of the editor.")
        return None
    return name