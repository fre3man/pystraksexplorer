STRAKS Block Explorer Python Module
===================================

.. image:: straks_icon.png

A Python module for interacting with the STRAKS block explorer API located at https://straks.info

For information on STRAKS please visit the website located at https://straks.io


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

See below for useage examples

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
    {'hash': '000000000024e75415eb76329b745095c54ec3cf4bbf50a146bf3c1cda983b0a', 'size': 707, 'height': 139896, 'version': 536870912, 'merkleroot': 'a2244e8afd226517830d2a13b49581eb5c970d46af30daf5d614238bf594ad5e', 'tx': ['b1fdcbae4ec2817dae32db1ea4b69cc324f885768a932fea9f8dafb655e9481c', 'f6004c28c9950a12150f8327507534d2f0dbcaef3262668cbd81870ef6e374f0', 'be25c161e4be9503d3e1f8535968dd0c62dd592baa833abf1d31e281779a769b'], 'time': 1519821570, 'nonce': 2085421746, 'bits': '1b318745', 'difficulty': 1323.18032665, 'chainwork': '000000000000000000000000000000000000000000000000104c8f7548d78b30', 'confirmations': 5, 'previousblockhash': '0000000000061ff0bdf7eec0bcb54fe5d20af2ddbfa1bbf675b40cbae6a37b2e', 'nextblockhash': '00000000001d04f4e8bbab59eb49dbd0b9f208cad11e909438e26b83ff1daaa8', 'reward': 10, 'value': 16.59884292, 'isMainChain': True, 'poolInfo': {}}
    >>>
    >>> s.get_address_balance('33Ssxmn3ehVMgyxgegXhpLGSBpubPjLZQ6')
    1623050000000
    >>>
    >>> s.get_address_total_sent('33Ssxmn3ehVMgyxgegXhpLGSBpubPjLZQ6')
    0
    >>>
    >>> s.get_masternodes('enabled',1,1)
    {'masternodes': [{'address': 'SWWuKDKaJBfWisJ1ebJmNfUDddh1bS6ske', 'status': 'enabled', 'protocol': 70102, 'active': 268501, 'txIn': '5c59eac2e18fb87e1df56afbc73667c3fc70922283e53c1f3071b87629f0e018', 'lastSeen': 1519823363, 'lastUpdate': 1519823400}], 'pagination': {'totalMasternodes': 91, 'totalPages': 91, 'currentPage': 1, 'limit': 1}}


Full documentation for the module can be found at the link below, and can also be built using "make html" from the docs folder.

- `Full Documentation <http://pystraksexplorer.readthedocs.io/en/latest/>`_

