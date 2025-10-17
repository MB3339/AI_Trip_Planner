import os
from utils.place_info_search import GooglePlaceSearchTool,TavilyPlaceSearchTool
from typing import List
from langchain.tools import tool
from dotenv import load_dotenv


class PlaceSearchTool:
    def __init__(self):
        load_dotenv()
        self.google_api_key=os.environ.get("GPLACES_API_KEY")
        self.google_places_search= GooglePlaceSearchTool(self.google_api_key)
        self.tavily_search=TavilyPlaceSearchTool()
        self.place_search_tool_list=self._setup_tools()

    def _setup_tools(self)->List:
        """ Setup all tools for the place search tool"""
        @tool
        def search_attraction(palce:str)-> str:
            """ Search for attractions in a given place"""
            try:
                attraction_results=self.google_places_search.google_search_attractions(place)
                if attraction_results:
                    return f" Following are the attractions in {place} as suggested by Google:{attraction_results}"
            except Exception as e:
                Tavily_result=self.tavily_search.search_attractions(place)
                return f"Google cannot find the details due to {e}.\n Following are the attractions in {place} as suggested by Tavily:{Tavily_result}"
            
        @tool
        def search_restraunts(place:str)-> str:
            """ Search restraunts of a place"""
            try:
                restraunts_results=self.google_places_search.google_search_restraunts(place)
                if restraunts_results:
                    return f" Following are the restraunts in {place} as suggested by Google:{restraunts_results}"
            except Exception as e:
                Tavily_result=self.tavily_search.search_restraunts(place)
                return f"Google cannot find the details due to {e}.\n Following are the restraunts in {place} as suggested by Tavily:{Tavily_result}"
            
        @tool
        def search_transportation(place:str)-> str:
            """ Search transportation options in a place"""
            try:
                transportation_results=self.google_places_search.google_search_transportation(place)
                if transportation_results:
                    return f" Following are the transportation options in {place} as suggested by Google:{transportation_results}"
            except Exception as e:
                Tavily_result=self.tavily_search.search_transportation(place)
                return f"Google cannot find the details due to {e}.\n Following are the transportation options in {place} as suggested by Tavily:{Tavily_result}"
            
        @tool
        def search_activities(place:str)-> str:
            """ Search activities in a place"""
            try:
                activities_results=self.google_places_search.google_search_activities(place)
                if activities_results:
                    return f" Following are the activities in {place} as suggested by Google:{activities_results}"
            except Exception as e:
                Tavily_result=self.tavily_search.search_activities(place)
                return f"Google cannot find the details due to {e}.\n Following are the activities in {place} as suggested by Tavily:{Tavily_result}"