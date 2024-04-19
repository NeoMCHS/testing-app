import sys
import re
import json
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QStackedWidget, QDialog, QDockWidget, QWidget, 
                               QVBoxLayout, QTextEdit, QCheckBox, QPlainTextEdit, QComboBox, QPushButton)
from Logic.setup import *
from Logic.test_editor.choice_question_logic import create_choice_question
from Logic.test_editor.editing_logic import block_editing_of_other_questions
from Logic.test_editor.text_question_logic import create_text_question
from Logic.test_editor.utility import student_registration_toggle, back_to_start, launch_test_editor


def setup_app():
    main_window.show()
    main_window.setCurrentIndex(0)      
    main_ui.addSingleButton.clicked.connect(create_choice_question)
    main_ui.addTextQuestion.clicked.connect(create_text_question) 
    main_ui.addSingleButton.clicked.connect(lambda: block_editing_of_other_questions())
    main_ui.addTextQuestion.clicked.connect(lambda: block_editing_of_other_questions())
    main_ui.student_button.clicked.connect(student_registration_toggle)
    main_ui.back_button_student.clicked.connect(back_to_start)
    main_ui.back_button_editor.clicked.connect(back_to_start)
    main_ui.teacher_button.clicked.connect(launch_test_editor)
