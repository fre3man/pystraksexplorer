import unittest

from pystraksexplorer import StraksExplorer, StocksExchange


class TestStraksExplorer(unittest.TestCase):

    def test_get_latest_block(self):
        self.assertTrue(StraksExplorer().get_latest_block().get('last_block'))

    def test_get_difficulty(self):
        self.assertTrue(str(StraksExplorer().get_difficulty()))

    def test_get_total_supply(self):
        self.assertTrue(str(StraksExplorer().get_total_supply()))

    def test_get_circulating_supply(self):
        self.assertTrue(str(StraksExplorer().get_circulating_supply()))

    def test_get_blocks(self):
        self.assertTrue(str(StraksExplorer().get_blocks(25, 3)))

    def test_get_block_from_blockhash(self):
        self.assertTrue(str(StraksExplorer().get_block_from_block_hash('000000000005e7e241410c528362cd02eeaa026237eb08c502ef802fa9d00cf8')))

    def test_get_blockhash_from_blockheight(self):
        self.assertTrue(str(StraksExplorer().get_block_hash_from_block_height('foo').get('errors')))

    def test_get_raw_block_from_blockhash(self):
        self.assertTrue(str(StraksExplorer().get_raw_block_from_block_hash('foo').get('errors')))

    def test_get_raw_block_from_blockheight(self):
        self.assertTrue(str(StraksExplorer().get_raw_block_from_block_height('foo').get('errors')))

    def test_get_transcation_data_from_transaction_hash(self):
        self.assertTrue(str(StraksExplorer().get_transcation_data_from_transaction_hash('1819fd02b866f14686c68c76af446857abd1d80798947b51fb91381a333e9f05').get('txid')))

    def test_get_transcations_from_address(self):
        self.assertTrue(str(StraksExplorer().get_transactions_from_address('000000000005e7e241410c528362cd02eeaa026237eb08c502ef802fa9d00cf8', '1', '5', '0').get('txs')))

    def test_get_raw_transaction_data_from_transaction_hash(self):
        self.assertTrue(str(StraksExplorer().get_raw_transaction_data_from_transaction_hash('1819fd02b866f14686c68c76af446857abd1d80798947b51fb91381a333e9f05').get('txs')))

    def test_get_address_balance(self):
        self.assertTrue(str(StraksExplorer().get_address_balance('SjtUfJU17izF9yh5hnCmtWmGyhhCv83eHb')))

    def test_get_address_total_received(self):
        self.assertTrue(str(StraksExplorer().get_address_total_received('SjtUfJU17izF9yh5hnCmtWmGyhhCv83eHb')))

    def test_get_address_total_sent(self):
        self.assertTrue(str(StraksExplorer().get_address_total_sent('SjtUfJU17izF9yh5hnCmtWmGyhhCv83eHb')))

    def test_get_richlist(self):
        self.assertTrue(str(StraksExplorer().get_richlist().get('addresses')))

    def test_get_masternodes(self):
        self.assertTrue(str(StraksExplorer().get_masternodes('enabled', 1, 10).get('masternodes')))

    def test_get_difficulty_chart(self):
        self.assertTrue(StraksExplorer().get_difficulty_chart())

    def test_get_hashrate_chart(self):
        self.assertTrue(StraksExplorer().get_hashrate_chart())

    def test_get_transcation_chart(self):
        self.assertTrue(StraksExplorer().get_transaction_chart())


class TestStocksExchange(unittest.TestCase):

    def test_get_orderbook(self):
        self.assertTrue(StocksExchange().get_orderbook())

    def test_get_market_summary(self):
        self.assertTrue(StocksExchange().get_market_summary().get('currency'))

    def test_get_ticker(self):
        self.assertTrue(StocksExchange().get_ticker().get('ask'))

    def test_get_price(self):
        self.assertTrue(StocksExchange().get_price().get('buy'))

    def test_trade_history(self):
        self.assertTrue(len(StocksExchange().get_market_summary()))

    def test_get_grafic(self):
        self.assertTrue(StocksExchange().get_grafic().get('pair'))



if __name__ == '__main__':
    unittest.main()
