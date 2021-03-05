import ccxt
from pprint import pprint

exchange = ccxt.ftx({'enableRateLimit': True})
since = exchange.parse8601('2019-10-01T00:00:00Z')
params = {'market_name': 'ETH-PERP'}  
limit = None

ohlcv = exchange.fetch_ohlcv('BTC-MOVE-2020Q4', '1h', since, limit, params)
pprint(ohlcv)