# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget
import startScreenUi

ui = startScreenUi.Ui_StackedWidget()
app = QApplication(sys.argv)
window = QStackedWidget()
ui.setupUi(window)

def student_registration():
    window.setCurrentIndex(1)
    print(ui.pushButton_2.text())

ui.pushButton_2.clicked.connect(student_registration)

if __name__ == "__main__":
    window.show()
    app.exec()
    sys.exit(app.exec())
