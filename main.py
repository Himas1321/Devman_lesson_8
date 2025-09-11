import json


with open("file/coffee.json", "r", encoding="CP1251") as coffee:
	coffee_json = coffee.read()

file_coffee = json.loads(coffee_json)

# print(file_coffee)
# print(file_coffee["Name"])
first = file_coffee[0]['geoData']
first_b = first['coordinates'] 
# first_a = first['Name']
# file = first['PublicPhone']
# file_a = file[0]
# file_b = file_a['geoData']
# file_g = file_b[0]
# first_d = file_g['coordinates']
print(first_b)
# print(file_d)
