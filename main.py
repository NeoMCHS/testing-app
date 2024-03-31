# This Python file uses the following encoding: utf-8
import sys
import re
import time
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QDialog
import startScreenUi
import errorDialog

error_dialog_ui = errorDialog.Ui_dialog()
start_window_ui = startScreenUi.Ui_StackedWidget()
app = QApplication(sys.argv)
dialog_window = QDialog()
window = QStackedWidget()
start_window_ui.setupUi(window)

def student_name_validation(name: str):
    if re.fullmatch('[A-Za-z]{2,25}', name) == None:
        return False
    return True

def student_registration_toggle():
    window.setCurrentIndex(1)

def back_to_start():
    window.setCurrentIndex(0)

def validate_student_connection():
    name = start_window_ui.textEdit_name.toPlainText()
    connection_details = start_window_ui.textEdit_conn.toPlainText()
    print(student_name_validation(name))
    if student_name_validation(name) == False:
        show_error_dialog("Invalid name", "Name must include only latin letters and be between 2 and 25 characters")

def show_error_dialog(header: str, message: str):
    global dialog_window
    error_dialog_ui.setupUi(dialog_window)
    error_dialog_ui.header_label.setText(header)
    error_dialog_ui.description_label.setText(message)
    dialog_window.show()
    print("ooga booga")

start_window_ui.submit_button.clicked.connect(validate_student_connection)
start_window_ui.student_button.clicked.connect(student_registration_toggle)
start_window_ui.back_button.clicked.connect(back_to_start)

if __name__ == "__main__":
    window.show()
    window.setCurrentIndex(0)
    app.exec()
    sys.exit(app.exec())
