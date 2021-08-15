import os
import json
from dotenv import load_dotenv
from web3 import Web3

load_dotenv()


class ContractABIUtil(object):

    @classmethod
    def get_ERC20_ABI(cls):
        return json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Approval","type":"event"}]')  # noqa: 501


class BlockchainNetwork(object):

    def __init__(self, provider_url=None):
        self.provider_url = provider_url or os.getenv('BLOCKCHAIN_PROVIDER_URL')
        if not self.provider_url:
            raise Exception("Please setting 'BLOCKCHAIN_PROVIDER_URL'")

        provider = self._detect_provider(self.provider_url)
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
        return self.get_address_from_key(
            key=os.getenv('BLOCKCHAIN_OWNER_PRIVATE_KEY')
        )

    def create_account(self):
        account = self.w3.eth.account.create()
        return {
            'address': account.address,
            'private_key': account.key.hex()
        }

    def get_address_from_key(self, key):
        return self.w3.eth.account.from_key(key).address

    def create_transaction(self, to_address, data):
        tx_info = {
            'to': to_address,
            'gas': 220000,
            'gasPrice': self.w3.eth.gas_price,
            'value': self.w3.toWei(0, 'ether'),
            'chainId': int(os.getenv('BLOCKCHAIN_CHAIN_ID')),
            'nonce': self.w3.eth.get_transaction_count(self.owner_address),
            'data': self.w3.toHex(text=data or '')
        }
        # sign the transaction by private key of sender
        tx_signed = self.w3.eth.account.sign_transaction(
            tx_info, os.getenv('BLOCKCHAIN_OWNER_PRIVATE_KEY')
        )
        # send transaction to the network
        tx_hash = self.w3.eth.sendRawTransaction(tx_signed.rawTransaction)
        tx_text = self.w3.toHex(tx_hash)
        self.w3.eth.wait_for_transaction_receipt(tx_text)
        return tx_text

    def get_transaction(self, tx_address):
        return self.w3.eth.get_transaction(tx_address)

    def get_transaction_input(self, tx_address):
        tx = self.get_transaction(tx_address)
        return self.w3.toText(tx['input'])

    def get_erc20_contract(self, contract_address):
        abi = ContractABIUtil.get_ERC20_ABI()
        return self.w3.eth.contract(contract_address, abi=abi)

    def _transfer_token(self, from_private_key, to_address, amount):
        contract = self.get_erc20_contract(settings.BLOCKCHAIN_ERC20_ADDRESS)

        tx_dict = self.get_default_tx_dict()
        tx_dict.update({'nonce': self._get_nonce(from_private_key)})
        tx_info = contract.functions.transfer(to_address, amount).buildTransaction(tx_dict)
        tx_hash = self._create_transaction(from_private_key, tx_info)
        return tx_hash

    def transfer_token_from_genetica(self, to_address, amount=1):
        return self._transfer_token(
            from_private_key=settings.BLOCKCHAIN_OWNER_PRIVATE_KEY,
            to_address=to_address,
            amount=amount
        )

