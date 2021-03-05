import pandas as pd
import math
import os.path
import time
import ftx

from datetime import timedelta, datetime
from dateutil import parser
from tqdm import tqdm_notebook

'''
eth_api_key ='rbmwWYf0kOfblMGThnqeNhWprVCtQrlIo7sP450g'
eth_api_secret = '29aqZWQUyqTRQtMwo8I37OgcKQ-uyDWAzEC-W04g'
'''

client_ftx = ftx.FtxClient(api_key='rbmwWYf0kOfblMGThnqeNhWprVCtQrlIo7sP450g', api_secret='29aqZWQUyqTRQtMwo8I37OgcKQ-uyDWAzEC-W04g')
data = client_ftx.get_trades('ETH-PERP')
data = pd.DataFrame(client_ftx.get_all_trades('ETH-PERP'))
#data.

#data2 = client_ftx.get_open_orders('ETH/USD')
data2 = client_ftx.get_order_history('ETH/USD')
result = pd.DataFrame(client_ftx.get_positions())
result2 = pd.DataFrame(client_ftx.get_trades('ETH-PERP'))
result2.to_csv('trades-eth-perp.csv')
#result2.to_csv('FTX-ETH-trades.csv')
#result.to_csv('FTX-ETH-USD.csv')
print(result2)