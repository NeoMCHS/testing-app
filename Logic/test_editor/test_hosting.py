from Logic.setup import *
from Logic.test_editor.utility import show_dialog, clean_the_slate, worker
from Logic.test_editor.choice_question_logic import load_choice_question
from Logic.test_editor.text_question_logic import load_text_question
from Logic.server_communication.test_handling import load_tests_list, get_test
from Logic.server_communication.session_handling import  start_session, end_session, get_session
from Logic.server_communication.answers_handling import  get_answers
from Logic.server_communication.user_handling import get_username
from functools import partial
import ast
from Logic.setup import (host_choice_ui, load_dialog_ui, answers_form_ui)
from PySide6.QtCore import Qt, QTime
from PySide6.QtWidgets import (QApplication, QMainWindow, QStackedWidget, QDialog, QDockWidget, QWidget, 
                               QVBoxLayout, QTextEdit, QCheckBox, QPlainTextEdit, QComboBox, QPushButton)

def host_test(test_id):
    clean_the_slate()
    test = get_test(test_id)
    name = test['name']
    run_id = start_session(test_id)
    if isinstance(run_id, int) == True:
        main_window.setCurrentIndex(5)
        main_ui.end_session_button.clicked.connect(lambda: end_hosting(run_id))
        main_ui.hosted_session_refresh_button.clicked.connect(lambda: refresh_answers(run_id))

def end_hosting(run_id):    
    response = end_session(run_id)
    if response == 'success':
        main_window.setCurrentIndex(1)

def hosting_dialog():
    hosting_dialog = QDialog()
    tests = load_tests_list()
    load_dialog_ui.setupUi(hosting_dialog)
    for i in range(len(tests)):
        test = tests[i]
        name = ast.literal_eval(test[3])['name']
        test_id = test[0]
        test_to_load = QWidget()
        host_choice_ui.setupUi(test_to_load)
        host_choice_ui.name.setText(f"{name}")
        host_choice_ui.host_button.clicked.connect(partial(host_test, test_id))
        load_dialog_ui.file_layout.addWidget(test_to_load)

    hosting_dialog.exec_()

def refresh_answers(run_id):
    for i in reversed(range(main_ui.hosted_session_answers_area.count())): 
        main_ui.hosted_session_answers_area.itemAt(i).widget().setParent(None)
    answers = get_answers(run_id)
    for answer in answers:
        answer_to_load = QWidget()
        submitter_id = answer[1]
        submitter = get_username(submitter_id)
        answers_form_ui.setupUi(answer_to_load)
        answers_form_ui.student_name.setText(submitter)
        answers_form_ui.score.setText(answer[4])
        print(ast.literal_eval((answer[5])))
        answers_form_ui.show_answers_button.clicked.connect(partial(show_student_answers, ast.literal_eval((answer[5]))))
        main_ui.hosted_session_answers_area.addWidget(answer_to_load)

def show_student_answers(answers):
    formatted_answers = ""
    for i in range(len(answers)):
        answer = answers[i]
        unlisted_answers = ''
        for elemment in answer:
            unlisted_answers = unlisted_answers + elemment + " "
        formatted_answers = formatted_answers + str(i+1) + ": " + unlisted_answers + '\n'
    show_dialog("Answers provided by this student", formatted_answers)