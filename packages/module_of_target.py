import csv
import json
from datetime import datetime
from packages import modules_of_weather
from packages import model_for_calculations
import requests

from packages import modules_of_weather

#פןנקציה שמטעינה cvs לתוך ליסט
def load_csv(path):
    with open(path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = list(reader)
    return  rows

#פונקציה שמטעינה את הליסט לגייסון
def load_list_to_json(my_list, path_json):
    with open(path_json, 'w') as file:
        json.dump(my_list, file, indent=4)

    return

#פונקציה שאני מביא לה גייסון והיא יודעת לפלטר לי את זה ולהחזיר לי יום מסויים
def filter_by_datetime(data, target_datetime_str):

    target_datetime = datetime.strptime(target_datetime_str, '%Y-%m-%d %H:%M:%S')


    for entry in data['list']:
        dt_txt = entry['dt_txt']
        dt = datetime.strptime(dt_txt, '%Y-%m-%d %H:%M:%S')
        if dt == target_datetime:
            filtered_data = {}
            level_clouds = modules_of_weather.weather_score(entry['weather'][0]['main'])
            filtered_data['clouds'] = entry['clouds']['all']

            filtered_data['main'] = level_clouds
            filtered_data['wind'] = entry['wind']['speed']

    return filtered_data


#הפונקציה שמשתמשת בפונקציה מעל ושולחת לה את הדאטה הרצוי לפי מדינה מסויימת
def load_weather(cuntry):
    url = rf"https://api.openweathermap.org/data/2.5/forecast?q={cuntry}&appid=a77e9ecbfe9c563ec12320f2d602eb7e"
    response = requests.get(url)
    data = response.json()
    target_date = '2024-09-13 00:00:00'
    filtered_list = filter_by_datetime(data, target_date)

    return filtered_list


#יצירת הגייסון של המטרות לפי כל הנתונים של כל מטרה הפונקציה נעזרת בפונקציות למעלה בשביל ליצור את הגייסון
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
        weather_of_cuntry = load_weather( cuntry)
        distances_from_israel = model_for_calculations.haversine_distance(data[0]['lat'], data[0]['lon'])
        my_dict = {'city': rows[i][0], 'Priority': rows[i][1],'lat': data[0]['lat'], 'lon': data[0]['lon'], 'distance_from_israel':distances_from_israel}

        combined_dict = {**weather_of_cuntry, **my_dict}
        my_list.append(combined_dict)
        path_json1 = 'dir_of_files/targets.json'
    load_list_to_json(my_list, path_json1)
    return my_list