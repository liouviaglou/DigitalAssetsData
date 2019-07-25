#!/usr/local/bin/python3

#https://github.com/Crypto-toolbox/btfxwss

import logging
import time
import sys
from datetime import datetime
import json
from btfxwss import BtfxWss

# python btfxwss_play.py "btcusd" "ltcusd" "ltcbtc" "ethusd" "ethbtc"
sym_list = [sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]]
sym_list = [s.upper() for s in sym_list]

def parse_ticker_data(sym, data):
    keys = ["bid", "bidSize", "ask", "askSize", "dailyChange", "dailyChangePer", "price", "volume", "high", "low"]
    data_dict = {k:r for k, r in zip(keys, data[0][0])}
    data_dict["symbol"] = sym
    data_dict["datetime"] = datetime.utcfromtimestamp(data[-1]).strftime('%Y-%m-%d-%H-%M-%S')
    return data_dict

def parse_trades_data(sym, data):
    keys = ["seq", "id", "volume", "price"]
    data_lst = []
    for d in data[0][0]:
        dct = {k:r for k, r in zip(keys, d)}
        dct["symbol"] = sym
        dct["datetime"] = datetime.utcfromtimestamp(data[-1]).strftime('%Y-%m-%d-%H-%M-%S')
        del dct["seq"]
        del dct["id"]
        data_lst.append(dct)
    return data_lst

    
wss = BtfxWss()
wss.start()

while not wss.conn.connected.is_set():
    time.sleep(1)
    
def get_ticker(sym):
    # Ticker: ticker feed
    # Ticker: The ticker is a high level overview of the state of the market. 
    # It shows you the current best bid and ask, as well as the last trade price. 
    # It also includes information such as daily volume and how much the price
    # has moved over the last day.
    wss.subscribe_to_ticker(sym)
    queue = wss.tickers(sym)
    lst = queue.get()
    dct = parse_ticker_data(sym,lst)
    output = { key:value for key,value in dct.items() if key in ["symbol", "datetime", "price", "volume"]} 
    wss.unsubscribe_from_ticker(sym)
    return(output)

def get_trades(sym):
    # Trades: trade feed
    # This channel sends a trade message whenever a trade occurs at Bitfinex. 
    # It includes all the pertinent details of the trade, such as price, size and time.
    wss.subscribe_to_trades(sym)
    queue = wss.trades(sym)
    lst = queue.get()
    lst_dcts = parse_trades_data(sym,lst)
    for l in lst_dcts:
        l["is_buy"] = 1 if l["volume"]>0 else 0
    output = lst_dcts
    wss.unsubscribe_from_trades(sym)
    return(output)


sym_list_trades = []

for sym in sym_list:
    print("trying "+sym)
    try:
        sym_list_trades.append(get_trades(sym))   
        print("success "+sym)
    except:
        print("error "+sym)

sym_list_trades = sum(sym_list_trades, [])
print(sym_list_trades)