import pandas as pd
import ccxt
import datetime

exchange = ccxt.ftx()
exchange2 = ccxt.binance()

def gather_data():
    data = exchange.fetch_ohlcv("ETH-PERP")
    df = pd.DataFrame(data)
    df.columns = (["Date Time", "Open", "High", "Low", "Close", "Volume"])
    df["Date Time"] = df["Date Time"].apply(parse_dates)
    df.to_csv("ETH_PERP-FTX.csv")

    data2 = exchange.fetch_ohlcv("LTC/USDT") 
    df = pd.DataFrame(data2)
    df.columns = (["Date Time", "Open", "High", "Low", "Close", "Volume"])
    df["Date Time"] = df["Date Time"].apply(parse_dates)
    df.to_csv("LTCUSDT-Binance.csv")

def parse_dates(ts):
    return datetime.datetime.fromtimestamp(ts/1000.0)

def main():

    gather_data()

if __name__ == "__main__":
    main()