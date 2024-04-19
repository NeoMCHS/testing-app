import sys
import re
import json
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QStackedWidget, QDialog, QDockWidget, QWidget, 
                               QVBoxLayout, QTextEdit, QCheckBox, QPlainTextEdit, QComboBox, QPushButton)
from PySide6.QtWidgets import QLabel, QPushButton, QFileDialog
from Logic.setup import (question_count, set_index, force_set_index, single_choice_question_ui, answer_choice_ui, 
                         add_to_question_count, substract_from_question_count, get_index)
from Logic.test_editor.editing_logic import (create_edit_button_target, disable_question_editing, allow_editing_of_other_questions, 
update_edit_buttons_on_delete)
from Logic.test_editor.utility import *

class ValidationPushButton(QPushButton):
    def __init__(self, name):
        super().__init__(name)

    def mousePressEvent(self, pos):
        target = self.parent().parent()
        for i in range(main_ui.test_area.count()):
            if main_ui.test_area.itemAt(i).widget() == target:
                validate_function_choice(i)
                print("hit")

class DeletePushButton(QPushButton):
    def __init__(self, name):
        super().__init__(name)

    def mousePressEvent(self, pos):
        target = self.parent().parent()
        for i in range(main_ui.test_area.count()):
            if main_ui.test_area.itemAt(i).widget() == target:
                remove_question()
                print("hit")

class AddAnswerPushButton(QPushButton):
    def __init__(self, name):
        super().__init__(name)

    def mousePressEvent(self, pos):
        target = self.parent().parent()
        for i in range(main_ui.test_area.count()):
            if main_ui.test_area.itemAt(i).widget() == target:
                if main_ui.test_area.itemAt(i).widget().findChildren(QVBoxLayout, "answers_area")[0].count() == 1:
                    main_ui.test_area.itemAt(i).widget().findChildren(QPushButton, "remove_answer_button")[0].setEnabled(True)
                if main_ui.test_area.itemAt(i).widget().findChildren(QVBoxLayout, "answers_area")[0].count() == 5:
                    self.setEnabled(False)
                add_answer_choice()
                print("hit")

class RemoveAnwerPushButton(QPushButton):
    def __init__(self, name):
        super().__init__(name)
        self.setEnabled(False)

    def mousePressEvent(self, pos):
        target = self.parent().parent()
        for i in range(main_ui.test_area.count()):
            if main_ui.test_area.itemAt(i).widget() == target:
                if main_ui.test_area.itemAt(i).widget().findChildren(QVBoxLayout, "answers_area")[0].count() == 2:
                    self.setEnabled(False)
                    main_ui.test_area.itemAt(i).widget().findChildren(QPushButton, "add_answer_button")[0].setEnabled(True)
                if main_ui.test_area.itemAt(i).widget().findChildren(QVBoxLayout, "answers_area")[0].count() <= 6:
                    main_ui.test_area.itemAt(i).widget().findChildren(QPushButton, "add_answer_button")[0].setEnabled(True)
                remove_answer_choice()
                print("hit")

def get_right_answers_choice():
    index = get_index()
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

def get_answers_choice():
    index = get_index()
    answers = []
    question = main_ui.test_area.itemAt(index).widget()
    answer_area = question.findChildren(QVBoxLayout, "answers_area")[0]
    for i in range(answer_area.count()):
        answer = answer_area.itemAt(i).widget().findChildren(QPlainTextEdit, "answer_choice_edit")[0].toPlainText()
        answers.append(answer)
    return answers

def get_points_destribution_choice():
    index = get_index()
    question = main_ui.test_area.itemAt(index).widget()
    point_destribution_index = question.findChildren(QComboBox, "point_destribution")[0].currentIndex()
    if point_destribution_index == 0:
        return "split"
    elif point_destribution_index == 1:
        return "concentrate"
    
def check_answers_choice():
    index = get_index()
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

def validate_question_choice():
    if check_blank_question() == False:
        show_error_dialog("There is no question", "You should probably write the question before trying to submit it")
        return False
    if check_answers_choice() == False:
        return False
    if get_right_answers_choice() == None:
        show_error_dialog("No correct answer set", "For a question to be valid at least one right answer must exist")
        return False
    if get_total_points() == None:
        show_error_dialog("Total points incorrect", "Total amount of points must be a positive whole number")
        return False
    return True

def validate_function_choice(target):
    if validate_question_choice() == True:
        generate_json_choice(target)
        create_edit_button_target(target)
        disable_question_editing()
        allow_editing_of_other_questions()

