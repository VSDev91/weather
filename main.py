import os
import googlemaps
import requests
from dotenv import load_dotenv

load_dotenv()

class Weather():
    def __init__(self, city, state):
        self.geocode(city, state)
        self.get_current_weather()

    def geocode(self, city, state):
        # Below is Google Maps Geocoding API, requires API_KEY
        API_KEY = os.getenv("G_MAPS_API_KEY")
        gmaps = googlemaps.Client(key=API_KEY)
        geocode_result = gmaps.geocode(f"{city} {state}")
        self.lat = geocode_result[0]['geometry']['location']['lat']
        self.lon = geocode_result[0]['geometry']['location']['lng']

    def get_current_weather(self):
        # NWS Weather API, no key/signup needed, free government service
        link = "https://api.weather.gov"
        station_link = f"{link}/points/"
        r = requests.get(f"{station_link}{self.lat},{self.lon}")
        data = r.json()
        station_id = data['properties']['gridId']
        x = data['properties']['gridX']
        y = data['properties']['gridY']
        forecast_link = f"{link}/gridpoints/{station_id}/{x},{y}/forecast"
        r = requests.get(forecast_link)
        data = r.json()
        current_weather = data['properties']['periods'][0]
        self.unpack_weather(current_weather)

    def unpack_weather(self, current_weather):
        self.isDaytime = current_weather['isDaytime']
        self.temp = current_weather['temperature']
        self.chance_rain = current_weather['probabilityOfPrecipitation']['value']
        self.humidity = current_weather['relativeHumidity']['value']
        self.windspeed = current_weather['windSpeed']
        self.picture = current_weather['icon']
        self.shortForecast = current_weather['shortForecast']
        self.print_vars()

    def print_vars(self):
        print(self.isDaytime)
        print(self.temp)
        print(self.chance_rain)
        print(self.humidity)
        print(self.windspeed)
        print(self.picture)
        print(self.shortForecast)
