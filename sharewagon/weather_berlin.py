import requests

def weather_berlin():
    """
    Get Berlin weather right to your
    Terminal
    """
    # gets wisdome from the interweb
    url = 'https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset,windspeed_10m_max,windgusts_10m_max,winddirection_10m_dominant&timezone=Europe%2FBerlin'
    
    response = requests.get(url).json()
    
    unit_winddirection = response['daily_units']['winddirection_10m_dominant']
    unit_windspeed = response['daily_units']['windspeed_10m_max']
    unit_temperature = response['daily_units']['temperature_2m_max']
    
    winddirection = response['daily']['winddirection_10m_dominant'][0]
    
    # Compute Winddirection to string
    # if winddirection < 35:
    #     win_compass = "north"
    # elif winddirection < 90:
    #     wind
    
    forecast_today = f"Todays Weather {response['daily']['time'][0]}: \
                            \
                        Temperature (max): {response['daily']['temperature_2m_max'][0]}{unit_temperature}\
                            \
                        Windspeed (max) {response['daily']['windspeed_10m_max'][0]}{unit_windspeed}\
                        Winddirection: {winddirection}{unit_winddirection}"
    return forecast_today

print(weather_berlin())