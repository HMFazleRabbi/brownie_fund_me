from brownie import accounts, FundMe, config, network, MockV3Aggregator
from scripts.helpful_scripts import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from web3 import Web3


def deploy_fundme():
    account = get_account()
    # price_feed_address = "0xD4a33860578De61DBAbDc8BFdb98FD742fA7028e"
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address=config["networks"][network.show_active()].get("eth_usd_price_feed")
    else:
        deploy_mocks()
        price_feed_address=MockV3Aggregator[-1].address
        print("Mocks Deployed!")


    fund_me=FundMe.deploy(
        price_feed_address,
        {"from": account}, 
        publish_source=config["networks"][network.show_active()].get("verify"), 
    )
    print(f"Contract deployed to {fund_me.address}")
    return fund_me

def main():
    deploy_fundme()