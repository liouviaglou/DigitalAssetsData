#!/usr/local/bin/python3

#https://stackoverflow.com/questions/33767817/how-to-subscribe-to-websocket-api-channel-using-python 

# pip install websocket-client

# from websocket import create_connection
# ws = create_connection("wss://api2.bitfinex.com:3000/ws")
# # ws.connect("wss://api2.bitfinex.com:3000/ws")
# ws.send("LTCBTC")

# # while True:

# #     result = ws.recv()
# #     print ("Received '%s'" % result)

# ws.close()

import json

from websocket import create_connection

import socket
socket.gethostbyname("")

ws = create_connection("wss://api2.bitfinex.com:3000/ws")
#ws.connect("wss://api2.bitfinex.com:3000/ws")
ws.send(json.dumps({
    "event": "subscribe",
    "channel": "book",
    "pair": "BTCUSD",
    "prec": "P0"
}))


while True:
    result = ws.recv()
    result = json.loads(result)
    print ("Received '%s'" % result)

ws.close()