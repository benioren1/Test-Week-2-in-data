import csv
import requests
import json
from packages import module_of_target
from packages import modules_of_weather
from packages.module_to_objects import convert_json_to_pilot, convert_json_to_aircraft

path_csv = 'dir_of_files/air_strike_targets.csv'

rows =module_of_target.load_csv(path_csv)
print(rows)
my_list =module_of_target.create_list_of_dictionaries(rows)
print(my_list)
path_json = 'dir_of_files/targets.json'

print(module_of_target.load_weather('tehran'))
path_pilots = 'dir_of_files/pilots.json'
path_aircraft = 'dir_of_files/aircrafts.json'

print(convert_json_to_pilot(path_pilots))
print(convert_json_to_aircraft(path_aircraft))





    # with open(path_json, 'r', encoding='utf_8') as file:
    #     data_json = json.load(file)
    # return data_json

# for i in range(len(rows)):
#     if i == 0:
#         continue
#     cuntry = rows[i][0]
#     response = requests.get(url)
#     data = response.json()
#     print(f"{rows[i][0]}, {data[0]['name']}, {data[0]['country']}")
#
# response = requests.get(url)
# data = response.json()
# print(data)
