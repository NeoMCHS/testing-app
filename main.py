# This Python file uses the following encoding: utf-8
import sys
import re
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget
import startScreenUi

ui = startScreenUi.Ui_StackedWidget()
app = QApplication(sys.argv)
window = QStackedWidget()
ui.setupUi(window)

def student_name_validation(name: str):
    if re.fullmatch(r"[a-zA-Z]{2, 20}", name):
        return True
    return False

def student_registration_toggle():
    window.setCurrentIndex(1)

def back_to_start():
    window.setCurrentIndex(0)

def validate_student_connection():
    name = ui.textEdit_name.toPlainText()
    connection_details = ui.textEdit_conn.toPlainText()

ui.submit_button.clicked.connect(validate_student_connection)
ui.student_button.clicked.connect(student_registration_toggle)
ui.back_button.clicked.connect(back_to_start)

if __name__ == "__main__":
    window.show()
    window.setCurrentIndex(0)
    app.exec()
    sys.exit(app.exec())
