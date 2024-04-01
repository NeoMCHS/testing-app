#!/bin/zsh

cd /Users/fedya/Developer/testing_app
pyside6-uic applicationUi.ui -o applicationUi.py
pyside6-uic errorDialog.ui -o errorDialog.py
pyside6-uic questionSingleChoice.ui -o questionSingleChoice.py
pyside6-uic choiceAnswer.ui -o choiceAnswer.py