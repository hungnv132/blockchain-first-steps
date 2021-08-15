#!/usr/bin/python3
import os
from dotenv import load_dotenv
from brownie import OnlyERC20, accounts

load_dotenv()  # take environment variables from .env.


def main():
    owner_key = os.getenv('BLOCKCHAIN_OWNER_PRIVATE_KEY')
    if not owner_key:
        raise Exception("No Owner Private Key")
    owner = accounts.add(owner_key)

    more_data = {'from': owner}

    return OnlyERC20.deploy(more_data)
