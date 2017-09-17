#!usr/bin/env python
#coding:utf8

def get_answer(question):
    answers = {"Привет" : "И тебе привет!", "Как дела?": "Лучше всех", "Пока": "Увидимся","привет":"И тебе привет!", "как дела?":"Лучше всех"}
    return answers.get(question,'Ой, я тебя не понял. Я пока еще маленький и умею понимать только несколько команд')

def main():
    test = get_answer("Кто ты")
    print(test)


if __name__ == '__main__':
    main()
