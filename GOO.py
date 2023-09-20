import requests


class Distatnce:

    def mi_km(self, mi):
        km = int(int(mi) * 1.60934 / 1)

        print(km, mi)

        return km

    def get_distance(self, origin, dest):
        API_KEY = 'AIzaSyBTG2Z2tCQyE4MiqIw6Cafil_TaVZaVON4'

        url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={origin}&destinations={dest}&units=imperial&key={API_KEY}"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        data = response.json()

        distance = data["rows"][0]["elements"][0]['distance']["text"]
        time = data["rows"][0]["elements"][0]['duration']["text"]

        new_d = distance.strip().split(" ")[0]
        distance = self.mi_km(new_d)

        return [distance, time]


print(Distatnce.get_distance(Distatnce(), "Arusha", "Dar es salaam"))
