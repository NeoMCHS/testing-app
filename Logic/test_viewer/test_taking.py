from Logic.setup import *
from Logic.test_editor.utility import show_dialog, worker
from Logic.test_editor.choice_question_logic import load_choice_question
from Logic.test_editor.text_question_logic import load_text_question
from Logic.server_communication.test_handling import get_test
from Logic.server_communication.session_handling import get_active_sessions, get_session
from Logic.server_communication.user_handling import get_username, check_password, get_author
from Logic.server_communication.answers_handling import submit_answers
from Logic.test_viewer.anti_cheat import *
from functools import partial
from collections import Counter
from Logic.setup import (session_active_ui)
from PySide6.QtCore import Qt, QTime, QTimer, QEvent
from PySide6.QtWidgets import (QApplication, QMainWindow, QStackedWidget, QDialog, QDockWidget, QWidget, 
                               QVBoxLayout, QTextEdit, QCheckBox, QPlainTextEdit, QComboBox, QPushButton)

def refresh_sessions_active():
    for i in reversed(range(main_ui.student_session_area.count())): 
        main_ui.student_session_area.itemAt(i).widget().setParent(None)
    sessions = get_active_sessions()
    for session in sessions:
        run_id, test_id = session[0], session[1]
        test = get_test(test_id)
        author_name = get_author(test_id)[0]
        title = test['name']
        session_to_load = QWidget()
        session_active_ui.setupUi(session_to_load)
        session_active_ui.test_title.setText(title)
        session_active_ui.tester_username.setText(author_name)
        session_active_ui.session_join_button.clicked.connect(partial(take_test, run_id, test))
        main_ui.student_session_area.addWidget(session_to_load)

timer = QTimer()
timer.setInterval(1000)

current_session = None

def take_test(run_id, test):
    global current_session
    global timer
    session = get_session(run_id)
    current_session = run_id
    if session[2] == 1:
        hours, minutes, questions = test['time_hours'], test['time_minutes'], test['questions']
        finish_time = hours*60*60+minutes*60
        timer.timeout.connect(partial(countdown, timer, finish_time))
        main_ui.test_current_question_label.setText(f"1/{len(questions)}")
        start_timer()
        load_questions(questions)
        main_window.showFullScreen()
        main_window.setCurrentIndex(4)
        start_anti_cheat()
    else: 
        show_dialog("This session is inactive", "It seems you tried joining inactive session. Please refresh the list to see what session are currently active.")

time = QTime(00,00,00)

def countdown(timer, finish_time):
    global time
    time = time.addSecs(-1)
    remaining_time = time.addSecs(finish_time)
    main_ui.test_timer.setText(remaining_time.toString("hh:mm:ss"))    
    if remaining_time.toString("hh:mm:ss") == "00:00:00":
        timer.stop()
        submit_test()
        exit_test()
        stop_anti_cheat()

def stop_timer():
    global timer
    timer.stop()

def start_timer():
    global timer
    timer.start()

def load_questions(questions):
    for i in range(len(questions)):
        question = questions[i]
        if question['points_destribution'] == "text_question":
            setup_text_quesiton(i, question)
        else:
            setup_choice_quesiton(i, question)
        
def setup_choice_quesiton(place, question):
    quesiton_to_load = QWidget()
    choice_question_test_ui.setupUi(quesiton_to_load)
    choice_question_test_ui.question_text.setText(question['question'])
    answers = question['answers']
    for i in range(len(answers)):
        answer = answers[i]
        answer_to_load = QWidget()
        choice_answer_test.setupUi(answer_to_load)
        choice_answer_test.answer_text.setText(answer['content'])
        choice_question_test_ui.choice_answers_area.addWidget(answer_to_load)
    choice_question_test_ui.submit_answer.clicked.connect(partial(validate_choice, place))
    main_ui.test_questions_area.insertWidget(place, quesiton_to_load)

def setup_text_quesiton(place, question):
    quesiton_to_load = QWidget()
    text_question_test_ui.setupUi(quesiton_to_load)
    text_question_test_ui.question_text.setText(question['question'])
    main_ui.test_questions_area.insertWidget(place, quesiton_to_load)
    text_question_test_ui.submit_answer.clicked.connect(partial(validate_text, place))

student_answers = []

