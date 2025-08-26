from Logic.test_editor.utility import show_dialog, worker
from Logic.test_editor.test_saving import assemble_test
from Logic.server_communication.user_handling import get_url
import ast

def save_test():
    test = assemble_test()

    url = get_url()

    test_saving_url = url + "/test/save"

    response = worker.post(url=test_saving_url, json=test)

    response = response.json()

    if response == 'success':
        show_dialog("Success", "You successfully saved the test")
    else:
        show_dialog("Encountered an error while saving", response)

def delete_test_request(test_id):
    url = get_url()

    test_deleting_url = url + "/test/delete"

    data = {"test_id": test_id}

    response = worker.delete(url=test_deleting_url, data=data)

    return response.json()

def load_tests_list():
    url = get_url()

    test_getting_url = url + "/test/tests"

    response = worker.get(url=test_getting_url)

    return response.json()

def get_test(test_id):
    url = get_url()

    test_getting_url = url + "/test/load"

    data = {"test_id": test_id}

    response = worker.get(url=test_getting_url, data=data)

    test_obj = ast.literal_eval((response.json()[0]))

    return test_obj