# My First Steps on Blockchain

### Smart Contracts - Brownie - https://eth-brownie.readthedocs.io/
- Install package:
  - `brownie pm install OpenZeppelin/openzeppelin-contracts@4.0.0`
- Add network:
  - `brownie networks add MyLocal my-local host=$BLOCKCHAIN_PROVIDER_URL chainid=$BLOCKCHAIN_CHAIN_ID`
  - `brownie networks add MyEthereum my-rinkeby host=$BLOCKCHAIN_PROVIDER_URL chainid=$BLOCKCHAIN_CHAIN_ID`
  - `brownie networks add MyAvax my-avax host=$BLOCKCHAIN_PROVIDER_URL chainid=$BLOCKCHAIN_CHAIN_ID`
- Deploy:
  - `brownie run deploy_my_erc20.py --network my-avax`
### Web3 App
