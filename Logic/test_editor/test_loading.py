from Logic.setup import *
from Logic.test_editor.utility import show_dialog, clean_the_slate, worker, question_count
from Logic.test_editor.choice_question_logic import load_choice_question
from Logic.test_editor.text_question_logic import load_text_question
from Logic.server_communication.test_handling import load_tests_list, get_test, delete_test_request
from functools import partial
import ast
from os import listdir
from os.path import isfile, join
from Logic.setup import (load_choice_ui, load_dialog_ui)
from PySide6.QtCore import Qt, QTime
from PySide6.QtWidgets import (QApplication, QMainWindow, QStackedWidget, QDialog, QDockWidget, QWidget, 
                               QVBoxLayout, QTextEdit, QCheckBox, QPlainTextEdit, QComboBox, QPushButton)

def load_test(test_id):
    global question_count
    clean_the_slate()
    test = get_test(test_id)
    hours, minutes, name, questions = test['time_hours'], test['time_minutes'], test['name'], test['questions']
    load_setting(hours, minutes, name)
    for i in range(len(questions)):
        question_count += 1
        question = questions[i]
        question = list(question.values())
        title, points_destribution, points_total, answers = question[0], question[1], question[2], question[3]
        if points_destribution == "text_question":
            load_text_question(i, title, points_total, answers)
        else:
            load_choice_question(i, title, points_destribution, points_total, answers)    

def load_setting(hours, minutes, name):
    main_ui.test_name.setPlainText(name)
    main_ui.timeEdit.setTime(QTime(int(hours), int(minutes)))

def delete_test(test_id, index):
    response = delete_test_request(test_id)
    if response == 'success':
        item = load_dialog_ui.file_layout.itemAt(index+1).widget()
        item.setParent(None)

def loading_dialog():
    loading_dialog = QDialog()
    tests = load_tests_list()
    load_dialog_ui.setupUi(loading_dialog)
    for i in range(len(tests)):
        test = tests[i]
        name = ast.literal_eval(test[3])['name']
        test_id = test[0]
        test_to_load = QWidget()
        load_choice_ui.setupUi(test_to_load)
        load_choice_ui.name.setText(f"{name}")
        load_choice_ui.confirm_button.clicked.connect(partial(load_test, test_id))
        load_choice_ui.delete_button.clicked.connect(partial(delete_test, test_id, i))
        load_dialog_ui.file_layout.addWidget(test_to_load)

    loading_dialog.exec_()