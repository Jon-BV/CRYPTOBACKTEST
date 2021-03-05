import os
import pandas as pd
import math
import os.path
import time
from ftx import *
from binance.client import Client
from binance.websockets import BinanceSocketManager # websocket
from datetime import timedelta, datetime
from dateutil import parser
from tqdm import tqdm_notebook
from twisted.internet import reactor


### Binance API
binance_api_key = 'eNbs0a81BASGxoRK2R3jZPAXft4wZGOYKg0M2tl3uKTKFhQ7QaFdydMY59GW0UMZ'   
binance_api_secret = 'BrqPRh1kaqEYc7ZcMVdKyLGsHbSCem85OX6QxD6q1A4IJlQ1foqVS1DZklM0KWIH'

client = Client(binance_api_key,binance_api_secret)
ltcusd_price = client.get_symbol_ticker(symbol="LTCUSDT")



'''
#print in dictionary form
print(ltcusd_price)

#or
print(ltcusd_price["price"]) # just a total closing
'''

def ltcusd_trade_history(msg):
    if msg['e'] != 'error':
        print(msg['c'])
        ltcusd_price['last'] = msg['c']
        ltcusd_price['bid'] = msg['b']
        ltcusd_price['last'] = msg['a']
    else:
        ltcusd_price['error'] = True

#test using Websocket
websocket_api = BinanceSocketManager(client)
connect = websocket_api.start_symbol_ticker_socket('LTCUSDT', ltcusd_trade_history)
websocket_api.start()
#print(client.futures_get_open_orders())
