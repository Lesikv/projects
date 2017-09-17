#!usr/bin/env python
#coding: utf8

age = int(input("Введите возраст "))

if age <= 6:
    print("Пока учись в детском саду")
elif age <= 18:
    print("Пока учись в школе")
elif age <= 23:
    print("Учись в университете")
else:
    print("Работать")

