import json
import requests

# api key/request url
key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

# requests data from url
data = requests.get(key)
data = data.json()
print(f"{data['symbol']} price is {data['price']}")