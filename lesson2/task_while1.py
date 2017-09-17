#!usr/bin/env python
#coding:utf8

#import numpy as np


names = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]

# def find_person(names, person):
#     while len(names) > 0:
#         name = names.pop()
#         print("YAHOO")
#         print(names)
#         if name == person:
#             break
#         print("YAHOO2")
#     return names


while len(names) > 0:
    name = names.pop()
    print(name)
    if name == 'Валера':
        break
    print("Yahoo")
    print(names)
print(names)
        
