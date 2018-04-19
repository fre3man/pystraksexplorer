import requests
import sys


class StocksExchange:

    def __init__(self, api_base='https://stocks.exchange/api2/'):
        if sys.version_info[0] < 3:
            if api_base == 'https://api.straks.info/v2/':
                api_base = api_base.replace('https', 'http')
        self.api_base = api_base

    def get_orderbook(self, currency1='STAK', currency2='BTC'):
        """
        Fetch the orderbook for currency1/currency2 pair from stocks exchange

        :param string currency1: Symbol of first currency in pair
        :param string currency2: Symbol of second currency in pair
        :return: Order book for currency pair
        """
        return requests.get(self.api_base + 'orderbook?pair=%s_%s'%(currency1, currency2)).json().get('result')

    def get_market_summary(self, currency1='STAK', currency2='BTC'):
        """
        Fetch the market summary for currency1/currency2 pair from stocks exchange

        :param string currency1: Symbol of first currency in pair
        :param string currency2: Symbol of second currency in pair
        :return: Market summary for currency pair
        """
        return requests.get(self.api_base + 'market_summary/%s/%s'%(currency1, currency2)).json()

    def get_ticker(self, currency1='STAK', currency2='BTC'):
        """
        Fetch the ticker for currency1/currency2 pair from stocks exchange

        :param string currency1: Symbol of first currency in pair
        :param string currency2: Symbol of second currency in pair
        :return: Ticker for currency pair
        """
        res = requests.get(self.api_base + 'ticker').json()
        coin_ticker = {}
        for tick in res:
            if tick.get('market_name') == '%s_%s'%(currency1, currency2):
                coin_ticker = tick

        return coin_ticker

    def get_price(self, currency1='STAK', currency2='BTC'):
        """
        Fetch the price for currency1/currency2 pair from stocks exchange

        :param string currency1: Symbol of first currency in pair
        :param string currency2: Symbol of second currency in pair
        :return: Price for currency pair
        """
        res = requests.get(self.api_base + 'prices').json()
        coin_price = {}
        for tick in res:
            if tick.get('market_name') == '%s_%s'%(currency1, currency2):
                coin_price = tick

        return coin_price

    def get_trade_history(self, currency1='STAK', currency2='BTC'):
        """
        Fetch the trade history for currency1/currency2 pair from stocks exchange

        :param string currency1: Symbol of first currency in pair
        :param string currency2: Symbol of second currency in pair
        :return: Trade history for currency pair
        """
        return requests.get(self.api_base + 'trades?pair=%s_%s'%(currency1, currency2)).json().get('result')

    def get_grafic(self, currency1='STAK', currency2='BTC', interval='1D', order='ASC', count=100):
        """
        Fetch the grafic for currency1/currency2 pair from stocks exchange

        :param string currency1: Symbol of first currency in pair
        :param string currency2: Symbol of second currency in pair
        :param: string interval: Interval of the grafic to return, default 1D. (ex. 20D, 3M, 1Y)
        :param: string order: Order to return the results in (ASC, DEC) default = ASC
        :param: int count: The number of results to return
        :return: Grafic for currency pair
        """
        return requests.get(self.api_base + 'grafic_public?pair=%s_%s&interval=%s&order=%s&count=%s'%(currency1, currency2, interval, order, count)).json().get('data')