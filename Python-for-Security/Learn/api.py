
#---------------------------  Public API  ---------------------------
https://github.com/public-apis/public-apis

#---------------------------  curl  ---------------------------
curl https://api.coinbase.com/v2/prices/spot\?currency\=USD

#---------------------------  request  ---------------------------
response = request.get(‘https://api.livecoin.net/exchange/ticker?currencyPair=BTC/USD’)
response 
#<Response [200]>
response.text
price = response.json()
price[‘high’]
#6599.99999

pip install pysocks
python

import requests
response = requests.get(‘https://api.coinbase.com/v2/prices/spot\?currency\=USD’, proxies={‘https’: ‘socks5://127.0.0.1:1080’})
print (response)
response.json()
response.json[‘data’]
float(response.json[‘data’][‘amount’])
5670
c

#---------------------------  Beautiful Soap  ---------------------------
response = request.get(‘https://bama.ir/car/all-brands/all-models/all-trims?price=30-40’)
from bs4 import BeautifulSoup
soup = BeautifulSoup(response .text, ‘html.parser’)
soup
val = soup.find(‘h2’)
val
soup.find_all(‘h2’)
result = soup.find_all(‘h2’)
result[1]
#<h2 itemprop=”name”>تیپ5  , 206  , پژو</h2>
val1 = result[1]
val1.attrs
#{‘itemprop’: ‘name’}
r = soup.find(‘h2’, attrs={‘itemprop’: ‘name’})
r.text
import re
re.sub(r’\s+’, ‘ ’, r.text)
‘    1395,   تیپ 5 , 206 , پژو   ’
re.sub(r’\s+’, ‘ ’, r.text).strip()
‘1395, تیپ 5 , 206 , پژو’
all_cars = soup.find_all(‘h2’, attrs={‘itemprop’: ‘name’})
for car in all_cars:
    print (re.sub(r’\s+’, ‘ ’, car.text).strip())

#---------------------------  sms  ---------------------------
def inform_jadi(price):
    API_key = ‘4D654656’B65465464656SRT654635G4FK6U4’
    url = ‘https://api.kavenegar.com/v1/%s/sms/send.json’ % API_Key
    payload = {‘receptor’: ‘09127864996’, ‘message’: ‘price is as low as %i’ % price}
    response = requests.post(url, data=payload)
    print(response)
