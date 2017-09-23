#!usr/bin/env python
#coding:utf8


import datetime
from datetime import time, timedelta, date, datetime

dt = datetime.now()
delta = timedelta(days = 1)
delta2 = timedelta(days = 30)

dt_yesterday = dt - delta
dt_month_ago = dt - delta2

date_string = "01/01/17 12:10:03.234567"

date_from_string = datetime.strptime(date_string, "%m/%d/%y %H:%M:%S.%f")
        

print("Today is {}, \nYesterday was {} \nMonth ago was {}".format(datetime.date(dt), datetime.date(dt_yesterday), datetime.date(dt_month_ago)))
print(datetime.date(date_from_string))


