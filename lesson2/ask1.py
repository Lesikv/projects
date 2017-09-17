#!usr/bin/env python
#coding: utf8

from answers import get_answer


def ask_user():
    question = input("Введите вопрос: ")
    return question

new_question = ask_user()

try:
    while new_question != "Пока":
        print(get_answer(new_question)) 
        new_question = ask_user()
    print("И тебе пока")
except KeyboardInterrupt:
    print("До новых встреч!")
#while ask_user() != "Пока":
   # print(get_answer(ask_user))
    #print(get_answer(ask_user))
    #if ask_user == "Пока":
      #  break


