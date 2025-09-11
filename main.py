import json


with open("file/coffee.json", "r", encoding="CP1251") as coffee:
	coffee_json = coffee.read()

file_coffee = json.loads(coffee_json)

# print(file_coffee)
# print(file_coffee["Name"])
first = file_coffee[0]
first_a = first['Name']
print(first_a) 
