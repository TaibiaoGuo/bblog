# !/usr/bin python3
# encoding:utf-8
'''
 @Time     :2020/3/23 9:26 AM
 @Author   :TaibiaoGuo
 @FileName :deploy
 @Github   :https://github.com/TaibiaoGuo
 @Describe :
'''

from web3 import Web3, HTTPProvider
import sols
import os


true = True
false = False
web3 = Web3(HTTPProvider('ETH_PROVIDER'))
fromAddr = 'MAIN_ADDRESS'
privateKey = 'PRIVATE_KEY'
nonce = web3.eth.getTransactionCount(fromAddr)
gasPrice = web3.eth.gasPrice

rawTx = {
    'from': fromAddr,
    'nonce': nonce,
    'gasPrice': gasPrice,
    'gas': 300000,
    'value': web3.toWei(0, 'ether'),
    'data': '0x606060405260008060006101000a81548160ff021916908315150217905550341561002957600080fd5b60e4806100376000396000f3006060604052600436106049576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168063a3c8e39314604e578063b2fa1c9e146060575b600080fd5b3415605857600080fd5b605e608a565b005b3415606a57600080fd5b607060a6565b604051808215151515815260200191505060405180910390f35b60016000806101000a81548160ff021916908315150217905550565b6000809054906101000a900460ff16815600a165627a7a723058208fd18624eaaac9c24521a084590bb1b536e9a94f23086c49864b9c02300ff0c20029'
}

def deploy(rawTx):
    signedTx = web3.eth.account.signTransaction(rawTx, private_key=privateKey)
    hashTx = web3.eth.sendRawTransaction(signedTx.rawTransaction).hex()
    receipt = web3.eth.waitForTransactionReceipt(hashTx)
    return receipt
if __name__ == '__main__':
    receipt = deploy(rawTx)
    print('address: ' + receipt['contractAddress'])

