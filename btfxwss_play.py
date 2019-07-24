#!/usr/local/bin/python3

#https://github.com/Crypto-toolbox/btfxwss

import logging
import time
import sys

from btfxwss import BtfxWss
    
log = logging.getLogger(__name__)

fh = logging.FileHandler('test.log')
fh.setLevel(logging.DEBUG)
sh = logging.StreamHandler(sys.stdout)
sh.setLevel(logging.DEBUG)

log.addHandler(sh)
log.addHandler(fh)
logging.basicConfig(level=logging.DEBUG, handlers=[fh, sh])
    

wss = BtfxWss()
wss.start()

while not wss.conn.connected.is_set():
    time.sleep(1)

# Subscribe to some channels
wss.subscribe_to_ticker('BTCUSD')
wss.subscribe_to_order_book('BTCUSD')

# Do something else
t = time.time()
while time.time() - t < 10:
    pass

# Accessing data stored in BtfxWss:
ticker_q = wss.tickers('BTCUSD')  # returns a Queue object for the pair.

# print(ticker_q)

# print(ticker_q.empty)

# print(ticker_q.get())
# (
#     [[9677.4, 26.1702001, 
#       9677.5, 26.6461616, , 
#       -613.99382809, -0.0597, , 
#       9676.00617191, 
#       10491.7425515, , 
#       10291, 
#        9625]], 
#       1563927913.537417
# )

trade_q = wss.trades('BTCUSD') 
print (trade_q.get())


# while not ticker_q.empty():
#     print(ticker_q.get())

# Unsubscribing from channels:
wss.unsubscribe_from_ticker('BTCUSD')
wss.unsubscribe_from_order_book('BTCUSD')

# Shutting down the client:
wss.stop()