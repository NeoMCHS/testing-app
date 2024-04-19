import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QStackedWidget, QDialog, QDockWidget, QWidget, 
                               QVBoxLayout, QTextEdit, QCheckBox, QPlainTextEdit, QComboBox, QPushButton)
from PySide6.QtWidgets import QLabel, QPushButton, QFileDialog
import Logic.UI.applicationUi as applicationUi
import Logic.UI.errorDialog as errorDialog
import Logic.UI.questionChoice as questionChoice
import Logic.UI.choiceAnswer as choiceAnswer
import Logic.UI.questionText as questionText

question_count = 0
index = 0
questions = []
text_question_ui = questionText.Ui_Form()
answer_choice_ui = choiceAnswer.Ui_Form()
single_choice_question_ui = questionChoice.Ui_Form()
error_dialog_ui = errorDialog.Ui_dialog()
main_ui = applicationUi.Ui_StackedWidget()
app = QApplication(sys.argv)
test_editor_window = QDockWidget()
dialog_window = QDialog()
main_window = QStackedWidget()
main_ui.setupUi(main_window)

def add_to_question_count():
    global question_count
    question_count = question_count + 1

def substract_from_question_count():
    global question_count
    question_count = question_count - 1

def force_set_index(forced_index):
    global index
    index = forced_index
    print(f"force setting index to {index}")

def set_index():
    global index
    index = question_count-1
    print(f"setting index to {index}")

def get_index():
    global index 
    return index