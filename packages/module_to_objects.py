import json

from classes.aircraft import aircraft
from classes.pilot import pilot

path_aircraft = r"C:\Users\benio\PycharmProjects\Test-Week-2-in-data\dir_of_files\aircrafts.json"
path_pilot = r"C:\Users\benio\PycharmProjects\Test-Week-2-in-data\dir_of_files\pilots.json"

def convert_json_to_pilot(path_pilot):
    with open(path_pilot, 'r',encoding='utf-8') as file:
        data = json.load(file)



    people_list = []
    for person_data in data:
        person = pilot(**person_data)
        people_list.append(person)


    return people_list



def convert_json_to_aircraft(path_aircraft):
    with open(path_aircraft, 'r',encoding='utf-8') as file:
        data = json.load(file)



    aircraft_list = []
    for person_data in data:
        person = aircraft(**person_data)
        aircraft_list.append(person)


    return aircraft_list

