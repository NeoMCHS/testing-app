# This Python file uses the following encoding: utf-8
import sys
import re
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QDialog, QDockWidget, QWidget
import applicationUi
import errorDialog

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

#From here on out lay commands that change windows and stuff

def student_registration_toggle():
    main_window.setCurrentIndex(2)

def launch_test_editor():
    main_ui.dockWidget.setTitleBarWidget(QWidget(None))
    main_window.setCurrentIndex(1)

def show_error_dialog(header: str, message: str):
    global dialog_window
    error_dialog_ui.setupUi(dialog_window)
    error_dialog_ui.header_label.setText(header)
    error_dialog_ui.description_label.setText(message)
    dialog_window.show()
    print("ooga booga")

main_ui.teacher_button.clicked.connect(launch_test_editor)
main_ui.submit_button.clicked.connect(validate_student_connection)
main_ui.student_button.clicked.connect(student_registration_toggle)
main_ui.back_button.clicked.connect(back_to_start)

if __name__ == "__main__":
    main_window.show()
    main_window.setCurrentIndex(0)
    app.exec()
    sys.exit(app.exec())