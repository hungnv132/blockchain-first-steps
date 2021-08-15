import os
from web3_app.base import BlockchainNetwork


def test_connection():
    blockchain = BlockchainNetwork()
    assert blockchain.is_connected is True
    assert blockchain.provider_url == os.getenv('BLOCKCHAIN_PROVIDER_URL')
