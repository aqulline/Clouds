# importing library
import requests
from bs4 import BeautifulSoup

# enter city name
city = "Dar es salaam"

# creating url and requests instance
url = "https://www.busbora.co.tz/search-buses?from=218&to=68&date=21-03-2023&srcType=1"
html = requests.get(url).content

citya = ["https://maps.me/catalog/transport/amenity-bus_station/country-tanzania/city-dar-es-salaam-27565027/",
         "https://maps.me/catalog/transport/amenity-bus_station/country-tanzania/city-moshi-255602805/",
         "https://maps.me/catalog/transport/amenity-bus_station/country-tanzania/city-arusha-255603098/",
         "https://maps.me/catalog/transport/amenity-bus_station/country-tanzania/city-mbeya-255594923/",
         "https://maps.me/catalog/transport/amenity-bus_station/country-tanzania/city-dodoma-87841198/",
         "https://maps.me/catalog/transport/amenity-bus_station/country-tanzania/city-tanga-255615843/",
         "https://maps.me/catalog/transport/amenity-bus_station/country-tanzania/city-morogoro-252592807/"]
# getting raw data
soup = BeautifulSoup(html, 'html.parser')

temp = soup.find_all('div', attrs={'class': 'bus_name'})
name = soup.find_all('h6', attrs={'class': 'name'})

for res in range(temp.__len__()):
    print(temp[res].text.strip())
