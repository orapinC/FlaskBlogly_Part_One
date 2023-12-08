from forex_python.converter import CurrencyCodes
import requests

def convert(API, KEY, from_curr, to_curr, amount):
    """get converted amount from exchangerate.host API"""    
    url = f'http://api.exchangerate.host/{API}?access_key={KEY}&from={from_curr}&to={to_curr}&amount={amount}'
    response = requests.get(url)
    data = response.json()
    return data["result"] 

def currency_symbol(to_curr):
    """get converted currency symbol"""
    to_curr = to_curr.upper()
    c = CurrencyCodes()
    return c.get_symbol(to_curr)
    

