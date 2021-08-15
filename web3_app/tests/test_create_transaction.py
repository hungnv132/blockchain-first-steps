import os
from web3_app.base import BlockchainNetwork


def test_create_transaction():
    blockchain = BlockchainNetwork()
    tx_text = blockchain.create_transaction(
        to_address=os.getenv('BLOCKCHAIN_TEST_ADDRESS'),
        data='',
    )
    assert tx_text == 1
