import os
import googlemaps
import requests
from dotenv import load_dotenv


link = "https://api.weather.gov"
alerts_link = "https://api.weather.gov/alerts?area="
forecast_link = "https://api.weather.gov/points/"

# NWS Weather API, no key/signup needed, free government service
r = requests.get(link)
r = requests.get(f"{alerts_link}{state}")
r = requests.get(f"{forecast_link}{lat}{lon}")

# Below is Google Maps Geocoding API, requires API_KEY
load_dotenv()
# lat + lon variables are temporary/hardcoded until further features are added, which then would use the geocode_result data
lat = os.getenv("lat")
lon = os.getenv("lon")
API_KEY = os.getenv("G_MAPS_API_KEY")
gmaps = googlemaps.Client(key=API_KEY)
geocode_result = gmaps.geocode("INPUT ADDRESS heRE")
lat = geocode_result[0]['geometry']['location']['lat']
lon = geocode_result[0]['geometry']['location']['lng']





