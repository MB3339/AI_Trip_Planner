import os
import json
from langchain_tavily import TavilySearch
from langchain_google_community import GooglePlacesTool, GooglePlacesAPIWrapper

class GooglePlaceSearchTool:
    def __init__(self,api_key:str):
        self.places_wrapper=GooglePlacesAPIWrapper(gplaces_api_key=api_key)
        self.places_tool=GooglePlacesTool(api_wrapper=self.places_wrapper)

    
    def google_search_attractions(self,place:str)-> dict:
        """
        Searches for attraction in the specified place using GooglePlaces API.

     
       """
        return self.places_tool.run(f"top attractive places in and around {place}")
    
    def google_search_restraunts(self,place:str)->dict:
        "searches for available restraunts in the specified place using GooglePlaces API"
        return self.places_tool.run(f"what are the top 10 restraunts and eatries in and around {place}?")

    def google_search_activity(self,place:str)->dict:
        """
        Searches for popular activities in the specified place using GooglePlaces API.

        """
        return self.places_tool.run(f"Activities in and around {place} ")
    
    def google_search_transportation(self,place:str)->dict:
        """
        Searches for available modes of transportation in the specified place using GooglePlaces_API
        """
        return self.places_tool.run(f"what are the different modes of transportation in and around {place}?")
    
class TavilyPlaceSearchTool:
    def __init__(self):
        pass

    def tavily_search_attractions(self,place:str)-> dict:
        """
        Searches for attraction in the specified place using TavilySearch.
        """
        tavily_tool=TavilySearch(topic='general',include_answers='advanced')
        result=tavily_tool.invoke({'query':f"top attractive places in and around {place}"})
        if isinstance(result,dict) and result.get('answers'):
            return result['answers']
        return result
    
    def tavily_search_restraunts(self,place:str)->dict:
        """
        Search for available restraunts in the specified place using TavilySearch.
        """
        tavily_tool=TavilySearch(topic='general', include_answer='advanced')
        result=tavily_tool.invoke({'query':f'what are the top 10 restraunts and eateries in and around the {place}'})
        if isinstance(result,dict) and result.get('answers'):
            return result['answers']
        return result

    def tavily_search_activity(self,place:str)->dict:
        """ 
        Searches for popular activities in the specified place using TavilySearch.
        """
        tavily_tool= TavilySearch(topic='general', include_answer='advanced')
        result=tavily_tool.invoke({'query':f'activities in and around {place}'})
        if isinstance(result,dict) and result.get('answers'):
            return result['answers']
        return result
    
    def tavily_search_transportation(self,place:str)->dict:
        """
        Searches for available modes of transportation in the specified place using TavilySearch.
        """
        tavily_tool=TavilySearch(topic='general', include_answer='advanced')
        result=tavily_tool.invoke({'query':f'what are the different modes of transportation in and around {place}?'})
        if isinstance(result,dict) and result.get('answers'):
            return result['answers']
        return result
