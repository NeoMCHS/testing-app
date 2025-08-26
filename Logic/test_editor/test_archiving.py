from Logic.setup import *
from Logic.test_editor.utility import show_dialog, clean_the_slate, worker
from Logic.test_editor.choice_question_logic import load_choice_question
from Logic.test_editor.text_question_logic import load_text_question
from Logic.server_communication.session_handling import get_sessions, end_session
from Logic.server_communication.test_handling import get_test
from Logic.server_communication.answers_handling import get_answers
from Logic.server_communication.user_handling import get_username
from functools import partial
import ast
from Logic.setup import (session_active_history_ui, session_inactive_history_ui, answers_form_ui)
from PySide6.QtCore import Qt, QTime
from PySide6.QtWidgets import (QApplication, QMainWindow, QStackedWidget, QDialog, QDockWidget, QWidget, 
                               QVBoxLayout, QTextEdit, QCheckBox, QPlainTextEdit, QComboBox, QPushButton)

def refresh_sessions_history():
    for i in reversed(range(main_ui.session_history_area.count())): 
        main_ui.session_history_area.itemAt(i).widget().setParent(None)
    sessions = get_sessions()
    for session in sessions:
        run_id, test_id, date, active = session[0], session[1], session[3], session[2]
        test = get_test(test_id)
        title = test['name']
        session_to_load = QWidget()
        if active == 1:
            session_active_history_ui.setupUi(session_to_load)
            session_active_history_ui.test_title.setText(title)
            session_active_history_ui.date_started_hosting.setText(date)
            session_active_history_ui.end_session_button.clicked.connect(partial(end_hosting, run_id))
        if active == 0:
            session_inactive_history_ui.setupUi(session_to_load)
            session_inactive_history_ui.test_title.setText(title)
            session_inactive_history_ui.date_started_hosting.setText(date)
            session_inactive_history_ui.session_show_responses_button.clicked.connect(partial(refresh_answers_history, run_id))
        main_ui.session_history_area.addWidget(session_to_load)

def end_hosting(run_id):    
    response = end_session(run_id)
    if response == 'success':
        refresh_sessions_history()

def refresh_answers_history(run_id):
    for i in reversed(range(main_ui.session_history_area.count())): 
        main_ui.session_history_area.itemAt(i).widget().setParent(None)
    answers = get_answers(run_id)
    print(answers)
    for answer in answers:
        answer_to_load = QWidget()
        submitter_id = answer[1]
        submitter = get_username(submitter_id)
        print(submitter)
        answers_form_ui.setupUi(answer_to_load)
        answers_form_ui.student_name.setText(submitter)
        answers_form_ui.score.setText(answer[4])
        print(ast.literal_eval((answer[5])))
        answers_form_ui.show_answers_button.clicked.connect(partial(show_student_answers_history, ast.literal_eval((answer[5]))))
        main_ui.session_history_area.addWidget(answer_to_load)

def show_student_answers_history(answers):
    formatted_answers = ""
    for i in range(len(answers)):
        answer = answers[i]
        unlisted_answers = ''
        for elemment in answer:
            unlisted_answers = unlisted_answers + elemment + " "
        formatted_answers = formatted_answers + str(i+1) + ": " + unlisted_answers + '\n'
    show_dialog("Answers provided by this student", formatted_answers)