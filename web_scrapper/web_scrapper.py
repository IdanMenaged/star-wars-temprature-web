# this file contains all the parsers for the different websites

from datetime import datetime
import requests
from bs4 import BeautifulSoup


def parseWorldWeather(city: str = '', time=datetime.now(), degrees: str = 'c') -> float:
    degreesToIndex = {
        'c': 0,
        'f': 1
    }
    
    URL = f'https://www.google.com/search?q=weather+{city.replace(" ", "+")}'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    # ^ soup is the version of the page we can parse
    temps = soup.find(id='main').find(id='cnt')
    # .find(id='rcnt').find(id='center_col').find(id='res').find(id='search').find('div').find(id='rso').find(class_='ULSxyf').find(class_='MjjYud').find(class_='wDYxhc').find('div').find(id='wob_wc').find(class_='UQt4rd').find(class_='Ab33Nc').find('div').find(class_='vk_bk')
    # ^ get the element with the temps data
    # WARNING: really fragile, once the html changes even one bit it falls apart
    print(temps.prettify())
    
    
if __name__ == '__main__':
    parseWorldWeather()