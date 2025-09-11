import json


with open("file/coffee.json", "r", encoding="CP1251") as coffee:
	coffee_json = coffee.read()

file_coffee = json.loads(coffee_json)


coffee_shop = file_coffee[1]['Name']
print(coffee_shop)
for cafe in file_coffee:
	coffee_shop = file_coffee[0]['Name']
	print(coffee_shop)

coordinates = file_coffee[0]['geoData']['coordinates']



# print(coffee_shop, '\n', coordinates[0], '\n', coordinates[1])
# print(coordinates[0])
# print(coordinates[1])
# print(coffee_shop,'\n', coordinates)
