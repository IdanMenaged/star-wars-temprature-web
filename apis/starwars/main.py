import sys
import os
sys.path.append(f'{os.getcwd()}')

import requests

from CONSTANTS import BASE_URL

def getPage(url) -> dict:
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(response.status_code)
    return response.json()

def get_all_planets() -> set[dict]:
    page = getPage(BASE_URL)
    planets = set()
    for planet in page['results']:
        planets.add(planet)
    while page['next'] != None:
        for planet in page['results']:
            planets.add(planet)
        getPage(url=page['next'])
    return planets

def orgonize() -> dict[str, list[str]]:
    planets = get_all_planets()
    out = {}
    for planet in planets:
        key = planet.climate
        if key not in out.keys():
            out[key] = []
        out[key].append(planet.name)
    return out