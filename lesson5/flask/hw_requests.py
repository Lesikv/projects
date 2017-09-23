#!usr/bin/env python
#codinf:utf8

import requests

#api_key ='0f7dc8d36ff97e51c59f8e2314a5bfe1'

def get_data(url):
    result = requests.get(url)
    if result.status_code == 200:
        return result.json()
    else:
        print("Something goes wrong")


if __name__ == "__main__":
    data = get_data('http://api.data.mos.ru/v1/datasets/2009/rows?api_key=0f7dc8d36ff97e51c59f8e2314a5bfe1')
    print(data)

