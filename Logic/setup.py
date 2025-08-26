import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QStackedWidget, QDialog, QDockWidget, QWidget, 
                               QVBoxLayout, QTextEdit, QCheckBox, QPlainTextEdit, QComboBox, QPushButton)
from PySide6.QtWidgets import QLabel, QPushButton, QFileDialog
#import Logic.UI.applicationUi as applicationUi
from Logic.UI.applicationUi import Ui_StackedWidget
import Logic.UI.errorDialog as errorDialog
import Logic.UI.questionChoice as questionChoice
import Logic.UI.choiceAnswer as choiceAnswer
import Logic.UI.questionText as questionText
import Logic.UI.loadDialog as loadDialod
import Logic.UI.loadChoice as loadChoice
import Logic.UI.hostChoice as hostChoice
import Logic.UI.sessionRecord as sessionRecord
import Logic.UI.sessionActive as sessionActive
import Logic.UI.choiceAnswerTest as choiceAnswerTest
import Logic.UI.questionChoiceTest as questionChoiceTest
import Logic.UI.questionTextTest as questionTextTest
import Logic.UI.answersForm as answersForm
import Logic.UI.sessionActiveHistory as sessionActiveHistory
import Logic.UI.sessionInactiveHistory as sessionInactiveHistory
import Logic.UI.userForm as userForm
from PySide6.QtCore import QEvent
from Logic.test_viewer.anti_cheat import *

app = QApplication(sys.argv)

class MainWindow(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_StackedWidget()
        self.ui.setupUi(self)  

    def changeEvent(self, event):
        if event.type() == QEvent.Type.WindowStateChange:
            if anti_cheat_status() == True:
                stop_anti_cheat()
                self.setCurrentIndex(6)
        super().changeEvent(event)

question_count = 0
index = 0
questions = []
load_dialog_ui = loadDialod.Ui_Dialog()
load_choice_ui = loadChoice.Ui_file_object()
host_choice_ui = hostChoice.Ui_file_object()
session_record_ui = sessionRecord.Ui_session_widget()
session_active_ui = sessionActive.Ui_sessionActive()
choice_question_test_ui = questionChoiceTest.Ui_choice_form_test()
choice_answer_test = choiceAnswerTest.Ui_Form()
text_question_test_ui = questionTextTest.Ui_Form()
answers_form_ui = answersForm.Ui_Form()
session_active_history_ui = sessionActiveHistory.Ui_Form()
session_inactive_history_ui = sessionInactiveHistory.Ui_Form()
user_form_ui = userForm.Ui_Form()
text_question_ui = questionText.Ui_Form()
answer_choice_ui = choiceAnswer.Ui_Form()
single_choice_question_ui = questionChoice.Ui_Form()
error_dialog_ui = errorDialog.Ui_dialog()
main_window = MainWindow()
main_ui = main_window.ui
test_editor_window = QDockWidget()
dialog_window = QDialog()

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