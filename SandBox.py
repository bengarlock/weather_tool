import requests
import json
from config import api_key

zip_code = "94574"
country_code = "us"
api_url = f"http://api.openweathermap.org/data/2.5/weather?zip={zip_code},{country_code}&appid={api_key()}&units=imperial"
print(api_url)

def get_weather():
    data = requests.request("GET", api_url).content
    output = json.loads(data)
    weather = output['weather'][0]['main'].lower()
    avg_temp = round(output['main']['feels_like'])
    city = output['name']
    if weather == 'Mist':
        weather = "Misty"
    return (f'Today the weather is {weather} in {city} with an average temperature of {avg_temp} degrees.')


print(get_weather())