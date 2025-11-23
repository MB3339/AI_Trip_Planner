from utils.expense_calculator import Calculator
from typing import List
from langchain_core.tools import tool


class CalculatorTool:
    def __init__(self):
        self.calculator=Calculator()
        self.calculator_tool_list=self._setup_tools()

    def _setup_tools(self)->list:
        """ setup all tools for the calculator tool."""
        @tool 
        def estimate_total_hotel_cost(price_per_night:float,total_days:int)->float:
            """ Estimate total hotel cost """
            return self.calculator.multiply(price_per_night,total_days)
        
        @tool 
        def calculate_total_expense(*costs:float)->float:
            """ Calculate total expense of the trip"""
            return self.calculator.calculate_total(*costs)
        
        @tool
        def calculate_daily_budget(total_costs:float, days: int)->float:
            """ calculate daily budget"""
            return self.calculator.calculate_daily_budget(total_costs,days)
        
        return [estimate_total_hotel_cost, calculate_total_expense, calculate_daily_budget]
    