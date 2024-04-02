# This Python file uses the following encoding: utf-8
import sys
import re
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QStackedWidget, QDialog, QDockWidget, QWidget, 
                               QVBoxLayout)
import UI.applicationUi as applicationUi
import UI.errorDialog as errorDialog
import UI.questionSingleChoice as questionSingleChoice
import UI.choiceAnswer as choiceAnswer

answer_choices_count = 1
question_count = 0
index = 0
questions = []
answer_choice_ui = choiceAnswer.Ui_answer_choice()
single_choice_question_ui = questionSingleChoice.Ui_Form()
error_dialog_ui = errorDialog.Ui_dialog()
main_ui = applicationUi.Ui_StackedWidget()
app = QApplication(sys.argv)
test_editor_window = QDockWidget()
dialog_window = QDialog()
main_window = QStackedWidget()
main_ui.setupUi(main_window)

def student_name_validation(name: str):
    if re.fullmatch('[A-Za-z ]{2,25}', name) == None:
        return False
    return True

def validate_student_connection():
    name = main_ui.textEdit_name.toPlainText()
    connection_details = main_ui.textEdit_conn.toPlainText()
    print(student_name_validation(name))
    if student_name_validation(name) == False:
        show_error_dialog("Invalid name", "Name must include only latin letters and be between 2 and 25 characters")

#returns INDEXES of the checked answers
def get_right_answers_choice():
    correct_indexes = []
    question = main_ui.test_area.itemAt(index).widget()
    answer_area = question.findChildren(QVBoxLayout, "answers_area")[0]
    for i in range(answer_area.count()):
        marked_as_correct = answer_area.itemAt(i).widget().findChildren(QWidget, "is_right")[0].isChecked()
        if marked_as_correct:
            correct_indexes.append(i)
    if correct_indexes == []:
        return None
    else:
        return correct_indexes

def get_total_points_choice():
    question = main_ui.test_area.itemAt(index).widget()
    total_points = question.findChildren(QPlainTextEdit, "total_points")[0].toPlainText()
    try:
        total_points = float(total_points)
        if total_points.is_integer() == True:
            total_points = int(total_points)
            if total_points >= 0:
                final = round(total_points, 1)
                print(final)
                return final
            else: 
                return None
        else:
            return None
    except:
        return None


def check_blank_answers_choice():
    question = main_ui.test_area.itemAt(index).widget()
    answer_area = question.findChildren(QVBoxLayout, "answers_area")[0]
    for i in range(answer_area.count()):
        print(i)
        answer_text = answer_area.itemAt(i).widget().findChildren(QWidget, "answer_choice_edit")[0].toPlainText()
        if answer_text == "":
            return False
        if answer_text.isspace() == True:
            return False
    return True

def validate_question():
    try:
        if check_blank_answers_choice() == False:
            show_error_dialog("Remove blank answer", "All answers must be non-blank")
            return False
        if get_right_answers_choice() == None:
            show_error_dialog("No correct answer set", "For a question to be valid at least one right answer must exist")
            return False
        if get_total_points_choice() == None:
            show_error_dialog("Total points incorrect", "Total amount of points must be a positive whole number")
            return False
    except:
        return False
    
def generate_json_choice():
    get_right_answers_choice()
    return 2

def add_image():
    file_dialog = QFileDialog()
    file_dialog.setNameFilter("Images (*.png *.jpg *.bmp)")
    file_dialog.setViewMode(QFileDialog.Detail)
    if file_dialog.exec_():
        file_path = file_dialog.selectedFiles()[0]

def create_choice_question():
    global question_count
    question = QWidget()
    question_count = question_count + 1
    set_index()
    single_choice_question_ui.setupUi(question)
    question.setObjectName(f"question_{question_count}")
    question.winId
    single_choice_question_ui.validate_button.clicked.connect(validate_question)
    main_ui.test_area.addWidget(question)
    single_choice_question_ui.delete_button.clicked.connect(remove_question)
    single_choice_question_ui.add_answer_button.clicked.connect(add_answer_choice)
    single_choice_question_ui.remove_answer_button.clicked.connect(remove_answer_choice)
    main_ui.addSingleButton.setEnabled(False)
    single_choice_question_ui.remove_answer_button.setEnabled(False)
    add_image_button = QPushButton("Add an image")
    add_image_button.clicked.connect(add_image)
    main_ui.test_area.addWidget(add_image_button)

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

# Choice question answer add/remove functions

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
    answer_choice.setObjectName(f"answer_widget")
    item = main_ui.test_area.itemAt(index).widget()
    answer_area = item.findChildren(QVBoxLayout, "answers_area")[0]
    answer_area.addWidget(answer_choice)

#From here on out lay commands that change windows and stuff

def student_registration_toggle():
    main_window.setCurrentIndex(2)

def back_to_start():
    main_window.setCurrentIndex(0)

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