import sys
import os
sys.path.append(f'{os.getcwd()}')

import requests

from .CONSTANTS import BASE_URL

def get_weather(city: str) -> dict:
    response = requests.get(BASE_URL + f'q={city}')
    if response.status_code != 200:
        raise Exception(response.status_code)
    data = response.json()
    return {
        'temp': data['temp'],
        'humidity': data['humidity'],
        'pressure': data['pressure']
    }