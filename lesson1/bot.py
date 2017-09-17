import logging
from answers import get_answer
import ephem
from datetime import datetime, date
import time
import re
import pandas as pd


from telegram.ext import Updater,CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup
logging.basicConfig(format = '%(name)s - %(levelname)s - %(message)s',level = logging.DEBUG)


def main():
    updater = Updater("435974426:AAEM0jPx_42SA7AWdBsynQShFUruf_WTS6k")
    dp = updater.dispatcher                                                                                   
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", cosmo, pass_args = True))
    dp.add_handler(CommandHandler("moon", new_moon, pass_args = True))
    dp.add_handler(CommandHandler("wordcount", wordcount, pass_args = True))
    dp.add_handler(CommandHandler("calc", calc, pass_args = True))
    dp.add_handler(CommandHandler("customkb", customkb))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("goroda", goroda, pass_args = True))
    updater.start_polling()
    updater.idle()






def greet_user(bot, update):
    text = 'Привет! Я пока еще маленький ботик. Я умею понимать следующие команды: "Привет", "Как дела?", "Пока"'
    print(text)
    print(update)
    print('Вызван/start')
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(get_answer(user_text))


def date_convert(date_string):
    print(date_string)
    if not date_string.find("."):
        pass
    else:
        print("YAHOO")
        date_string = date_string.replace(".", "/")
    res_date = datetime.fromtimestamp(time.mktime(time.strptime(date_string, "%d/%m/%Y"))).strftime("%Y/%m/%d")
    print(res_date)
    return res_date



def cosmo(bot, update, args):
    update.message.reply_text("Введите название планеты Солнечной системы на английском язык")
    user_planet = args[0]
    user_date = date_convert(str(args[1]))
    print(type(user_date))
    print(user_date)
    print(user_planet)
    print("Вызван /planet")
    print(update)
    planet = getattr(ephem, user_planet, None)
    if not planet:
        update.message.reply_text("Такой планеты нет")
    else:
        answer = ephem.constellation(planet(user_date))
        update.message.reply_text("{} {} находится в созвездии {}".format(user_date, user_planet, answer[0]))


def new_moon(bot, update, args):
    date = date_convert(args[0])
    print(date)
    print("Вызван/moon")
    print(update)
    answer = ephem.next_full_moon(date)
    update.message.reply_text(str(answer))
    print(answer)

def wordcount(bot, update, args):
    #user_string = args
    #print(args)
    user_string = update.message.text
    res = re.split(r"[\s,\.]+", user_string[len("/wordcount"):].strip())
    print(res)
    len_str = len(res)
    update.message.reply_text(len_str)

def calc_fun(operand, *numbers):
    first = numbers[0]
    second = numbers[1]
    firest, second = numbers[:2]
    if operand == "-":
        return first - second
    if operand == "+":
        return first + second
    if operand == "*":
        return first*second
    try:
        if operand == "/":
            return first / second
    except ZeroDivisionError: 
        return "На ноль делить нельзя"


def calc_simple(bot, update, args):
    user_string = update.message.text[len("/calc"):].strip()
    print(user_string)
    res = []
    for i in range(len(user_string)):
        if user_string[i] != "=":
            res.append(user_string[i])
    print(res)
    first = int(res[0])
    print(first)
    second = int(res[len(res)-1])
    print(second)
    operand = res[1]
    answer = calc_fun(operand,first, second)
    update.message.reply_text(answer)
            
def calc(bot, update, args):
    user_string = update.message.text[len("/calc"):].strip()
    print(user_string)
    operators = [ "+", "-", "*", "/", "="] 
    numbers = [str(i) for i in range(0,10)]
    answer = None
    last_oper = None
    last_elem = ""
    for i in range(len(user_string)):
        cur = user_string[i]
        if cur in operators:
            print("YAHOO3")
            print(cur)
            if last_oper is None:
                answer = last_elem
            else:
                print("last_elem = {} cur = {} answer = {} last_oper = {}".format(last_elem, cur, answer, last_oper))
                answer = calc_fun(last_oper, int(answer), int(last_elem))
                print("last_elem = {} cur = {} answer = {} last_oper = {}".format(last_elem, cur, answer, last_oper))
                if cur == "=":
                    break
            last_elem = ""

            last_oper = cur
            continue
        if cur in numbers:
            last_elem += cur
    update.message.reply_text(answer)

def customkb(bot, update):
    custom_keyboard = [['1','2','3','4','5'], ['6','7','8','9','0'],['-','+','*','/','=']]
    reply_markup = ReplyKeyboardMarkup(custom_keyboard)
    bot.send_message(chat_id = update.message.chat_id, text = "Клавиатура активирована.", reply_markup = reply_markup)

df = pd.read_table("cities.txt", sep = "\t", names = ['city_name'])                                                                                                                      
cities = [str(i) for i in df['city_name']]

def goroda(bot, update, args):
    user_city = args[0]
    last_letter = args[0][-1]
    if last_letter in ["й","ъ","ь","ц"]:
        last_letter = args[0][-2]
    print(last_letter)
    print(user_city)
    for i in range(len(cities)):
        if cities[i][:1] == last_letter.upper():
            answer = cities.pop(i)
            cities.remove(user_city)
            print(answer)
            update.message.reply_text("{}, ваш ход ".format(answer))
            return






if __name__ == '__main__':
    main()
