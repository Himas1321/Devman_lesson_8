import os
import json
import requests
from geopy import distance

apikey = '523415ff-cec5-4774-b24a-fd5d9203c5d0'


def fetch_coordinates(apikey, address):
    base_url = "https://geocode-maps.yandex.ru/1.x"
    response = requests.get(base_url, params={
        "geocode": address,
        "apikey": apikey,
        "format": "json",
    })
    response.raise_for_status()
    found_places = response.json()['response']['GeoObjectCollection']['featureMember']

    if not found_places:
        return None

    most_relevant = found_places[0]
    lon, lat = most_relevant['GeoObject']['Point']['pos'].split(" ")
    return lon, lat




 
# def user(apikey):
# 	name_user = input('Где вы находитесь: ')
# 	coords = fetch_coordinates(apikey, name_user)
# 	print(f'Ваши координаты: {coords}')   


def main():
	name_a = input('Пункт А: ')
	name_b = input('Пункт Б: ')
	coords_a = fetch_coordinates(apikey, name_a)
	coords_b = fetch_coordinates(apikey, name_b)
	coords_a_1 = coords_a[1], coords_a[0]
	coords_b_1 = coords_b[1], coords_b[0]
	result_distance = distance.distance(coords_a_1, coords_b_1).km
	print(f'Расстояние: {result_distance}')
	print(f'Ваши координаты: {coords_b[1], coords_b[0]}, {coords_a[1], coords_a[0]}') 

	with open("file/coffee.json", "r", encoding="CP1251") as coffee:
		coffee_json = coffee.read()
		
	file_coffee = json.loads(coffee_json)

	coffeeshop_list = []

# 	for cafe in file_coffee:
# 		if 'Name' in cafe:
# 			print(cafe['Name'])
# 			if 'geoData' in cafe and 'coordinates' in cafe['geoData']:
# 				print(cafe['geoData']['coordinates'])




# # # coffee_shop = file_coffee[1]['Name']
# # # coordinates = file_coffee[0]['geoData']['coordinates']

if __name__ == '__main__':
	main()
	main()

