import os
from dotenv import load_dotenv
from typing import Any, Dict, Optional, List
from utils.weather_info import WeatherForecastTool
from langchain_tools import Tool  

class WeatherInfoTool(Tool):
   
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("WEATHER_API_KEY")
        self.weather_service= WeatherForecastTool(api_key=self.api_key)
        self.weather_tool_list= self._setup_tools()
  
        

    def _setup_tools(self) -> List:
        """ Setup all tools for weather information retrieval. """
        @Tool
        def get_current_weather(city:str)   -> str:
            "Get current weather for a city"
            weather_data = self.weather_service.get_current_weather(city)

            if weather_data:
                temp=weather_data.get('main',{}).get('temp','N/A')
                desc=weather_data.get('weather',[{}])[0].get('description','N/A')
                return f'Current temperature in {city} is {temp}°C with {desc}.'
            return f"Could not retrieve weather data for {city}."


        @Tool

        def get_weather_forecast(city:str, days:int=3) -> str:
            "Get weather forecast for a city for the next 'days' days"
            forecast_data = self.weather_service.get_weather_forecast(city, days)

            if forecast_data:
                forecasts = []
                for day in forecast_data.get('list', []):
                    date = day.get('dt_txt', 'N/A')
                    temp = day.get('main', {}).get('temp', 'N/A')
                    desc = day.get('weather', [{}])[0].get('description', 'N/A')
                    forecasts.append(f"{date}: {temp}°C, {desc}")
                return f"Weather forecast for {city}:\n" + "\n".join(forecasts)
            return f"Could not retrieve weather forecast for {city}."