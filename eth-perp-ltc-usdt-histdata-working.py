# Basic Backtest - Jon BV
# Get Historical data each FTX : ETH-PERP || BINANCE : LTC/USDT
# begin backtest on SPREAD strategy


import ccxt
import pandas as pd

#exch = 'binance' # initial exchange
exch = 'ftx'
t_frame = '1m' # 1-day timeframe, usually from 1-minute to 1-week depending on the exchange
symbol = 'ETH-PERP' # initial symbol
#symbol = 'LTC/USDT'
exchange_list = ['binance','ftx']
 
# Get our Exchange
try:
    exchange = getattr (ccxt, exch) ()
except AttributeError:
    print('-'*36,' ERROR ','-'*35)
    print('Exchange "{}" not found. Please check the exchange is supported.'.format(exch))
    print('-'*80)
    quit()
 
# Check if fetching of OHLC Data is supported
if exchange.has["fetchOHLCV"] != True:
    print('-'*36,' ERROR ','-'*35)
    print('{} does not support fetching OHLC data. Please use another  exchange'.format(exch))
    print('-'*80)
    quit()
 
# Check requested timeframe is available. If not return a helpful error.
if (not hasattr(exchange, 'timeframes')) or (t_frame not in exchange.timeframes):
    print('-'*36,' ERROR ','-'*35)
    print('The requested timeframe ({}) is not available from {}\n'.format(t_frame,exch))
    print('Available timeframes are:')
    for key in exchange.timeframes.keys():
        print('  - ' + key)
    print('-'*80)
    quit()
 
# Check if the symbol is available on the Exchange
exchange.load_markets()
if symbol not in exchange.symbols:
    print('-'*36,' ERROR ','-'*35)
    print('The requested symbol ({}) is not available from {}\n'.format(symbol,exch))
    print('Available symbols are:')
    for key in exchange.symbols:
        print('  - ' + key)
    print('-'*80)
    quit()
 
 
# Get the historical data
data = exchange.fetch_ohlcv(symbol, t_frame)
header = ['Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume']
df = pd.DataFrame(data, columns=header).set_index('Timestamp')
df['symbol'] = symbol
syms = [symbol]
filename = 'ETH-PERP-'+'{}.csv'.format(t_frame)

for exch in exchange_list:
    try:
        exchange = getattr (ccxt, exch) ()
    except AttributeError:
        print('-'*36,' ERROR ','-'*35)
        print('Exchange "{}" not found. Please check the exchange is supported.'.format(exch))
        print('-'*80)
        quit()
    if exchange.has["fetchOHLCV"] != True:
        print('-'*36,' ERROR ','-'*35)
        print('{} does not support fetching OHLC data. Please use another exchange'.format(exch))
        print('-'*80)
        quit()
    if (not hasattr(exchange, 'timeframes')) or (t_frame not in exchange.timeframes):
        print('-'*36,' ERROR ','-'*35)
        print('The requested timeframe ({}) is not available from {}\n'.format(t_frame,exch))
        print('Available timeframes are:')
        for key in exchange.timeframes.keys():
            print('  - ' + key)
        print('-'*80)
        quit()
    exchange.load_markets()
    for coin in exchange.symbols:
        if coin in syms or coin[-3:] != 'LTC/USD':
            continue
        else:
            try:
                data = exchange.fetch_ohlcv(coin, t_frame)
            except:
                continue
            data_df = pd.DataFrame(data, columns=header).set_index('Timestamp')
            data_df['symbol'] = coin
            df = df.append(data_df)
            syms.append(coin)
df.index = df.index/1000 #Timestamp is 1000 times bigger than it should be in this case
df['Date'] = pd.to_datetime(df.index,unit='s')

# Resample the columns

df = df[['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'symbol']]

# Save to CSV for backtest
df.to_csv(filename)