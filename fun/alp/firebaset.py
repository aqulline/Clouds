import requests


def get_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"

    response = requests.get(url)
    data = response.json()

    print(data)

    if response.status_code == 200:
        weather = data['main']['temp']

        print(weather)
        return weather
    else:
        return "Weather data not found"


# Set your API key and location
api_key = "18ae72529c924ea34141ce37862480d4"
location = "Dar es salaam"

# Call the function to get the weather
weather = get_weather(api_key, location)
print(weather)



def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return int(celsius)

x = kelvin_to_celsius(weather)

print(x)