# This Python file uses the following encoding: utf-8
import sys
import re
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QStackedWidget, QDialog, QDockWidget, QWidget, 
                               QVBoxLayout)
import applicationUi
import errorDialog
import questionSingleChoice
import choiceAnswer

answer_choices_count = 1
question_count = 0
index = 0
questions = []
answer_choice_ui = choiceAnswer.Ui_Form()
single_choice_question_ui = questionSingleChoice.Ui_Form()
error_dialog_ui = errorDialog.Ui_dialog()
main_ui = applicationUi.Ui_StackedWidget()
app = QApplication(sys.argv)
test_editor_window = QDockWidget()
dialog_window = QDialog()
main_window = QStackedWidget()
main_ui.setupUi(main_window)

def student_name_validation(name: str):
    if re.fullmatch('[A-Za-z]{2,25}', name) == None:
        return False
    return True

def back_to_start():
    main_window.setCurrentIndex(0)

def validate_student_connection():
    name = main_ui.textEdit_name.toPlainText()
    connection_details = main_ui.textEdit_conn.toPlainText()
    print(student_name_validation(name))
    if student_name_validation(name) == False:
        show_error_dialog("Invalid name", "Name must include only latin letters and be between 2 and 25 characters")

def generate_json_choice_question():
    return 2

def validate_question():
    return 0

def create_choice_question():
    global question_count
    question = QWidget()
    #print(str(question_count)+" -> "+str(question_count + 1))
    question_count = question_count + 1
    single_choice_question_ui.setupUi(question)
    question.setObjectName(f"question_{question_count}")
    question.winId
    single_choice_question_ui.validate_button.clicked.connect(back_to_start)
    main_ui.test_area.addWidget(question)
    single_choice_question_ui.delete_button.clicked.connect(set_index)
    single_choice_question_ui.delete_button.clicked.connect(remove_question)
    single_choice_question_ui.add_answer_button.clicked.connect(set_index)
    single_choice_question_ui.add_answer_button.clicked.connect(add_answer_choice)
    single_choice_question_ui.remove_answer_button.clicked.connect(set_index)
    single_choice_question_ui.remove_answer_button.clicked.connect(remove_answer_choice)
    main_ui.addSingleButton.setEnabled(False)
    single_choice_question_ui.remove_answer_button.setEnabled(False)

def remove_question():
    global index
    global question_count
    global answer_choices_count
    #print(str(question_count)+" -> "+str(question_count - 1))
    question_count = question_count - 1
    item = main_ui.test_area.itemAt(index).widget()
    item.deleteLater()
    answer_choices_count = 1
    main_ui.addSingleButton.setEnabled(True)
    #main_ui.test_area.removeItem(item)

def set_index():
    global index
    index = question_count-1

def remove_answer_choice():
    global index
    global answer_choices_count
    #print(str(answer_choices_count)+" -> "+str(answer_choices_count - 1))
    answer_choices_count = answer_choices_count - 1
    if answer_choices_count == 1:
        single_choice_question_ui.remove_answer_button.setEnabled(False)
        single_choice_question_ui.add_answer_button.setEnabled(True)
    item = main_ui.test_area.itemAt(index).widget()
    answer_area = item.findChildren(QVBoxLayout, "answers_area")[0]
    target_index = answer_area.count()-1
    target_answer = answer_area.itemAt(target_index).widget()
    target_answer.deleteLater()    

def add_answer_choice():
    global index
    global answer_choices_count
    #print(str(answer_choices_count)+" -> "+str(answer_choices_count + 1))
    answer_choices_count = answer_choices_count + 1
    if answer_choices_count > 1:
        single_choice_question_ui.remove_answer_button.setEnabled(True)
    if answer_choices_count > 5:
        single_choice_question_ui.add_answer_button.setEnabled(False)
    answer_choice = QWidget()
    answer_choice_ui.setupUi(answer_choice)
    item = main_ui.test_area.itemAt(index).widget()
    answer_area = item.findChildren(QVBoxLayout, "answers_area")[0]
    answer_area.addWidget(answer_choice)

#From here on out lay commands that change windows and stuff

def student_registration_toggle():
    main_window.setCurrentIndex(2)

def launch_test_editor():
    #main_ui.dockWidget.setTitleBarWidget(QWidget(None))
    title_bar = main_ui.dockWidget.titleBarWidget()
    main_window.setCurrentIndex(1)

def show_error_dialog(header: str, message: str):
    global dialog_window
    error_dialog_ui.setupUi(dialog_window)
    error_dialog_ui.header_label.setText(header)
    error_dialog_ui.description_label.setText(message)
    dialog_window.show()
    print("ooga booga")

main_ui.addSingleButton.clicked.connect(create_choice_question)
main_ui.teacher_button.clicked.connect(launch_test_editor)
main_ui.submit_button.clicked.connect(validate_student_connection)
main_ui.student_button.clicked.connect(student_registration_toggle)
main_ui.back_button_student.clicked.connect(back_to_start)
main_ui.back_button_editor.clicked.connect(back_to_start)

if __name__ == "__main__":
    main_window.show()
    main_window.setCurrentIndex(0)
    app.exec()
    sys.exit()