.. STRAKS Block Explorer API documentation master file, created by
   sphinx-quickstart on Wed Feb 21 22:28:15 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

STRAKS Explorer Python API Documentation
=====================================================

.. image:: straks_icon.png

This library serves as a python interface to access relevant information about the STRAKS crypto currency.

* `STRAKS Website <https://straks.tech>`_

* `STRAKS Github <https://github.com/straks/straks>`_

* `STRAKS Block Explorer <https://straks.info>`_

* `pystraksexplorer Github <https://github.com/fre3man/pystraksexplorer>`_

The library is seperated into two classes, with more to be added in the future.

StraksExplorer - This class exposes functions to interact with the STRAKS blockchain explorer API and the Coin Market Cap API.

* With this class uses can access blockchain information and core STRAKS network stastics. See `STRAKS API <https://straks.info/api>`_ for the official API documentation.

* This class also exposes an endpoint to access the current STRAKS information from Coin Market Cap.

StocksExchange - This class exposes functions to interact with the Socks Exchange API

* With this class users can access Stocks Exchange information about the current markets, prices, orders etc.

* Be default every function is configured to only access STRAKS data, however parameters can be passed to each function to retrieve information from any coin pair.

Click the below links to access each classes documentation.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   StocksExchange
   StraksExplorer





Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
