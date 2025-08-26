from Logic.test_editor.utility import show_dialog, worker
from Logic.test_editor.test_saving import assemble_test
from Logic.server_communication.user_handling import get_url
import ast

def start_session(test_id):
    url = get_url()

    test_getting_url = url + "/test/start_session"

    data = {"test_id": test_id}

    response = worker.get(url=test_getting_url, data=data)

    return response.json()

def end_session(run_id):
    url = get_url()

    test_getting_url = url + "/test/end_session"

    data = {"run_id": run_id}

    response = worker.patch(url=test_getting_url, data=data)

    return response.json()

def get_active_sessions():
    url = get_url()

    session_getting_url = url + "/test/sessions_active"

    response = worker.get(url=session_getting_url)

    return response.json()

def get_sessions():
    url = get_url()

    session_getting_url = url + "/test/sessions"

    response = worker.get(url=session_getting_url)

    return response.json()

def get_session(run_id):
    url = get_url()

    session_getting_url = url + "/test/session"

    data = {"run_id": run_id}

    response = worker.get(url=session_getting_url, data=data)

    return response.json()