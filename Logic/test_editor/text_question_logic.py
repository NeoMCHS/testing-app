import sys
import re
import json
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QStackedWidget, QDialog, QDockWidget, QWidget, 
                               QVBoxLayout, QTextEdit, QCheckBox, QPlainTextEdit, QComboBox, QPushButton)
from PySide6.QtWidgets import QLabel, QPushButton, QFileDialog
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from Logic.setup import (text_question_ui, set_index, force_set_index, question_count, add_to_question_count,
                        substract_from_question_count, get_index)
from Logic.test_editor.editing_logic import *
from Logic.test_editor.utility import *

class ValidationPushButton(QPushButton):
    def __init__(self, name):
        super().__init__(name)

    def mousePressEvent(self, pos):
        target = self.parent().parent()
        for i in range(main_ui.test_area.count()):
            print(i)
            if main_ui.test_area.itemAt(i).widget() == target:
                validate_function_text()
                print("hit")

class DeletePushButton(QPushButton):
    def __init__(self, name):
        super().__init__(name)

    def mousePressEvent(self, pos):
        target = self.parent().parent()
        for i in range(main_ui.test_area.count()):
            print(i)
            if main_ui.test_area.itemAt(i).widget() == target:
                remove_question()
                print("hit")

def find_index(e):
    print(e)
    for i in range(main_ui.test_area.count()):
        question = main_ui.test_area.itemAt(i).widget()
        print(question)
        button = question.childAt(e)
        print(button)
        print('button',main_ui.test_area.indexOf(button))

def get_right_answers_text():
    index = get_index()
    correct_answers = []
    question = main_ui.test_area.itemAt(index).widget()
    answers_raw = question.findChildren(QTextEdit, "text_answers")[0].toPlainText()
    return answers_raw.split(",")

def check_blank_question():
    index = get_index()
    question = main_ui.test_area.itemAt(index).widget()
    question_text = question.findChildren(QTextEdit, "question_text_field")[0].toPlainText()
    if question_text == "":
        return False
    if question_text.isspace() == True:
        return False
    return True

def check_answers_text():
    global index
    index = get_index()
    question = main_ui.test_area.itemAt(index).widget()
    answers = question.findChildren(QTextEdit, "text_answers")[0].toPlainText()
    print(answers)
    print(answers.isspace())
    if answers.isspace() == True:
        return False
    elif answers == "":
        return False
    else:
        return True
    
def validate_question_text():
    if check_blank_question() == False:
        show_error_dialog("There is no question", "You should probably write the question before trying to submit it")
        return False
    if check_answers_text() == False:
        show_error_dialog("No correct answer set", "For a question to be valid at least one right answer must exist")
        return False
    if get_total_points() == None:
        show_error_dialog("Total points incorrect", "Total amount of points must be a positive whole number")
        return False
    return True

def validate_function_text():
    target = get_index()
    if validate_question_text() == True:
        generate_json_text(target)
        create_edit_button_target(target)
        disable_question_editing()
        allow_editing_of_other_questions()

def generate_json_text(target):
    force_set_index(target)
    index = get_index()
    answers = get_right_answers_text()
    question = main_ui.test_area.itemAt(index).widget()
    question_text = question.findChildren(QTextEdit, "question_text_field")[0].toPlainText()
    total_points = get_total_points()
    json_answers = []
    for answer in answers:
        dict = {'content': answer, 'isCorrect': True}
        json_answers.append(dict)
    final_obj = json.dumps({"question": question_text, "points_destribution": "text_question", "total_point": total_points, "answers": json_answers})
    print(final_obj)
    return final_obj

def create_text_question():
    global question_count
    question = QWidget()
    add_to_question_count()
    set_index()
    index = get_index()
    main_ui.test_area.addWidget(question)
    text_question_ui.setupUi(question)
    question.setObjectName("text_question")
    delete_button = DeletePushButton("delete_button")
    delete_button.setStyleSheet("background-color: rgb(255, 0, 0); color: rgb(0, 0, 0);")
    delete_button.setText("Delete")
    text_question_ui.bottom_bar_layout.addWidget(delete_button)
    validation_button = ValidationPushButton("validation_button")
    validation_button.setStyleSheet("background-color: rgb(86, 73, 255); color: rgb(255, 255, 255);")
    validation_button.setText("Validate")
    text_question_ui.bottom_bar_layout.addWidget(validation_button)
    main_ui.addTextQuestion.setEnabled(False)
    main_ui.addSingleButton.setEnabled(False)
    add_image_button = QPushButton("Add an image")
    add_image_button.clicked.connect(add_image)
    add_image_button.setObjectName("add_image_button")
    question = main_ui.test_area.itemAt(index).widget()
    question.findChildren(QVBoxLayout, "question_area")[0].addWidget(add_image_button)

def remove_question():
    global index
    global question_count
    index = get_index()
    #print(str(question_count)+" -> "+str(question_count - 1))
    substract_from_question_count()
    item = main_ui.test_area.itemAt(index).widget()
    item.setParent(None)
    main_ui.addSingleButton.setEnabled(True)
    main_ui.addTextQuestion.setEnabled(True)
    update_edit_buttons_on_delete()
    #main_ui.test_area.removeItem(item)

def add_image():
    #TODO convert the image into a datastring that can be displayed using HTML. You can use base64 module to do that
    #Also you need to make sure that only ONE image is added to any question. As for the UI component you need to 
    #make the button change if an image is successfuly added. Think of a way to display the added image. 
    file_dialog = QFileDialog()
    file_dialog.setNameFilter("Images (*.png *.jpg *.bmp)")
    file_dialog.setViewMode(QFileDialog.Detail)
    if file_dialog.exec():
        file_path = file_dialog.selectedFiles()[0]