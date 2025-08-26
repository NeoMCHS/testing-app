from Logic.test_editor.utility import show_dialog, clean_the_slate, worker
from Logic.setup import question_count, main_window, error_dialog_ui, main_ui, dialog_window, get_index, main_window, main_ui

def login():
    global url
    username = main_ui.username_input.toPlainText()
    password = main_ui.password_input.text()
    ip = main_ui.ip_input.toPlainText()
    port = main_ui.port_input.toPlainText()

    url = "http://" + ip + ":" + port

    auth_url = url + "/auth/login"

    data = {"username": username, "password": password}

    try:
        response = worker.post(url=auth_url, data=data)

        response = response.json()
    except:
        response = "The connection details you provided were innacurate"

    if response in ['admin', 'student', 'teacher']:
        if response == 'student':
            main_window.setCurrentIndex(2)
        if response == 'teacher':
            main_window.setCurrentIndex(1)
        if response == 'admin':
            main_window.setCurrentIndex(7)
        main_ui.password_input.setText('')
        main_ui.username_input.setText('')
    else:
        show_dialog("Login error", response)

def get_url():
    return url

def get_username(user_id):
    url = get_url()

    username_url = url + "/user/username"

    data = {"target_id": user_id}

    response = worker.get(url=username_url, data=data)

    return response.json()

def check_password(target_id, password):
    url = get_url()

    username_url = url + "/user/check_password"

    data = {"target_id": target_id, "password": password}

    response = worker.get(url=username_url, data=data)

    return response.json()

def register_user(password, username, role):
    url = get_url()

    reqister_url = url + "/auth/register"

    data = {"username": username, "password": password, "role": role}

    print(data)

    response = worker.post(url=reqister_url, data=data)

    print(response.json())

    return response.json()

def delete_user(user_id):
    url = get_url()

    delete_user_url = url + "/auth/delete"

    data = {"user_id": user_id}

    response = worker.delete(url=delete_user_url, data=data)

    return response.json()

def get_users():
    url = get_url()

    user_getting_url = url + "/user/users"

    response = worker.get(url=user_getting_url)

    return response.json()

def update_user_password(user_id, password):
    url = get_url()

    password_updating_url = url + "/auth/update_password"

    data = {"target_id": user_id, "password": password}

    response = worker.patch(url=password_updating_url, data=data)

    return response.json()

def get_author(test_id):
    url = get_url()

    author_getting_url = url + "/test/author"

    data = {"test_id": test_id}

    response = worker.get(url=author_getting_url, data=data)

    return response.json()