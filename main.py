import os
from dotenv import load_dotenv
import json
import requests
from geopy import distance
import folium


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


def get_coffeeshop_distance(coffeeshop_min):
	return coffeeshop_min['distance']


def main():
	load_dotenv()
	apikey = os.getenv('APIKEY')

	user = input('Где вы находитесь ?')
	coords = fetch_coordinates(apikey, user)
	coords_separately = coords[1], coords[0]

	with open("file/coffee.json", "r", encoding="CP1251") as coffee:
		coffee_json = coffee.read()
		
	file_coffee = json.loads(coffee_json)

	coffeeshop_list = []

	for coffeeshop in file_coffee:
		coffeeshop_coords = coffeeshop['geoData']['coordinates']
		coffeeshop_info = dict()
		coffeeshop_info['title'] = coffeeshop['Name']
		coffeeshop_info['distance'] = distance.distance((coffeeshop_coords[1], coffeeshop_coords[0]), (coords_separately)).km
		coffeeshop_info['latitude'] = coffeeshop_coords[1]
		coffeeshop_info['longitude'] = coffeeshop_coords[0]
		coffeeshop_list.append(coffeeshop_info)

	coffeeshop_min = sorted(coffeeshop_list, key=get_coffeeshop_distance)[:5]
	
	m = folium.Map([coords[1], coords[0]], zoom_start=12)
	
	folium.Marker(
		location=[coords[1], coords[0]],
		tooltip="Нажми меня!",
		popup="Я",
		icon=folium.Icon(icon="green"),
	).add_to(m)

	for coffeeshop in coffeeshop_min:
		folium.Marker(
            location=[coffeeshop['latitude'], coffeeshop['longitude']],
            tooltip=coffeeshop['title'],
            popup=coffeeshop['title'],
            icon=folium.Icon(color='red'),
        ).add_to(m)

	m.save('index.html')


if __name__ == '__main__':
	main()
