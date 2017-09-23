#!usr/bin/env/python                                                                                                                                                                         
#coding:utf8                                                                                                                                                                                 


import json
import sys 
from datetime import datetime, time, date, timedelta

with open("metro.json", "r", encoding = "cp1251") as f:
    data = json.load(f)

res = {}

for row in data:
    key = row["NameOfStation"]
    #print(key)
    repair_list = row["RepairOfEscalators"]
    if repair_list:
        #res[key] = [(datetime.strptime(elem["RepairOfEscalators"].split('-')[0], "%d.%m.%Y"), datetime.strptime(elem["RepairOfEscalators"].split('-')[1], '%d.%m.%Y'))for elem in repair_list]
        for elem in repair_list:
            res[key] = {'date': [], 'Repair' : 'False'}
            res[key]['date'] = [datetime.date(datetime.strptime(elem["RepairOfEscalators"].split('-')[0], "%d.%m.%Y")), datetime.date(datetime.strptime(elem["RepairOfEscalators"].split('-')[1], '%d.%m.%Y'))]
            if datetime.date(datetime.now()) >= res[key]['date'][0] and datetime.date(datetime.now()) <= res[key]['date'][1]:
                res[key]['Repair'] = 'True'


print(res)
