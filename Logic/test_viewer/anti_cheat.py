taking_test = False

def start_anti_cheat():
    global taking_test
    taking_test = True

def stop_anti_cheat():
    global taking_test
    taking_test = False

def anti_cheat_status():
    global taking_test
    return taking_test