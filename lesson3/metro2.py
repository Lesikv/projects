#!usr/bin/env/python                                                                                                                                                                         
#coding:utf8                                                                                                                                                                                 


import json
import sys 

with open("metro.json", "r", encoding = "cp1251") as f:
    data = json.load(f)

res = {}

for row in data:
    key = row["NameOfStation"]
    #print(key)
    repair_list = row["RepairOfEscalators"]
    #if not repair_list:
        #continue
    #for repair in repair_list:
     #   if repair['data'] = now:
     #       res[key]: True
      #      continue
    if repair_list:
        res[key] = [elem["RepairOfEscalators"][0] for elem in repair_list]
        #res[key] = row["RepairOfEscalators"]

print(res)
