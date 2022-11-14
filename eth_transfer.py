from web3 import Web3
from decouple import config

infuraUrl = config('INFURA_URL')
contractAddress = config('CONTRACT_ADDRESS')
ownerAddress = config('OWNER_ADDRESS')
privateKey = config('SUPER_SECRET_PRIVATE_KEY')
abi = '[{"inputs":[{"internalType":"string","name":"name_","type":"string"},{"internalType":"string","name":"symbol_","type":"string"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]'

web3 = Web3(Web3.HTTPProvider(infuraUrl))

res = web3.isConnected()

# Check if the connection is established
if res:
    print("Connected to Web3")

    # Amount to transfer
    amountInEther="0.001"

    # Account Address to transferTo
    targetAddress="0xac35866956C9eD35880Be6c7B229d8E84B7B7280"

    # Get the account Nonce
    nonce = web3.eth.getTransactionCount(ownerAddress)
    print('nonce (Tranx count): ' + str(nonce))

    # Set up Gas Price for the tranx
    gasPrice = web3.toWei('100', 'gwei')

    # Set the amount of ETH we want to send
    value = web3.toWei(amountInEther, 'ether')

    # Creating transaction
    tx = {
        'nonce': nonce,
        'to': targetAddress,
        'value': value,
        'gas': 21000,
        'gasPrice': gasPrice,
        'chainId': 5
    }

    # Sign the tranx
    signed_tx = web3.eth.account.sign_transaction(tx, privateKey)

    # Send the tranx to Infura
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print('tx hash: ' + tx_hash.hex())

    # Wait for the transaction to be mined
    web3.eth.waitForTransactionReceipt(tx_hash)
    print('tx mined')
    