STRAKS Block Explorer Python Module
===================================

.. image:: straks_icon.png

This library serves as a python interface to access relevant information about the STRAKS crypto currency.

* `STRAKS Website <https://straks.tech>`_

* `STRAKS Github <https://github.com/straks/straks>`_

* `STRAKS Block Explorer <https://straks.info>`_


Installation
~~~~~~~~~~~~

* pystraksexplorer is avaiable via pip and is supported for both python 2 and 3:

::

   pip3 install pystraksexplorer


* Or you can download the source code from the github `here <https://github.com/fre3man/pystraksexplorer>`_, and then install the package using

::

    python3 setup.py install

Useage
~~~~~~~~~~~~

The library is seperated into two classes, with more to be added in the future.

StraksExplorer - This class exposes functions to interact with the STRAKS blockchain explorer API and the Coin Market Cap API.

* With this class uses can access blockchain information and core STRAKS network stastics. See straks.info/api for the official API documentation.

* This class also exposes an endpoint to access the current STRAKS information from Coin Market Cap.

StocksExchange - This class exposes functions to interact with the Socks Exchange API

* With this class users can access Stocks Exchange information about the current markets, prices, orders etc.

* Be default every function is configured to only access STRAKS data, however parameters can be passed to each function to retrieve information from any coin pair.


