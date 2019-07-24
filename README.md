# Problem Statement:

Write a working python websocket implementation that pulls trade data from bitfinex.  The implementation should subscribe to and write any five valid symbols.  There is additional help available, but your submission will lose some credit should you need it.             

## Required output format: 
 (expected type/format provided)         
 [symbol="string", datetime="yyyy-mm-dd-hh-mm-ss-msc", price="float", volume="float", is_buy:"boolean"]


## Design Doc reqs:
We'd also like your design document ... which can be a simple text file ... but should describe what you thought about as you architected and implemented the solution, specifically but not limited to: where your solution has limitations, how you would extend/industrialize it  .      
Note:Bitfinex will send you more data than requested above. Please don't include it in your output. 

# Lab Notebook:

## 07/23/19
Using btfxwss. wss.ticker('xxxx').get() returns a list plus some additional values -- mapping to data in required output format
