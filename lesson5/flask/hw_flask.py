#!usr/bin/env python
#coding:utf8


#Задание
#Добавьте на сайт страницу /names, на которой в табличном виде выведите данные о именах новорожденных, получаемые при помощи функции из предыдущей задачи. Пример простейшего оформления таблицы 
#Ограничьте выводимые данные одним годом. Год должен указываться в URL как параметр, например /names?year=2016


#ВОПРОСЫ
#1. Как сделать отсортированную таблицу
#2. Как сделать так, чтобы в маршрутизатор можно было подставлять переменную


from flask import Flask

from hw_requests import get_data


app = Flask(__name__)

api_key ='0f7dc8d36ff97e51c59f8e2314a5bfe1'
year = 2016

@app.route("/")
def index():
    url = 'http://api.data.mos.ru/v1/datasets/2009/rows?api_key=0f7dc8d36ff97e51c59f8e2314a5bfe1'
    names = get_data(url)
    return str(names)
    
@app.route("/names")
def table():
    url = 'http://api.data.mos.ru/v1/datasets/2009/rows?api_key=%s' %(api_key) 
    names = get_data(url)
    table = '<table><tr><th> %s </th> <th> %s </th><th>%s </th></tr>' %('Name','Number','Date')
    for row in names:
        table += "<tr><td> %s </td> <td> %s </td><td> %s </td> <tr>" % (row['Cells']['Name'], row['Cells']['NumberOfPersons'],(str(row['Cells']['Month']) + ' ' + str(row['Cells']['Year'])))
    table += '</table>'
    return table
@app.route('/names&year=2016')
def filter():
    url = 'http://api.data.mos.ru/v1/datasets/2009/rows?api_key=%s' %(api_key)
    names = get_data(url)
    table = '<table><tr><th> %s </th> <th> %s </th><th>%s </th></tr>' %('Name','Number','Date')                                                                                              
    for row in names:
        if row['Cells']['Year'] != year:
            print(row)
            continue
        print('Yahoo')
        table += "<tr><td> %s </td> <td> %s </td><td> %s </td> <tr>" % (row['Cells']['Name'], row['Cells']['NumberOfPersons'],(str(row['Cells']['Month']) + ' ' + str(row['Cells']['Year'])))
    table += '</table>'  
    print(table)
    return table


if __name__ == "__main__":
    app.run()

