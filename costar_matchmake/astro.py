# api calls 
# need location coordinates
# use geopy?
from geopy.geocoders import Nominatim
import requests
import urllib.parse

astro_host = 'http://localhost:3000'
astro_port = 3000

def get_coordinates(location):
	# Initialize Nominatim API
	geolocator = Nominatim(user_agent="MyApp")
	l = geolocator.geocode(location)
	print(l)
	return l.latitude, l.longitude

def get_astrology_info(birthdate, lat, longitude):
	url = 'http://localhost:3000/horoscope?'
	params = {'time': birthdate, 'latitude': lat, 'longitude': longitude, 'house_system': 'P'}
	urllib.parse()
	requests.get('http://localhost:3000/horoscope')


get_coordinates("Nashua")


