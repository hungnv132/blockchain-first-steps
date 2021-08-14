import os
from dotenv import load_dotenv
from web3 import Web3

load_dotenv()


class BlockchainNetwork(object):

    def __init__(self, provider_url=None):
        provider_url = provider_url or os.getenv('BLOCKCHAIN_PROVIDER_URL')
        if not provider_url:
            raise Exception("Please setting 'BLOCKCHAIN_PROVIDER_URL'")

        provider = self._detect_provider(provider_url)
        self.w3 = Web3(provider)

    def _detect_provider(self, provider_url):
        if provider_url.startswith('http'):
            return Web3.HTTPProvider(provider_url)
        if provider_url.startswith('ws'):
            return Web3.WebsocketProvider(provider_url)
        return Web3.IPCProvider(provider_url)  # may be wrong

    @property
    def is_connected(self):
        """True or False"""
        return self.w3.isConnected()

    @property
    def owner_address(self):
        return self.get_address_from_private_key(
            key=os.getenv('BLOCKCHAIN_OWNER_PRIVATE_KEY')
        )

    def create_account(self):
        account = self.w3.eth.account.create()
        acc_info = {
            'address': account.address,
            'private_key': account.key.hex()
        }
        return acc_info

    def get_address_from_private_key(self, key):
        return self.w3.eth.account.from_key(key).address
