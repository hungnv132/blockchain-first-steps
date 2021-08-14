from web3_app.base import BlockchainNetwork


def test_connection():
    blockchain = BlockchainNetwork()
    assert blockchain.is_connected is True
