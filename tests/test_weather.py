import sys
import os
sys.path.append(f'{os.getcwd()}')

from apis.weather.main import get_weather


class TestGetWeather:
    def test_():
        data: dict[str, str] = get_weather(city='tel aviv')
        assert data['temp'] != None
        assert data['humidity'] != None
        assert data['pressure'] != None