from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QStackedWidget, QDialog, QDockWidget, QWidget, 
                               QVBoxLayout, QTextEdit, QCheckBox, QPlainTextEdit, QComboBox, QPushButton)
from PySide6.QtWidgets import QLabel, QPushButton, QFileDialog
from Logic.setup import question_count, main_window, error_dialog_ui, main_ui, force_set_index, get_index

def update_edit_buttons_on_delete():
    for i in range(main_ui.test_area.count()):
        print(i)
        remove_edit_button_target(i)
        create_edit_button_target(i)

def add_edit_buttons_to_others(exception):
    for i in range(main_ui.test_area.count()):
        if i == exception:
            pass
        else:
            question = main_ui.test_area.itemAt(i).widget()
            if bool(question.findChildren(QPushButton, "edit_button")) == False:
                create_edit_button_target(i)
                disable_question_editing_target(i)

def block_editing_of_other_questions():
    for i in range(main_ui.test_area.count()):
        question = main_ui.test_area.itemAt(i).widget()
        if bool(question.findChildren(QPushButton, "edit_button")) == True:
            question.findChildren(QPushButton, "edit_button")[0].setEnabled(False)
        disable_question_creation()

def allow_editing_of_other_questions():
    for i in range(main_ui.test_area.count()):
        question = main_ui.test_area.itemAt(i).widget()
        if bool(question.findChildren(QPushButton, "edit_button")) == True:
            question.findChildren(QPushButton, "edit_button")[0].setEnabled(True)
        enable_question_creation()

def create_edit_button_target(target):
    question = main_ui.test_area.itemAt(target).widget()
    if bool(question.findChildren(QPushButton, "edit_button")) == True:
        return True
    print(f"creating edit button with target at {target}")
    edit_button = QPushButton()
    edit_button.setObjectName("edit_button")
    edit_button.setStyleSheet("background-color: rgb(86, 73, 255); color: rgb(255, 255, 255);")
    edit_button.setText("Edit")
    place = question.findChildren(QVBoxLayout, "question_area")[0]
    place.addWidget(edit_button)
    edit_button.clicked.connect(lambda: force_set_index(target))
    edit_button.clicked.connect(enable_question_editing)
    #edit_button.clicked.connect(remove_edit_button)
    edit_button.clicked.connect(lambda: add_edit_buttons_to_others(target))
    edit_button.clicked.connect(lambda: block_editing_of_other_questions())
    edit_button.clicked.connect(remove_edit_button)

def create_edit_button():
    index = get_index()
    print(f"creating edit button at {index}")
    question = main_ui.test_area.itemAt(index).widget()
    edit_button = QPushButton()
    edit_button.setObjectName("edit_button")
    edit_button.setStyleSheet("background-color: rgb(86, 73, 255); color: rgb(255, 255, 255);")
    edit_button.setText("Edit")
    place = question.findChildren(QVBoxLayout, "question_area")[0]
    place.addWidget(edit_button)
    current_index = index
    edit_button.clicked.connect(lambda: force_set_index(current_index))
    edit_button.clicked.connect(lambda: enable_question_editing())
    edit_button.clicked.connect(lambda: remove_edit_button())
    edit_button.clicked.connect(lambda: add_edit_buttons_to_others(current_index))
    edit_button.clicked.connect(lambda: block_editing_of_other_questions())

def remove_edit_button():
    index = get_index()
    question = main_ui.test_area.itemAt(index).widget()
    edit_button = question.findChildren(QPushButton, "edit_button")[0]
    edit_button.setParent(None)

def remove_edit_button_target(target):
    question = main_ui.test_area.itemAt(target).widget()
    edit_button = question.findChildren(QPushButton, "edit_button")[0]
    edit_button.setParent(None)

def disable_question_creation():
    main_ui.save_test.setEnabled(False)
    main_ui.addSingleButton.setEnabled(False)
    main_ui.addTextQuestion.setEnabled(False)

def enable_question_creation():
    main_ui.save_test.setEnabled(True)
    main_ui.addSingleButton.setEnabled(True)
    main_ui.addTextQuestion.setEnabled(True)

def disable_question_editing_target(target):
    question = main_ui.test_area.itemAt(target).widget()
    for PushButton in question.findChildren(QPushButton):
        if PushButton.objectName() == "edit_button":
            pass
        else:
            PushButton.setEnabled(False)
    for ComboBox in question.findChildren(QComboBox):
        ComboBox.setEnabled(False)
    for TextEdit in question.findChildren(QTextEdit):
        TextEdit.setEnabled(False)
    for PlainTextEdit in question.findChildren(QPlainTextEdit):
        PlainTextEdit.setEnabled(False)
    answer_area = question.findChildren(QVBoxLayout, "answers_area")[0]
    for i in range(answer_area.count()):
        answer_area.itemAt(i).widget().setEnabled(False)
    #question.setMinimumHeight(question.geometry().height())
    #question.setMaximumHeight(question.geometry().height())

def disable_question_editing():
    index = get_index()
    question = main_ui.test_area.itemAt(index).widget()
    for PushButton in question.findChildren(QPushButton):
        if PushButton.objectName() == "edit_button":
            pass
        else:
            PushButton.setEnabled(False)
    for ComboBox in question.findChildren(QComboBox):
        ComboBox.setEnabled(False)
    for TextEdit in question.findChildren(QTextEdit):
        TextEdit.setEnabled(False)
    for PlainTextEdit in question.findChildren(QPlainTextEdit):
        PlainTextEdit.setEnabled(False)
    #question.findChildren(QPushButton, "delete_button")[0].setEnabled(False)
    #question.findChildren(QPushButton, "remove_answer_button")[0].setEnabled(False)
    #question.findChildren(QPushButton, "add_answer_button")[0].setEnabled(False)
    #question.findChildren(QPushButton, "validate_button")[0].setEnabled(False)
    #question.findChildren(QComboBox, "point_destribution")[0].setEnabled(False)
    #question.findChildren(QPushButton, "add_image_button")[0].setEnabled(False)
    #question.findChildren(QTextEdit, "question_text_field")[0].setEnabled(False)
    #question.findChildren(QPlainTextEdit, "total_points")[0].setEnabled(False)
    try:
        answer_area = question.findChildren(QVBoxLayout, "answers_area")[0]
        for i in range(answer_area.count()):
            answer_area.itemAt(i).widget().setEnabled(False)
        question.setMinimumHeight(question.geometry().height())
        question.setMaximumHeight(question.geometry().height())
    except:
        question.setMinimumHeight(question.geometry().height())
        question.setMaximumHeight(question.geometry().height())

def enable_question_editing():
    index = get_index()
    print(f"enabling editing for {index}")
    question = main_ui.test_area.itemAt(index).widget()
    for PushButton in question.findChildren(QPushButton):
        if PushButton.objectName() == "edit_button":
            pass
        else:
            PushButton.setEnabled(True)
    for ComboBox in question.findChildren(QComboBox):
        ComboBox.setEnabled(True)
    for TextEdit in question.findChildren(QTextEdit):
        TextEdit.setEnabled(True)
    for PlainTextEdit in question.findChildren(QPlainTextEdit):
        PlainTextEdit.setEnabled(True)
    try:
        answer_area = question.findChildren(QVBoxLayout, "answers_area")[0]
        for i in range(answer_area.count()):
            answer_area.itemAt(i).widget().setEnabled(True)
        #question.setMinimumHeight(question.geometry().height())
        #question.setMaximumHeight(1500000)
    except:
        a = 1
        #question.setMinimumHeight(question.geometry().height())
        #question.setMaximumHeight(1500000)