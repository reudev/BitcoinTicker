#import libs
from urllib import request
import json
from time import sleep

#Function to Pull BTC USD price from MTGox
def PricePull():
 persistant_thing = None
 while True:
  req = request.urlopen('http://data.mtgox.com/api/2/BTCUSD/money/ticker_fast')
  encoding = req.headers.get_content_charset()
  obj = json.loads(req.read().decode(encoding))
  print ("MTGox USD Buy Price:", obj['data']['buy']['display_short'])
  sleep(10) 
 
PricePull() #Calls PricePull function
