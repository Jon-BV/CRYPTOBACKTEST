import ftx
from ftx import FtxClient.websockets as ws_client
from ftx import FtxClient
import datetime
import os

from binance.client import Client

'''
# Historical Data
client = FtxClient()
start_time = 2020-12-31
ends_time = 2021-1-12
symbol = 'ETH-PERP'
depth = 100
order_book = client.get_orderbook(symbol,depth)
prices = client.get_trades('ETH-PERP', 1, datetime.datetime(2020,8,20).timestamp())
print(prices)
'''

# connecting via FTX API

client_ftx = ftx.FtxClient(api_key='rbmwWYf0kOfblMGThnqeNhWprVCtQrlIo7sP450g', api_secret='29aqZWQUyqTRQtMwo8I37OgcKQ-uyDWAzEC-W04g')

data = client_ftx.get_trades('ETH/USD')


# this is live account from Domenik
binance_api = 'eNbs0a81BASGxoRK2R3jZPAXft4wZGOYKg0M2tl3uKTKFhQ7QaFdydMY59GW0UMZ'
binance_secret = 'BrqPRh1kaqEYc7ZcMVdKyLGsHbSCem85OX6QxD6q1A4IJlQ1foqVS1DZklM0KWIH'


#This is testnet-account:jviray2011@hotmail.com(github account)

#binance_api = 'yw3JP6XTheuqu15CRL86jMKrpar00vzpZijb2xF8IuyjRB2JllYQZKbyrLWYq40q'
#binance_secret = 'nx5T7vepwfok1kYEBcgHicZW0nRddCqp5g8WqiRfN8SNsFpv6F0pfS1AQBxl4rPg'


binance_connect = Client(binance_api, binance_secret)

#print('FTX-ETH-USD\n: ',data)

# Uncomment if needed
#print(binance_connect.futures_account_balance())
#client_binance_connect.get_account_status()
clears = ws_client.FtxWebsocketClient(api_key='rbmwWYf0kOfblMGThnqeNhWprVCtQrlIo7sP450g', api_secret='29aqZWQUyqTRQtMwo8I37OgcKQ-uyDWAzEC-W04g')
#ws = client_ftx.FtxWebsocketClient(api_key='rbmwWYf0kOfblMGThnqeNhWprVCtQrlIo7sP450g', api_secret='29aqZWQUyqTRQtMwo8I37OgcKQ-uyDWAzEC-W04g')
#ws.connect()
clears.connect()
for i in range(1,10):
    print(ws.get_ticker(market='ETH-PERP'))
    time.sleep(1)