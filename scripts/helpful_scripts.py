from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3
DECEMALS=8
STARTING_PRICE=200000000000
LOCAL_BLOCKCHAIN_ENVIRONMENTS =["development", "ganache-local"]
FORKED_LOCAL_ENVIRONMENTS =["mainnet-fork", "mainnet-fork-dev"]

def get_account():
    if(network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or network.show_active() in FORKED_LOCAL_ENVIRONMENTS):
        print("Running brownie local account!")
        return accounts[0]
    else:
        print("Running on " + network.show_active() + "network.")
        return accounts.add(config['wallets']["from_key"])

def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    if len(MockV3Aggregator)<=0:
        MockV3Aggregator.deploy(
            DECEMALS, STARTING_PRICE,  {"from": get_account()}
        )