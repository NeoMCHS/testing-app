# This Python file uses the following encoding: utf-8
import sys
import re
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QStackedWidget, QDialog, QDockWidget, QWidget, 
                               QVBoxLayout, QTextEdit, QCheckBox, QPlainTextEdit, QComboBox, QPushButton)
import UI.applicationUi as applicationUi
import UI.errorDialog as errorDialog
import UI.questionSingleChoice as questionSingleChoice
import UI.choiceAnswer as choiceAnswer
from PySide6.QtWidgets import QLabel, QPushButton, QFileDialog

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

def get_points_destribution_choice():
    question = main_ui.test_area.itemAt(index).widget()
    point_destribution_index = question.findChildren(QComboBox, "point_destribution")[0].currentIndex()
    if point_destribution_index == 0:
        return "split"
    elif point_destribution_index == 1:
        return "concentrate"

def get_total_points_choice():
    question = main_ui.test_area.itemAt(index).widget()
    total_points = question.findChildren(QPlainTextEdit, "total_points")[0].toPlainText()
    try:
        total_points = float(total_points)
        if total_points.is_integer() == True:
            total_points = int(total_points)
            if total_points >= 0:
                final = round(total_points, 1)
                return final
            else: 
                return None
        else:
            return None
    except:
        return None

def check_blank_question_choice():
    question = main_ui.test_area.itemAt(index).widget()
    question_text = question.findChildren(QTextEdit, "question_text_field")[0].toPlainText()
    if question_text == "":
        return False
    if question_text.isspace() == True:
        return False
    return True

def check_answers_choice():
    question = main_ui.test_area.itemAt(index).widget()
    answer_area = question.findChildren(QVBoxLayout, "answers_area")[0]
    if answer_area.count() == 1:
        show_error_dialog("Only one answer choice present", "This question wouldn't be very challenging")
        return False
    for i in range(answer_area.count()):
        answer_text = answer_area.itemAt(i).widget().findChildren(QWidget, "answer_choice_edit")[0].toPlainText()
        if answer_text == "":
            show_error_dialog("Remove blank answer", "All answers must be non-blank")
            return False
        if answer_text.isspace() == True:
            show_error_dialog("Remove blank answer", "All answers must be non-blank")
            return False
    return True

def validate_question():
    if check_blank_question_choice() == False:
        show_error_dialog("There is no question", "You should probably write the question before trying to submit it")
        return False
    if check_answers_choice() == False:
        return False
    if get_right_answers_choice() == None:
        show_error_dialog("No correct answer set", "For a question to be valid at least one right answer must exist")
        return False
    if get_total_points_choice() == None:
        show_error_dialog("Total points incorrect", "Total amount of points must be a positive whole number")
        return False
    toggle_question_finished()
    
def toggle_question_finished():
    #TODO make sure that the drop down menu is getting locked. Make sure that add image is getting locked
    #TODO create and connect a function to the edit button that will set the right index + make sure that no other questions are editable
    question = main_ui.test_area.itemAt(index).widget()
    button = QPushButton()
    button.setObjectName("edit_button")
    button.setStyleSheet("background-color: rgb(86, 73, 255); color: rgb(255, 255, 255);")
    button.setText("Edit")
    place = question.findChildren(QVBoxLayout, "question_area")[0]
    question.findChildren(QPushButton, "delete_button")[0].setEnabled(False)
    question.findChildren(QPushButton, "remove_answer_button")[0].setEnabled(False)
    question.findChildren(QPushButton, "add_answer_button")[0].setEnabled(False)
    question.findChildren(QPushButton, "validate_button")[0].setEnabled(False)
    place.addWidget(button)
    #question.setMinimumWidth(question.geometry().width())
    #question.setMaximumWidth(question.geometry().width())
    question.setMinimumHeight(question.geometry().height())
    question.setMaximumHeight(question.geometry().height())
    main_ui.addSingleButton.setEnabled(True)

def generate_json_choice():
    get_right_answers_choice()
    return 2

def add_image():
    file_dialog = QFileDialog()
    file_dialog.setNameFilter("Images (*.png *.jpg *.bmp)")
    file_dialog.setViewMode(QFileDialog.Detail)
    if file_dialog.exec():
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
    #TODO maybe add the add_image button to the question_area for estetics reasons (maybe)
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

def force_set_index(forced_index):
    global index
    index = forced_index
    print(f"force setting index to {index}")

def set_index():
    global index
    index = question_count-1
    print(f"setting index to {index}")

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