StraksExplorer
~~~~~~~~~~~~~~
.. code:: python

    >>> from pystraksexplorer import StraksExplorer
    >>>
    >>> s = StraksExplorer()
    >>>
    >>> s.get_latest_block()
    {'last_block': 1519821473, 'block_height': 139893, 'difficulty': 1326.42908167, 'hashrate': 112648332742.3684, 'total_coins': 42548130, 'circulating_coins': 2047421.0002712, 'total_txs': 195600, 'total_size': 108500529}
    >>>
    >>> s.get_difficulty()
    1301.18019592
    >>>
    >>> s.get_total_supply()
    42548150.0
    >>>
    >>> s.get_blocks(1,1)
    {'blocks': [{'height': 139896, 'time': 1519821570, 'hash': '000000000024e75415eb76329b745095c54ec3cf4bbf50a146bf3c1cda983b0a', 'size': 707, 'difficulty': 1323.18032665, 'txlength': 3, 'value': 16.59875252}], 'length': 1, 'pagination': {'totalBlocks': 139897, 'totalPages': 139897, 'currentPage': 1, 'limit': 1}}
    >>>
    >>> s.get_block_from_block_hash('000000000024e75415eb76329b745095c54ec3cf4bbf50a146bf3c1cda983b0a')
    {'hash': '000000000024e75415eb76329b745095c54ec3cf4bbf50a146bf3c1cda983b0a', 'size': 707, 'height': 139896, 'version': 536870912, 'merkleroot': 'a2244e8afd226517830d2a13b49581eb5c970d46af30daf5d614238bf594ad5e', 'tx': ['b1fdcbae4ec2817dae32db1ea4b69cc324f885768a932fea9f8dafb655e9481c']
    >>>
    >>> s.get_address_balance('33Ssxmn3ehVMgyxgegXhpLGSBpubPjLZQ6')
    1623050000000
    >>>
    >>> s.get_address_total_sent('33Ssxmn3ehVMgyxgegXhpLGSBpubPjLZQ6')
    0
    >>>
    >>> s.get_masternodes('enabled',1,1)
    {'masternodes': [{'address': 'SWWuKDKaJBfWisJ1ebJmNfUDddh1bS6ske', 'status': 'enabled', 'protocol': 70102, 'active': 268501, 'txIn': '5c59eac2e18fb87e1df56afbc73667c3fc70922283e53c1f3071b87629f0e018', 'lastSeen': 1519823363, 'lastUpdate': 1519823400}], 'pagination': {'totalMasternodes': 91, 'totalPages': 91, 'currentPage': 1, 'limit': 1}}

Coinmarketcap Ticker
~~~~~~~~~~~~~~~~~~~~
.. code:: python

    >>> s.cmc_ticker()
    {'id': 'straks', 'name': 'STRAKS', 'symbol': 'STAK', 'rank': '751', 'price_usd': '0.556911', 'price_btc': '0.00006754', '24h_volume_usd': '8804.2', 'market_cap_usd': '1899674.0', 'available_supply': '3411091.0', 'total_supply': '43187820.0', 'max_supply': '150000000.0', 'percent_change_1h': '-5.86', 'percent_change_24h': '26.99', 'percent_change_7d': '105.91', 'last_updated': '1524165861'}

StocksExchange
~~~~~~~~~~~~~~
.. code:: python

    >>> from pystraksexplorer import StocksExchange
    >>> se = StocksExchange()
    >>>
    >>> se.get_orderbook()
    {'buy': [{'Quantity': '0.00028761', 'Rate': '6.11301372'}, {'Quantity': '0.00120270', 'Rate': '25.56781462'}, {'Quantity': '0.00078476', 'Rate': '16.69365523'}, {'Quantity': '0.09004684', 'Rate': '1915.89029283'}, {'Quantity': '0.00573982', 'Rate': '140.40680039'},
    >>> se.get_market_summary()
    {'currency': 'STAK', 'partner': 'BTC', 'currency_long': 'Straks', 'partner_long': 'Bitcoin', 'min_order_amount': '0.00000010', 'min_buy_price': '0.00000001', 'min_sell_price': '0.00000001', 'buy_fee_percent': '0.2', 'sell_fee_percent': '0.2', 'active': True, 'currency_precision': 8, 'partner_precision': 8, 'market_name': 'STAK_BTC'}
    >>>
    >>>
    >>> se.get_ticker()
    {'min_order_amount': '0.00000010', 'ask': '0.00006', 'bid': '0.000047', 'last': '0.00005898', 'lastDayAgo': '0.00005899', 'vol': '6355.29200243', 'spread': '0', 'buy_fee_percent': '0', 'sell_fee_percent': '0', 'market_name': 'STAK_BTC', 'updated_time': 1524166204, 'server_time': 1524166204}
    >>>
    >>>
    >>> se.get_price()
    {'buy': '0.00004705', 'sell': '0.00005886', 'market_name': 'STAK_BTC', 'updated_time': 1524166201, 'server_time': 1524166201}
    >>>
    >>>
    >>> se.get_trade_history()
    [{'timestamp': 1524158309, 'quantity': '20.00000000', 'price': '0.00005898', 'type': 'BUY'}, {'timestamp': 1524158245, 'quantity': '77.00000000', 'price': '0.00004705', 'type': 'SELL'}, {'timestamp': 1524158151, 'quantity': '20.00000000', 'price': '0.00005898', 'type': 'BUY'},
    >>>
    >>>
    >>> se.get_grafic()
    {'pair': 'STAK_BTC', 'interval': '1D', 'order': 'ASC', 'since': '2018-04-18 19:30:00', 'end': '2018-04-19 19:31:03', 'count_pages': 1, 'count': '100', 'current_page': 1, 'graf': [{'open': '0.00005102', 'close': '0.00005102', 'low': '0.00005102', 'high': '0.00005102', 'date': '2018-04-18 22:00:00'}

As mentioned this API can be extended beyond just STAK by supplying arguments to each function

.. code:: python

    >>> se.get_price(currency1='ETH', currency2='BTC')
    {'buy': '0.06510204', 'sell': '0.06699999', 'market_name': 'ETH_BTC', 'updated_time': 1524166381, 'server_time': 1524166381}
    >>>
    >>> se.get_ticker(currency1='ETH', currency2='BTC')
    {'min_order_amount': '0.00001000', 'ask': '0.06699999', 'bid': '0.06261', 'last': '0.06699999', 'lastDayAgo': '0.06275', 'vol': '60.80603293', 'spread': '0', 'buy_fee_percent': '0', 'sell_fee_percent': '0', 'market_name': 'ETH_BTC', 'updated_time': 1524166381, 'server_time': 1524166381}
    >>>


Full documentation for the module can be found at the link below, and can also be built using "make html" from the docs folder.

- `Full Documentation <http://pystraksexplorer.readthedocs.io/en/latest/>`_
