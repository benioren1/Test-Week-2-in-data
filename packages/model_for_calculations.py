import json
import math

weights = {
    "distance" : 0.15,
    "aircraft_type" : 0.25,
    "pilot_skill" : 0.25,
    "weather_conditions" : 0.20,
    "execution_time" : 0.10,
    "priority":0.10
}
#jhauc מרחק
def haversine_distance(lat1, lon1):
    lat2 = 32.6307267 # Destination latitude
    lon2 = 35.3488686 # Destination longitude
    r = 6371.0 # Radius of the Earth in kilometers
    # Convert degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    # Calculate differences between the coordinates
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    # Apply Haversine formula
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    # Calculate the distance
    distance = r * c
    return distance

def calculate_distances_persent():
    path_targets = '../dir_of_files/targets.json'
    with open(path_targets, 'r',encoding='utf-8') as file:
        data = json.load(file)

    list_target_by_distance = sorted(data, key=lambda x: x['distance_from_israel'], reverse=True)
    list_dictance = []
    count = 0.15
    for i in range(len(list_target_by_distance)):

        distance = round(count, 2)
        list_dictance.append((list_target_by_distance[i]['city'], distance))
        count -= 0.01
    return  list_dictance

print(calculate_distances_persent())

def calculate_aircraft_type_persent():
    path_aircraft = '../dir_of_files/aircrafts.json'
    with open(path_aircraft, 'r',encoding='utf-8') as file:
        data = json.load(file)

    list_aircraft_by_fuel = sorted(data, key=lambda x: x['fuel_capacity'], reverse=True)
    count = 0.20
    list_type = []
    for i in range(len(list_aircraft_by_fuel)):
        distance = round(count, 2)
        list_type.append((list_aircraft_by_fuel[i]['type'], distance))
        count -= 0.02
    return list_type

print(calculate_aircraft_type_persent())

def calculate_pilot_skill_persent():
    path_pilot = '../dir_of_files/pilots.json'
    with open(path_pilot, 'r',encoding='utf-8') as file:
        data = json.load(file)

    list_pilot_by_skill = sorted(data, key=lambda x: x['skill_level'], reverse=True)
    count = 0.25
    list_skill = []
    for i in range(len(list_pilot_by_skill)):
        distance = round(count, 2)
        list_skill.append((list_pilot_by_skill[i]['name'], distance))
        count -= 0.02
    return list_skill
print(calculate_pilot_skill_persent())

def calculate_weather_persent():
    path_targets = '../dir_of_files/targets.json'
    with open(path_targets, 'r',encoding='utf-8') as file:
        data = json.load(file)

    list_target_by_weather = sorted(data, key=lambda x: x['main'], reverse=True)
    list_dictance = []

    for i in range(len(list_target_by_weather)):
        if list_target_by_weather[i]['main'] ==1.0:
            list_dictance.append((list_target_by_weather[i]['city'], 0.25))
        elif list_target_by_weather[i]['main'] ==0.7:
            list_dictance.append((list_target_by_weather[i]['city'], 0.20))
        elif list_target_by_weather[i]['main'] == 0.4:
            list_dictance.append((list_target_by_weather[i]['city'], 0.15))
        elif list_target_by_weather[i]['main'] == 0.2:
            list_dictance.append((list_target_by_weather[i]['city'], 0.10))

    return  list_dictance

print(calculate_weather_persent())

def calculate_prayority_persent():
    path_prayority = '../dir_of_files/targets.json'
    with open(path_prayority, 'r',encoding='utf-8') as file:
        data = json.load(file)

    list_target_by_prayority = sorted(data, key=lambda x: x['Priority'], reverse=True)
    list_dictance = []

    for i in range(len(list_target_by_prayority)):
        if list_target_by_prayority[i]['Priority'] == "5":
            list_dictance.append((list_target_by_prayority[i]['city'], 0.15))
        elif list_target_by_prayority[i]['Priority'] =="4":
            list_dictance.append((list_target_by_prayority[i]['city'], 0.12))
        elif list_target_by_prayority[i]['Priority'] == "3":
            list_dictance.append((list_target_by_prayority[i]['city'], 0.10))
        elif list_target_by_prayority[i]['Priority'] == "2":
            list_dictance.append((list_target_by_prayority[i]['city'], 0.8))
        elif list_target_by_prayority[i]['Priority'] == "1":
            list_dictance.append((list_target_by_prayority[i]['city'], 0.5))

    return  list_dictance
print(calculate_prayority_persent())



def blblblblblbbllbl(list):
    list1 = calculate_distances_persent()
    l1 = 0
    for i in range(len(list1)):
        if list1[i][0] == list[0]:
            l = list1[i][1]
            break

    list2 = calculate_weather_persent()
    l2 = 0
    for i in range(len(list2)):
        if list2[i][0] == list[1]:
            l2 = list2[i][1]
            break
    result_list = []

    list3 = calculate_prayority_persent()
    l3 = 0
    for i in range(len(list3)):
        if list3[i][0] == list[0]:
            l3 = list3[i][1]
            break

    list4 = calculate_pilot_skill_persent()
    l4 = 0
    for i in range(len(list4)):
        if list4[i][0] == list[2]:
            l4 = list4[i][1]
            break
    list5 = calculate_aircraft_type_persent()
    l5 = 0
    for i in range(len(list5)):
        if list5[i][0] == list[3]:
            l5 = list5[i][1]
            break
    allll = l1 + l2 + l3 + l4 + l5

    last_all = round(allll, 2)
    return last_all

