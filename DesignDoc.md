# Design Doc:
#### python websocket implementation of bitfinex data acquisiton

Despite my extensive experience with various forms of data acquisition in python, this was my first attempt at pulling data from bitfinex and my first time using websockets. Upon intially diving into the problem, I familiarized myself with websockets and bitfinex. I considered implementing a solution more or less from scratch (using the websockets python package) until I found BtfxWss, a Bitfinex Websocket API Client written in Python3. This is not the most well documented or widely used package so the most time consuming portion was understanding the arguments passed in and the data returned. 

At first, I thought that the problem required a pull of ticker data due to the 'price' and 'volume' keys in the requested output. However, 'is_buy' as a key does not make sense for this high level, daily overview -- itmakes sense for ticker data, which lists individual buys and sells (positive and negative amounts, respectively -- I assume).

Thus, my final solution returns, for a given set of 5 symbols, the ticker data formatted as per the problem statement.

The data is requested and returned via command line terminal, executed as outlined below. In order to extend of industrialize it, the first thing I would do would be to write the output to a database. I would also build in better error handling to make this script resilient to systemic data download fails (system derived issues) and the possibility of malformed symbol arguments/ flexible number of symbols (user derived issues). I would also supply a requirements file and packaging the code. Further more, I would make the package dlexible enough to support various python verisons.

This code uses python 3. To run the websocket implementation of bitfinex data acquisition, please execute the following from within the same directory as the btfxwss_play.py file. You can replace the 5 string arguments with the valid symbols of your choice.

``python btfxwss_play.py "btcusd" "ltcusd" "ltcbtc" "ethusd" "ethbtc"``

