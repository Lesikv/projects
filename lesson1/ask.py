#!usr/bin/env python
#coding: utf8

from answers import get_answer


def ask_user():
    answer = input("Как дела?")
    return answer

new_answer = ask_user()


while new_answer != "Хорошо":
    new_answer = ask_user()
print("Ну наконец-то!")

