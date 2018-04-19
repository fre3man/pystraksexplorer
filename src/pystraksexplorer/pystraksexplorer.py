import requests
import sys


class StraksExplorer:

    def __init__(self, api_base='https://api.straks.info/v2/'):
        if sys.version_info[0] < 3:
            if api_base == 'https://api.straks.info/v2/':
                api_base = api_base.replace('https', 'http')
        self.api_base = api_base
        self.cmc_base = 'https://api.coinmarketcap.com/v1/'

    """ Blockchain Data """
    def get_latest_block(self):
        """
        Fetch the latest blockchain statistics

        :endpoint: /statistics/latest
        :return: latest straks block in json object
        """
        return requests.get(self.api_base + 'statistics/latest').json()

    def get_difficulty(self):
        """
        Fetch block difficulty

        :endpoint: /raw/difficulty
        :return: the current difficulty on the network
        """
        return requests.get(self.api_base + 'raw/difficulty').json()

    def get_total_supply(self):
        """
        Fetch coin supply

        :endpoint: /raw/totalSupply
        :return: the total supply
        """
        return requests.get(self.api_base + 'raw/totalSupply').json()

    def get_circulating_supply(self):
        """
        Fetch circulating supply

        :endpoint: /raw/totalSupply
        :return: the circulating supply
        """
        return requests.get(self.api_base + 'raw/circSupply').json()

    """ Block Data """
    def get_blocks(self, limit, page):
        """
        Fetch a list of recent blocks

        :param int limit: Blocks to return per page
        :param int page: Page number to return
        :endpoint: /blocks?limit={limit}&page={page}
        :return: blocks
        """
        return requests.get(self.api_base + 'blocks?limit=%s&page=%s'%(limit, page)).json()

    def get_block_from_block_hash(self, block_hash):
        """
        Fetch block data for given blockhash

        :param string block hash:  Block hash to lookup
        :endpoint: /blocks/{blockHash}
        :return: block
        """
        return requests.get(self.api_base + 'block/%s'%(block_hash)).json()

    def get_block_hash_from_block_height(self, block_height):
        """
        Fetch block hash for given block height

        :param int block height: Block height to lookup
        :endpoint: /blocks-index/{blockHeight}
        :return: block hash
        """
        return requests.get(self.api_base + 'block-index/%s'%(block_height)).json()

    def get_raw_block_from_block_hash(self, block_hash):
        """
        Fetch raw block data for given block hash

        :param string block_hash: the block height to retrieve a block from
        :endpoint: /rawblock/{blockHash}
        :return: raw block
        """
        return requests.get(self.api_base + 'rawblock/%s'%(block_hash)).json()

    def get_raw_block_from_block_height(self, block_height):
        """
        Fetch raw block data for given block height

        :param string block_height: the block height to retrieve a block from
        :endpoint: /rawblock/{blockHeight}
        :return: raw block
        """
        return requests.get(self.api_base + 'rawblock/%s'%(block_height)).json()

    """ Transaction Data """
    def get_transcation_data_from_transaction_hash(self, transaction_hash, summary=0):
        """
        Fetch transaction data for given transaction hash

        :param string transcation_hash: Transaction hash to lookup
        :param int summary: Group input/output amounts by address / 0 = no, 1 = yes / Default 0
        :endpoint: /tx/{transactionHash}?summary={summary}
        :return: transaction data
        """
        return requests.get(self.api_base + 'tx/%s?%s'%(transaction_hash, summary)).json()

    def get_transactions_from_blockhash(self, block_hash, page, limit, summary=0):
        """
        Fetch all transactions associated with given blockhash

        :param string block_hash: Block hash to lookup
        :param int page: Page number
        :param int limit: Records per page
        :param int summary: Ignore inputs/outputs (i.e. fetch transaction header details only)
        :endpoint: /txs?block={blockHash}&pageNum={page}&limit={limit}&summary={summary}
        :return: transaction data
        """
        return requests.get(self.api_base + 'txs?block=%s&pageNum=%s&limit=%s&summary=%s'%(block_hash, page, limit, summary)).json()

    def get_transactions_from_address(self, address, page, limit, summary=0):
        """
        Fetch all transactions associated with given address

        :param string address: Address to lookup
        :param int page: Page number
        :param int limit: Records per page
        :param int summary: Ignore inputs/outputs (i.e. fetch transaction header details only)
        :endpoint: /txs?address={address}&pageNum={page}&limit={limit}&summary={summary}
        :return: transaction data
        """
        return requests.get(self.api_base + 'txs?address=%s&pageNum=%s&limit=%s&summary=%s'%(address, page, limit, summary)).json()

    def get_raw_transaction_data_from_transaction_hash(self, transaction_hash):
        """
        Fetch raw transaction data for given transaction hash

        :param string transaction_hash: Transaction hash to lookup
        :endpoint: /rawtx/{transactionHash}
        :return: raw transaction data
        """
        return requests.get(self.api_base + 'rawtx/%s'%(transaction_hash)).json()

    """ Address Data """
    def get_address_balance(self, address):
        """
        Fetch raw address balance

        :param string address: Wallet address
        :endpoint: /addr/{address}/balance
        :return: address balance
        """
        return requests.get(self.api_base + 'addr/%s/balance'%(address)).json()

    def get_address_total_received(self, address):
        """
        Fetch raw address total received

        :param string address: Wallet address
        :endpoint: /addr/{address}/totalReceived
        :return: total received
        """
        return requests.get(self.api_base + 'addr/%s/totalReceived'%(address)).json()

    def get_address_total_sent(self, address):
        """
        Fetch raw address total sent

        :param string address: Wallet address
        :endpoint: /addr/{address}/totalSent
        :return: total sent
        """
        return requests.get(self.api_base + 'addr/%s/totalSent'%(address)).json()

    """ General purpose Data """
    def get_richlist(self, limit=100):
        """
        Fetch richlist

        :param int limit: limit of richlist entries to return
        :endpoint: /richlist?limit={limit}
        :return: richlist
        """
        return requests.get(self.api_base + 'richlist?limit=%s'%(limit)).json()

    def get_masternodes(self, status, page, limit):
        """
        Fetch masternodes

        :param string status: Either enabled, vin_spent, expired or remove. Leave blank for all.
        :param int page: Page number
        :param int limit: Records per page
        :endpoint: /masternodes?status={status}&limit={limit}&page={page}
        :return: masternode list
        """
        return requests.get(self.api_base + 'masternodes?status=%s&limit=%s&page=%s'%(status, limit, page)).json()

    """ Chart Data """
    def get_difficulty_chart(self, days=1):
        """
        Fetch difficulty chart

        :param string days: Total days to fetch. Default 1 / Max 7
        :endpoint: /charts/difficulty?days={days}
        :return: difficulty chart data
        """
        return requests.get(self.api_base + 'charts/difficulty?days=%s'%(days)).json()

    def get_hashrate_chart(self, days=1):
        """
        Fetch hashrate chart data

        :param string days: Total days to fetch. Default 1 / Max 7
        :endpoint: /charts/hashrate?days={days}
        :return: hashrate chart data
        """
        return requests.get(self.api_base + 'charts/hashrate?days=%s'%(days)).json()

    def get_transaction_chart(self, days=1):
        """
        Fetch transaction chart data

        :param string days: Total days to fetch. Default 1 / Max 7
        :endpoint: /charts/transactions?days={days}
        :return: transaction chart data
        """
        return requests.get(self.api_base + 'charts/transactions?days=%s'%(days)).json()

    """ Price / Exchange Data """

    def cmc_ticker(self, coin='STRAKS', currency='USD'):
        """
        Fetch current ticker of {coin} in the specified {currency} from coinmarketcap api

        :param string currency: The currency code to return the results in
        :apisource: api.coinmarketcap.com
        :endpoint: /v1/ticker/straks/?convert={currency}
        :return: ticker
        """

        return requests.get(self.cmc_base + 'ticker/%s/?convert=%s'%(coin, currency)).json()[0]


