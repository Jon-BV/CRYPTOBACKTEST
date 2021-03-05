import ftx as ws_client
from datetime import datetime
if __name__ == '__main__':
    # rest = client.FtxClient(api_key=key, api_secret=secret)
    ws = ws_client.FtxWebsocketClient(api_key='rbmwWYf0kOfblMGThnqeNhWprVCtQrlIo7sP450g', api_secret='29aqZWQUyqTRQtMwo8I37OgcKQ-uyDWAzEC-W04g')
    ws.connect()
    for i in range(1, 10):
        print(ws.get_ticker(market='BTC-PERP'))
        time.sleep(1)
        