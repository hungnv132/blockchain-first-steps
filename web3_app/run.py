from base import BlockchainNetwork

if __name__ == '__main__':
    blockchain = BlockchainNetwork()
    acc_info = blockchain.create_account()
    print(acc_info)
