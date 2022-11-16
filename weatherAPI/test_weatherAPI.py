import pytest

from weather import getData, getWeather


# getData tests
def test_get_data():
    try:
        data = getData('tel aviv')
        assert type(data) == dict
    except:
        assert False
        
def test_get_data_units():
    tempStandard = getData('tel aviv', 'standard')['main']['temp']
    tempMetric = getData('tel aviv', 'metric')['main']['temp']
    tempImperial = getData('tel aviv', 'imperial')['main']['temp']
    assert tempImperial != tempMetric != tempStandard
    
def test_get_data_invalid_city():
    try:
        data = getData('afjasda')
    except Exception as e:
        assert True
        

# getWeather tests
def test_get_weather():
    data = getWeather('tel aviv')
    assert type(data) == dict
    assert type(data['temp']) == float
    assert type(data['humidity']) == int
    assert type(data['pressure']) == int
    
def test_get_weather_units():
    tempStandard = getWeather('tel aviv', 'standard')['temp']
    tempMetric = getWeather('tel aviv', 'metric')['temp']
    tempImperial = getWeather('tel aviv', 'imperial')['temp']
    assert tempImperial != tempMetric != tempStandard