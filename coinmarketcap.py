#!/usr/bin/python

import sys
import urllib2
import json
from tabulate import tabulate

def get_position(json):
    try:
        return int(json['position'])
    except KeyError:
        return 1000

if len(sys.argv) == 2:
        count = int(sys.argv[1])

count = 10
currency = "usd"
url = "http://coinmarketcap.northpole.ro/api/v5/all.json"
headers = ["Position","Name","Market Cap","Price","Available Supply","Volume 24h","Change 7h"]

data = urllib2.urlopen(url).read()
data = json.loads(data)['markets']
data.sort(key=get_position)
btc_price = float(data[0]['price'][currency])

table = []
for d in data[0:count]:
        volume = float(d['volume24']['btc'])*btc_price
        table.append([d['position'],d['name'],d['marketCap'][currency],d['price'][currency],d['marketCap']['btc'],volume,d['change7h'][currency]])

print tabulate(table,headers,numalign="left",stralign="left",floatfmt=".2f")

