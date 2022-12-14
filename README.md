
# Blockchain Web3 APIs

Python Application to transfer Goerli ETH and SHIBBY (SHB) Tokens


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`INFURA_URL`: Create an infura account at infura.io and create a project then change the Ethereum url from mainnet to goerli and paste the url here

`CONTRACT_ADDRESS`: Go to https://goerli.etherscan.io/ and fetch the address of the contract created by you  

`OWNER_ADDRESS`: This is the MetaMask Account address, can be found once account is created.

`SUPER_SECRET_PRIVATE_KEY`: To fetch this key, go to MetaMask Settings -> account details -> export private key, 'which will prompt for account password'

`SEED_PHRASE`: This is the Secret Phase which will be visible in security & privacy section in MetaMask Settings just after clicking on secret recovery phase.

## Installation

Install Docker Desktop on windows & for linux you can follow the official document provided by Docker (https://docs.docker.com/engine/install/ubuntu/)

```bash
  Open Docker Desktop on windows system
```
    
## Run Locally

Clone the project

```bash
  git clone https://github.com/rajendrachavan/blockchain-2022.git
```

Go to the project directory

```bash
  cd blockchain-2022
```

Add the .env file in this directory, which we created earlier.

Once environment (.env) file is added, 
Open git bash for the same directory to Create Docker Container

```bash
  docker build -t <docker_container_name>
```
Check the running containers by following command,

```bash
  docker ps
  docker image ls  -for checking images
```
Now we spin up the application with the docker-compose command in detach mode,

```bash
  docker-compose up -d
```
## Run the following curl command for doing transactions ##
**Replace the values enclosed in angular brackets i.e., '<>' for below commands,**

This transfers ETH:  

```bash
curl --header "Content-Type: application/json" --request POST --data '{"address":"<MetaMask Account Address of Receipient>", "amount":"<Amount of GoerliETH to send eg: 0.05>"}' http://localhost:8090/eth
```

This transfers token:

```bash
curl --header "Content-Type: application/json" --request POST --data '{"address":"<MetaMask Account Address of Receipient>"}' http://localhost:8090/token
```
