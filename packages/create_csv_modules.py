import csv
import json

from packages import  model_for_calculations

data = []



path_json_target = '../dir_of_files/targets.json'
with open(path_json_target, 'r', encoding='utf-8') as file:
    data_target = json.load(file)

path_json_pilot = '../dir_of_files/pilots.json'
with open(path_json_pilot, 'r', encoding='utf-8') as file:
    data_pilot = json.load(file)

path_json_aircraft = '../dir_of_files/aircrafts.json'
with open(path_json_aircraft, 'r', encoding='utf-8') as file:
    data_aircraft = json.load(file)

data = [["target_city", "priority", "assigned_pilot", "assigned_aircraft", "distance", "weather_conditions", "pilot_skill", "aircraft_speed", "fuel_capacity"]]
for i in range(len(data_target)):
    for j in range(len(data_pilot)):
        for k in range(len(data_aircraft)):
            last_score = model_for_calculations.blblblblblbbllbl(
                [data_target[i]['city'], data_target[i]['main'], data_pilot[j]['name'],
                 data_aircraft[k]['fuel_capacity']])
            data.append([data_target[i]['city'],int(data_target[i]['Priority']), data_pilot[j]['name'], data_aircraft[k]['type'],data_target[i]['distance_from_israel'],data_target[i]['main'],data_pilot[j]['skill_level'], data_aircraft[k]['speed'], data_aircraft[k]['fuel_capacity'],last_score])

print(data)
with open('data_semicolon.csv', mode='w', newline='') as file:
    csv_writer = csv.writer(file, delimiter=';')
    csv_writer.writerows(data)