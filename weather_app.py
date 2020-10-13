import requests
import json
from config import api_key

zip_code = "07071"
country_code = "us"
api_url = f"http://api.openweathermap.org/data/2.5/weather?zip={zip_code},{country_code}&appid={api_key()}&units=imperial"

def get_weather():
    data = requests.request("GET", api_url).content
    output = json.loads(data)
    weather = output['weather'][0]['main'].lower()
    avg_temp = round(output['main']['temp'])
    city = output['name']
    if weather == 'mist':
        weather = "misty"
    if weather == 'rain':
        weather = 'rainy'

    return (f'Currently, the weather is {weather} in {city} with an average temperature of {avg_temp} degrees.')


print(get_weather())