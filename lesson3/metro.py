#!usr/bin/env/python
#coding:utf8

import sys
import csv

with open("dataset_metro.csv", "r", encoding = "cp1251") as f:
    reader = csv.reader(f, delimiter=';')
    #reader = csv.DictReader(f, ['id', 'street'], delimiter=';')
    field_names = []
    rows = []
    for fields in reader:
        if field_names == []:
            field_names = fields
            print(field_names)
            continue
        row = dict(zip(field_names, fields))
        #print(row)
        #print("YAHOO")
        rows.append(row)
        #break

street_to_stations = {}

for row in rows:
    key = row["Street"]
    if key not in street_to_stations:
        street_to_stations[key] = [row["StationName"]]
        continue
    street_to_stations[key].append(row["StationName"])
print(street_to_stations)

res = [(len(stations), street) for street, stations in street_to_stations.items()]

print(street_to_stations.items())

#print(list(sorted(res)))

sort_res = sorted(res, key = lambda x: -x[0])
#print(sort_res)

for elem in sort_res[:10]:
    print(elem)

