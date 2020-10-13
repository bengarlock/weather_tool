import requests
import json
from config import api_key

zip_code = "10128"
country_code = "us"
api_url = f"http://api.openweathermap.org/data/2.5/weather?zip={zip_code},{country_code}&appid={api_key}"


def get_weather():
    data = requests.request("GET", api_url).content
    output = json.loads(data)
    weather = output['weather'][0]['main']
    city = output['name']
    if weather == 'Mist':
        weather = "Misty"
    return (f'Today the weather is {weather} in {city}')


print(get_weather())