def validate_choice(target):
    global student_answers
    question = main_ui.test_questions_area.widget(target)
    answers = question.findChildren(QVBoxLayout, 'choice_answers_area')[0]
    chosen = []
    for i in range(answers.count()):
        marked_as_correct = answers.itemAt(i).widget().findChildren(QWidget, "is_chosen")[0].isChecked()
        if marked_as_correct == True:
            chosen.append(answers.itemAt(i).widget().findChildren(QWidget, "answer_text")[0].text())
    if len(chosen) == 0:
        show_dialog("No answers chosen", "Please choose an answer")
    else:
        student_answers.append(chosen)
        if target+1 == main_ui.test_questions_area.count():
            submit_test()
        else:
            print(student_answers)
            main_ui.test_current_question_label.setText(f"{target+2}/{main_ui.test_questions_area.count()}")
            main_ui.test_questions_area.setCurrentIndex(target+1)

def validate_text(target):
    global student_answers
    question = main_ui.test_questions_area.widget(target)
    answer = question.findChildren(QTextEdit, 'answer_input')[0]
    chosen = []
    if answer.toPlainText() == '':
        show_dialog("No answer entered", "Please enter an answer")
    else:
        chosen.append(answer.toPlainText())
        student_answers.append(chosen)
        if target+1 == main_ui.test_questions_area.count():
            submit_test()
        else:
            main_ui.test_current_question_label.setText(f"{target+2}/{main_ui.test_questions_area.count()}")
            main_ui.test_questions_area.setCurrentIndex(target+1)

def calculate_score(test, student_answers):
    student_total_points = 0
    total_possible_points = 0
    correct_answers = []
    question_type = []
    total_points = []
    questions = test['questions']
    for question in questions:
        question_correct = []
        answers = question['answers']
        for answer in answers:
            if answer['isCorrect'] == True:
                question_correct.append(answer['content'])
        correct_answers.append(question_correct)
        question_type.append(question['points_destribution'])
        total_points.append(question['total_point'])
    for points in total_points:
        total_possible_points += points
    for i in range(len(correct_answers)):
        try:
            student = student_answers[i]
        except: 
            break
        correct = correct_answers[i]
        type = question_type[i]
        points = total_points[i]
        student_correct_answers = len(list((Counter(student) & Counter(correct)).elements()))
        if type == 'text_question':
            if student_correct_answers > 0:
                student_total_points += points
        elif type == 'concentrate':
            if student_correct_answers >= 1 and len(student) == student_correct_answers:
                student_total_points += points
        elif type == 'split':
            if student_correct_answers == len(correct) and len(student) == len(correct):
                student_total_points += points
#            elif student_correct_answers > len(correct) and student_correct_answers > 0:
#                student_total_points += round(points*((student_correct_answers - len(correct))/len(correct)))
#            elif student_correct_answers < len(correct) and student_correct_answers > 0:
#                student_total_points += round(points*((len(correct) - student_correct_answers)/len(correct)))

    final_score = f"{student_total_points}/{total_possible_points}"
    final_percentage = round((student_total_points/total_possible_points)*100)

    final_score = f"{student_total_points}/{total_possible_points} ({final_percentage}%)"

    print(final_score)

    return final_score

def submit_test():
    global student_answers
    global current_session
    session = get_session(current_session)
    test = get_test(session[1])
    score = calculate_score(test, student_answers)
    response = submit_answers(score, current_session, student_answers)
    if response == 'success':
        show_dialog("Answers submitted", "Your answers were submitted successfully!")
        exit_test()
        stop_anti_cheat()
    else:
        show_dialog("Something went wrong", "Something went wrong when submitting your answers. Restart the test please!")
        exit_test()
    main_window.showNormal()
    main_window.setCurrentIndex(2)

def exit_test():
    global student_answers
    global timer
    global time
    student_answers = []
    while main_ui.test_questions_area.count() > 0:
        widget = main_ui.test_questions_area.widget(0)
        main_ui.test_questions_area.removeWidget(widget)
        widget.setParent(None)
    timer.stop()
    timer.timeout.disconnect()
    time = QTime(00,00,00)

def cheating_exit():
    exit_test()
    main_window.setCurrentIndex(2)
    main_ui.cheating_trigger_password_input.setText('')

def cheating_continue():
    global current_session
    password = main_ui.cheating_trigger_password_input.text()
    session = get_session(current_session)
    test_id = session[1]
    tester_id = get_author(test_id)[1]
    check = check_password(tester_id, password)
    if check == 'success':
        main_window.showFullScreen()
        main_window.setCurrentIndex(4)
        start_anti_cheat()
        main_ui.cheating_trigger_password_input.setText('')
    else:
        show_dialog("Please try again", "Incorrect password")
        main_ui.cheating_trigger_password_input.setText('')