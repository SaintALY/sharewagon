# tests/test_lib.py
from mlproject.lib import weather_berlin

def test_weather_prediction():
    assert len(weather_berlin()) != 0
   