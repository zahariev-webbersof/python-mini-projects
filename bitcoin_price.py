import requests
from bs4 import BeautifulSoup as bs

URL = 'https://coinmarketcap.com/currencies/bitcoin/'
req = requests.get(URL)

soup = bs(req.content, 'html.parser')

price = soup.find('div', {'class': 'priceValue'})
extract = price.select_one('span')

print(f'Bitcoin price today is {extract.text} per (BTC / USD)')