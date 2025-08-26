from Logic.test_editor.utility import show_dialog, worker
from Logic.test_editor.test_saving import assemble_test
from Logic.server_communication.user_handling import get_url
import ast

def submit_answers(score, run_id, answers):
    url = get_url()

    answer_writing_url = url + "/test/answer"

    data = {"score": score, "run_id": run_id, 'answers': str(answers)}

    response = worker.post(url=answer_writing_url, data=data)

    return response.json()

def get_answers(run_id):
    url = get_url()

    answer_getting_url = url + "/test/answers"

    data = {"run_id": run_id}

    response = worker.get(url=answer_getting_url, data=data)

    return response.json()