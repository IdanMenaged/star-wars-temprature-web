import requests

from settings import BASE_URL, API_KEY


def getData(city: str, units: str = 'metric') -> dict:
    url = f'{BASE_URL}q={city}&appid={API_KEY}&units={units}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(response.status_code)
    
def getWeather(city: str, units: str = 'metric') -> dict:
    data = getData(city=city, units=units)
    return data['main']