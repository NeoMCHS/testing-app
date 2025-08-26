from Logic.setup import *
from Logic.test_editor.choice_question_logic import create_choice_question
from Logic.test_editor.editing_logic import block_editing_of_other_questions
from Logic.test_editor.text_question_logic import create_text_question
from Logic.test_editor.utility import back_to_start, launch_test_editor, clean_the_slate
from Logic.server_communication.test_handling import save_test
from Logic.test_editor.test_loading import loading_dialog
from Logic.server_communication.user_handling import login
from Logic.test_editor.test_hosting import hosting_dialog
from Logic.test_viewer.test_taking import refresh_sessions_active, cheating_exit, cheating_continue
from Logic.test_editor.test_archiving import refresh_sessions_history
from Logic.admin.admin_logic import *
import Logic.UI.applicationUi as Ui_StackedWidget
from PySide6 import QtWidgets
import socket
import os
import atexit

def setup_app():
    main_window.show()
    main_window.setCurrentIndex(0) 
    main_ui.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
    main_ui.cheating_trigger_password_input.setEchoMode(QtWidgets.QLineEdit.Password)
    main_ui.addSingleButton.clicked.connect(create_choice_question)
    main_ui.addTextQuestion.clicked.connect(create_text_question) 
    main_ui.addSingleButton.clicked.connect(lambda: block_editing_of_other_questions())
    main_ui.addTextQuestion.clicked.connect(lambda: block_editing_of_other_questions())
    main_ui.save_test.clicked.connect(save_test)
    main_ui.load_test.clicked.connect(loading_dialog)
    main_ui.host_test.clicked.connect(hosting_dialog)
    main_ui.save_test.setEnabled(False)
    main_ui.clear_test.clicked.connect(clean_the_slate)
    #main_ui.host_test.clicked.connect(host_test)
    main_ui.login_button.clicked.connect(login)
    main_ui.editor_to_session_button.clicked.connect(lambda: main_window.setCurrentIndex(3))
    main_ui.session_to_editor_button.clicked.connect(lambda: main_window.setCurrentIndex(1))
    main_ui.session_selection_logout.clicked.connect(lambda: main_window.setCurrentIndex(0))
    main_ui.admin_panel_logout.clicked.connect(lambda: main_window.setCurrentIndex(0))
    main_ui.change_password_back_button.clicked.connect(lambda: main_window.setCurrentIndex(7))
    main_ui.new_user_back_button.clicked.connect(lambda: main_window.setCurrentIndex(7))
    main_ui.editor_logout.clicked.connect(lambda: main_window.setCurrentIndex(0))
    main_ui.session_history_logout.clicked.connect(lambda: main_window.setCurrentIndex(0))
    main_ui.students_refresh_button.clicked.connect(refresh_sessions_active)
    main_ui.cheating_exit_button.clicked.connect(cheating_exit)
    main_ui.cheating_resolve_button.clicked.connect(cheating_continue)
    main_ui.session_history_refresh_button.clicked.connect(refresh_sessions_history)
    main_ui.admin_panel_refresh_button.clicked.connect(refresh_users)
    main_ui.register_user.clicked.connect(register_new_user)