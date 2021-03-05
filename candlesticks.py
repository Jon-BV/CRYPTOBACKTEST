# test in candlesticks but 1 exchange only
import ccxt
from datetime import datetime
import plotly.graph_objects as go
# collect the candlestick data from Binance
binance = ccxt.binance()
trading_pair = 'LTC/ETH'
candles = binance.fetch_ohlcv(trading_pair, '1m')
dates = []
open_data = []
high_data = []
low_data = []
close_data = []
# format the data to match the charting library
for candle in candles:
    dates.append(datetime.fromtimestamp(candle[0] / 1000.0).strftime('%Y-%m-%d %H:%M:%S.%f'))
    open_data.append(candle[1])
    high_data.append(candle[2])
    low_data.append(candle[3])
    close_data.append(candle[4])
# plot the candlesticks
fig = go.Figure(data=[go.Candlestick(x=dates,
                       open=open_data, high=high_data,
                       low=low_data, close=close_data)])
fig.show()