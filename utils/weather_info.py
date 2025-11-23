import requests

class WeatherForecastTool:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5"

    def get_current_weather(self, place:str):
        """ Get the current weather for current city"""

        try:
            url=f"{self.base_url}/weather"
            params={
                "q": place,
                "appid": self.api_key,
            }
            response=requests.get(url, params=params)
            return response.json() if response.status_code==200 else None
        except Exception as e:
            raise e
        

    def get_weather_forecast(self, city:str):
        """Get weather forecast of a place"""

        try:
            url=f"{self.base_url}/forecast"
            params={
                "q": city,
                "appid": self.api_key,
                "cnt": 10,  # Number of forecast entries to retrieve
            }
            response=requests.get(url, params=params)
            return response.json() if response.status_code==200 else None
        except Exception as e:
            raise e
