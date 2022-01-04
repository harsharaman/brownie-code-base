from brownie import Token, accounts

def main():
    #The first account holds all the token and distributes to everyone else
    account = accounts[0]
    
    token = Token.deploy("BRO Token", "BRO", 18, 1e18, {"from": account})
    return token

def distribute_tokens(sender=account, receiver_list=accounts[1:]):
    token = main()
    for receiver in receiver_list:
        token.transfer(receiver, 1e9, {"from": sender})