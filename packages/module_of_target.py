import csv
import json

import requests

def load_csv(path):
    with open(path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = list(reader)
    return  rows

def load_list_to_json(my_list, path_json):
    with open(path_json, 'w') as file:
        json.dump(my_list, file, indent=4)
    return



def create_list_of_dictionaries(rows):
    cuntry = ""
    my_list = []
    for i in range(len(rows)):
        if i == 0:
            continue
        cuntry = rows[i][0]
        url = rf"http://api.openweathermap.org/geo/1.0/direct?q={cuntry}&appid=a77e9ecbfe9c563ec12320f2d602eb7e"
        response = requests.get(url)
        data = response.json()
        my_dict = {'city': rows[i][0], 'Priority': rows[i][1],'lat': data[0]['lat'], 'lon': data[0]['lon']}
        my_list.append(my_dict)
        path_json1 = 'dir_of_files/targets.json'
    load_list_to_json(my_list, path_json1)
    return my_list