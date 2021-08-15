#!/usr/bin/python3
import os
from dotenv import load_dotenv
from brownie import MyToken, accounts

load_dotenv()  # take environment variables from .env.


def main():
    owner_key = os.getenv('BLOCKCHAIN_OWNER_PRIVATE_KEY')
    if not owner_key:
        raise Exception("No Owner Private Key")
    owner = accounts.add(owner_key)

    # Initial Token Information
    token_name = 'Hung Token Test'
    token_symbol = 'HUNGTOKEN88'
    token_decimal = 18
    token_total_supply = 1e21
    more_data = {'from': owner}

    return MyToken.deploy(
        token_name,
        token_symbol,
        token_decimal,
        token_total_supply,
        more_data
    )
