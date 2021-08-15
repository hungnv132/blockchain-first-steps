#!/usr/bin/python3
import os
from dotenv import load_dotenv
from brownie import ZeppelinERC20, accounts

load_dotenv()  # take environment variables from .env.


def main():
    owner_key = os.getenv('BLOCKCHAIN_OWNER_PRIVATE_KEY')
    if not owner_key:
        raise Exception("No Owner Private Key")
    owner = accounts.add(owner_key)

    token_total_supply = 1e21
    more_data = {'from': owner}

    return ZeppelinERC20.deploy(token_total_supply, more_data)
