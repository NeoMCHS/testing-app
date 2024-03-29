# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
import ui_mainwindow

ui = ui_mainwindow.Ui_MainWindow()
app = QApplication(sys.argv)
window = QMainWindow()
ui.setupUi(window)

def student_registration():
    ui.stackedWidget.setCurrentIndex(1)
    print(ui.student_button.text())

ui.student_button.clicked.connect(student_registration)

if __name__ == "__main__":
    window.show()
    app.exec()
    sys.exit(app.exec())
