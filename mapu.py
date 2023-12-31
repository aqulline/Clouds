import time
import googlemaps


def miles_to_meters(miles):
    try:
        return miles * 1_609.344
    except:
        return 0


API_KEY = 'AIzaSyBTG2Z2tCQyE4MiqIw6Cafil_TaVZaVON4'
map_client = googlemaps.Client(API_KEY)

address = 'Gamex, Makutano Road, Jitegemee, Mabibo, Ubungo Municipal, Dar es Salaam, Coastal Zone, 21493, Tanzania'
geocode = map_client.geocode(address=address)
(lat, lng) = map(geocode[0]['geometry']['location'].get, ('lat', 'lng'))

search_string = 'Bus Company'
distance = miles_to_meters(2)
business_list = []

response = map_client.places_nearby(
    location=(lat, lng),
    keyword=search_string,
    radius=distance
)

business_list.extend(response.get('results'))
next_page_token = response.get('next_page_token')

while next_page_token:
    time.sleep(2)
    response = map_client.places_nearby(
        location=(lat, lng),
        keyword=search_string,
        radius=distance,
        page_token=next_page_token
    )
    business_list.extend(response.get('results'))
    next_page_token = response.get('next_page_token')

for i in range(10):
    print(business_list[i]["name"], f'{business_list[i]["geometry"]["location"]["lat"]}, {business_list[i]["geometry"]["location"]["lng"]}')