def generate_json_choice(target):
    force_set_index(target)
    index = get_index()
    correct_answers_indexes = get_right_answers_choice()
    answers = get_answers_choice()
    print(answers)
    json_answers = []
    for answer_index in range(len(answers)):
        answer = answers[answer_index]
        if answer_index in correct_answers_indexes:
            is_correct = True
        else: 
            is_correct = False
        dict = {'content': answer, 'isCorrect': is_correct}
        json_answers.append(dict)
        print(dict)
    question = main_ui.test_area.itemAt(index).widget()
    question_text = question.findChildren(QTextEdit, "question_text_field")[0].toPlainText()
    point_distrbution = get_points_destribution_choice()
    total_points = get_total_points()
    final_obj = json.dumps({"question": question_text, "points_destribution": point_distrbution, "total_point": total_points, "answers": json_answers})
    print(final_obj)

def create_choice_question():
    global question_count
    question = QWidget()
    add_to_question_count()
    print(question_count)
    set_index()
    index = get_index()
    single_choice_question_ui.setupUi(question)
    question.setObjectName(f"choice_question")
    delete_button = DeletePushButton("delete_button")
    delete_button.setStyleSheet("background-color: rgb(255, 0, 0); color: rgb(0, 0, 0);")
    delete_button.setText("Delete")
    single_choice_question_ui.bottom_bar_layout.addWidget(delete_button)
    remove_answer_button = RemoveAnwerPushButton("remove_answer_button")
    remove_answer_button.setStyleSheet("background-color: rgb(97, 97, 97);")
    remove_answer_button.setObjectName("remove_answer_button")
    remove_answer_button.setText("Remove answer")
    single_choice_question_ui.bottom_bar_layout.addWidget(remove_answer_button)
    add_answer_button = AddAnswerPushButton("add_answer_button")
    add_answer_button.setStyleSheet("background-color: rgb(97, 97, 97);")
    add_answer_button.setObjectName("add_answer_button")
    add_answer_button.setText("Add answer")
    single_choice_question_ui.bottom_bar_layout.addWidget(add_answer_button)
    validation_button = ValidationPushButton("validation_button")
    validation_button.setStyleSheet("background-color: rgb(86, 73, 255); color: rgb(255, 255, 255);")
    validation_button.setText("Validate")
    single_choice_question_ui.bottom_bar_layout.addWidget(validation_button)
    #single_choice_question_ui.validate_button.clicked.connect(lambda: validate_function_choice(index))
    main_ui.test_area.addWidget(question)
    #single_choice_question_ui.delete_button.clicked.connect(remove_question)
    main_ui.addTextQuestion.setEnabled(False)
    main_ui.addSingleButton.setEnabled(False)
    add_image_button = QPushButton("Add an image")
    add_image_button.clicked.connect(add_image)
    add_image_button.setObjectName("add_image_button")
    print(index)
    question = main_ui.test_area.itemAt(index).widget()
    print(index)
    question.findChildren(QVBoxLayout, "question_area")[0].addWidget(add_image_button)

def remove_answer_choice():
    index = get_index()
    item = main_ui.test_area.itemAt(index).widget()
    answer_area = item.findChildren(QVBoxLayout, "answers_area")[0]
    target_index = answer_area.count()-1
    target_answer = answer_area.itemAt(target_index).widget()
    target_answer.setParent(None)

def add_answer_choice():
    index = get_index()
    item = main_ui.test_area.itemAt(index).widget()
    answer_area = item.findChildren(QVBoxLayout, "answers_area")[0]
    answer_choice = QWidget()
    answer_choice_ui.setupUi(answer_choice)
    answer_choice.setObjectName(f"answer_widget")
    answer_area.addWidget(answer_choice)

def remove_question():
    index = get_index()
    global question_count
    #print(str(question_count)+" -> "+str(question_count - 1))
    substract_from_question_count()
    item = main_ui.test_area.itemAt(index).widget()
    item.setParent(None)
    main_ui.addSingleButton.setEnabled(True)
    main_ui.addTextQuestion.setEnabled(True)
    update_edit_buttons_on_delete()
    #main_ui.test_area.removeItem(item)

def check_blank_question():
    index = get_index()
    question = main_ui.test_area.itemAt(index).widget()
    question_text = question.findChildren(QTextEdit, "question_text_field")[0].toPlainText()
    if question_text == "":
        return False
    if question_text.isspace() == True:
        return False
    return True

def add_image():
    #TODO convert the image into a datastring that can be displayed using HTML. You can use base64 module to do that
    #Also you need to make sure that only ONE image is added to any question. As for the UI component you need to 
    #make the button change if an image is successfuly added. Think of a way to display the added image. 
    file_dialog = QFileDialog()
    file_dialog.setNameFilter("Images (*.png *.jpg *.bmp)")
    file_dialog.setViewMode(QFileDialog.Detail)
    if file_dialog.exec():
        file_path = file_dialog.selectedFiles()[0]