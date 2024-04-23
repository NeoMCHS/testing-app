from Logic.setup import *
from Logic.test_editor.choice_question_logic import create_choice_question
from Logic.test_editor.editing_logic import block_editing_of_other_questions
from Logic.test_editor.text_question_logic import create_text_question
from Logic.test_editor.utility import student_registration_toggle, back_to_start, launch_test_editor
from Logic.test_editor.test_settings_logic import assemble_test

def setup_app():
    main_window.show()
    main_window.setCurrentIndex(0)  
    main_ui.addSingleButton.clicked.connect(create_choice_question)
    main_ui.addTextQuestion.clicked.connect(create_text_question) 
    main_ui.addSingleButton.clicked.connect(lambda: block_editing_of_other_questions())
    main_ui.addTextQuestion.clicked.connect(lambda: block_editing_of_other_questions())
    main_ui.student_button.clicked.connect(student_registration_toggle)
    main_ui.back_button_student.clicked.connect(back_to_start)
    main_ui.back_button_editor.clicked.connect(back_to_start)
    main_ui.teacher_button.clicked.connect(launch_test_editor)
    main_ui.test_validation.clicked.connect(assemble_test)
