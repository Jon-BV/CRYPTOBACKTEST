import yfinance as yf
import talib as ta
import pandas as pd
import matplotlib.pyplot as plt
power = yf.Ticker("POWERGRID.NS")
df = power.history(start="2020-01-01", end='2021-01-01')
print(df.head())
#simple moving averages rolling 20 days
df['MA'] = ta.SMA(df['Close'],14)
df[['Close','MA']].plot(figsize=(12,12))
plt.show()

#EMA
df['EMA'] = ta.EMA(df['Close'], timeperiod = 14)
df[['Close','EMA']].plot(figsize=(12,10))
plt.show()

#ADX ind.

df['avg'] = ta.ADX(df['High'],df['Low'], df['Close'], timeperiod=14)
df[['avg']].plot(figsize=(12,10))
plt.show()

#Bollinger
df['up_band'], df['mid_band'], df['low_band'] = ta.BBANDS(df['Close'], timeperiod =14)
df[['Close','up_band','mid_band','low_band']].plot(figsize=(12,10))
plt.show()

# RSI
df['Relative'] = ta.RSI(df['Close'],14)
df['Relative'].plot(figsize=(12,10))
plt.show()