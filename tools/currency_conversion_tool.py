import os
from utils.currency_convertor import CurrencyConvertor
from typing import List
from langchain_core.tools import tool
from dotenv import load_dotenv


class CurrencyConverterTool:
    def __init__(self):
        load_dotenv()
        self.api_key=os.getenv("EXCHANGE_RATE_API_KEY")
        self.currency_service=CurrencyConvertor(self.api_key)
        self.currency_converter_tool_list=self.setup_tools()

    def setup_tools(self)->list:
        """ setup all tools for currency convertor tool."""

        @tool
        def convert_currency(amount:float,from_currency:str,to_currency:str)->float:
            """ convert the amount from one currency to another""" 
            return self.currency_service.convert(amount,from_currency,to_currency)
        return [convert_currency]