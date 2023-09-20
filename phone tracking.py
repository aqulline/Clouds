import phonenumbers
from myphone import number
from phonenumbers import carrier
import opencage
from opencage.geocoder import OpenCageGeocode
import folium

from phonenumbers import geocoder

phone = phonenumbers.parse(number)
location = geocoder.description_for_number(phone, "en")
print(location)
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, 'en'))


opencode_key = "229637eb75ec40daae6f5967b2d7f81b"

gecoder = OpenCageGeocode(opencode_key)
query = str(location)
result = gecoder.geocode(query)
# print(result)

lat = result[0]['geometry']['lat']
lon = result[0]['geometry']['lng']
#
print(lat, lon)

# -6.5247123 35.7878438

map_location = folium.Map(location=[lat, lon], zoom_start=9)
folium.Marker([lat, lon], popup=location).add_to(map_location)
map_location.save('locations.html')
