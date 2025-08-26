from Logic.setup import *
from Logic.test_editor.utility import show_dialog, clean_the_slate
from Logic.test_editor.choice_question_logic import load_choice_question
from Logic.test_editor.text_question_logic import load_text_question
from Logic.server_communication.session_handling import get_sessions, end_session
from Logic.server_communication.test_handling import get_test
from Logic.server_communication.answers_handling import get_answers
from Logic.server_communication.user_handling import get_username, get_users, delete_user, update_user_password, register_user
from functools import partial
import ast
from PySide6.QtCore import Qt, QTime
from PySide6.QtWidgets import (QApplication, QMainWindow, QStackedWidget, QDialog, QDockWidget, QWidget, 
                               QVBoxLayout, QTextEdit, QCheckBox, QPlainTextEdit, QComboBox, QPushButton)

def refresh_users():
    for i in reversed(range(main_ui.registered_users_area.count())): 
        main_ui.registered_users_area.itemAt(i).widget().setParent(None)
    users = get_users()
    for user in users:
        name, role, user_id = user[1], user[3], user[0]
        user_to_load = QWidget()
        user_form_ui.setupUi(user_to_load)
        user_form_ui.username_field.setText(name)
        user_form_ui.role_field.setText(role)
        user_form_ui.delete_user_button.clicked.connect(partial(delete_user_function, user_id))
        user_form_ui.set_new_password_button.clicked.connect(partial(set_new_password, user_id))
        main_ui.registered_users_area.addWidget(user_to_load)

def delete_user_function(user_id):
    response = delete_user(user_id)
    if response == 'success':
        refresh_users()
        show_dialog("Success", "Successfully deleted user.")

def set_new_password(user_id):
    main_window.setCurrentIndex(9)
    main_ui.change_password_confirm_button.clicked.connect(lambda: confirm_new_password(user_id))

def confirm_new_password(user_id):
    password = main_ui.change_password_input.text()
    response = update_user_password(user_id, password)
    if response == 'success':
        main_window.setCurrentIndex(7)
        show_dialog("Success", "New password was successfully set.")
    else:
        show_dialog("Failure", "Something went wrong, new password has not been set.")
    main_ui.change_password_input.setText('')

def register_new_user():
    main_window.setCurrentIndex(8)
    main_ui.register_confirm_button.clicked.connect(submit_new_user)

def submit_new_user():
    username = main_ui.username_input_register.toPlainText()
    password = main_ui.password_input_register.text()
    role = main_ui.role_selection_register.currentText()
    if not(username == ''):
        response = register_user(password=password, username=username, role=role)
        main_ui.username_input_register.setText('')
        main_ui.password_input_register.setText('')
        main_window.setCurrentIndex(7)
        refresh_users()