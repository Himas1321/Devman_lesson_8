import json


with open("file/coffee.json", "r", encoding="CP1251") as coffee:
	coffee_json = coffee.read()

file_coffee = json.loads(coffee_json)



# print(coffee_shop)
for cafe in file_coffee:
	if cafe == 'Name':
		print(cafe)


coffee_shop = file_coffee[1]['Name']
coordinates = file_coffee[0]['geoData']['coordinates']

