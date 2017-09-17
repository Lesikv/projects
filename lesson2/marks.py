#!usr/bin/env python
#coding:utf8

#import numpy as np
import random

classes = ('2a','2b','3a','3b','4a','4b') 

marks = {'school_class':' ','scores': []}

journal = []

def gen_score():
    return [random.randint(2, 5) for i in range(5)]

for class_name in classes:
    journal.append({'school_class': class_name, 'scores': gen_score() })

print(journal)




def agg_count(data):
    res = {}
    overall_sum = 0
    class_count = 0

    for row in data:
        #print(row)
        overall_sum += sum(row['scores'])
        class_count += len(row['school_class'])
        res_key = row['school_class']
        #print(res_key)

        res[res_key] = {'marks_sum': sum(row['scores']), 'avg_mark': sum(row['scores'])/len(row['scores'])}

    return res, round(overall_sum/class_count,2)


res, overall_mark = agg_count(journal)
for class_name, data in res.items():
    print(class_name, data)

print('average per each class = {}, average per school = {}'.format(agg_count(journal)[0], agg_count(journal)[1]))       
