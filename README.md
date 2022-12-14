STEP 1->

Pull the code from the repository using following command:-
git pull https://github.com/swappys/blockchainCodes.git

STEP 2->

Extract the ZIP file using some unzipping tool.

STEP 3->

After the process of unzipping, import the above project into Visual Studio Code.

STEP 4->

For the code to run properly, we need to add an .env file in the same directory, hence create a .env file which will contain 
1.INFURA_URL- For this you will have to create an Infura account and in that copy the GORLI url from ethereum section and assign it to INFURA_URL variable.
2.CONTRACT_ADDRESS- For this, go to the etherscan and fetch the address of contract that was created and assign it to CONTRACT_ADDRESS variable.
3.OWNER_ADDRESS- In this enter the address which is displayed in account details section in metamask.
4.SUPER_SECRET_PRIVATE_KEY- To get this key, go to settings, account details and click on export private key. It will prompt you to enter the password of metamask. 
Enter the same and assign it to this variable.
5.SEED_PHRASE- This is the secret phase which will be visible on security & privacy section in metamask setting. Click on reveal secret recovery phase to access the same.
Assign it to this variable.

After setting up these variables with their respective keys, your .env file is ready. Save it.
 
STEP 5-> Install Docker Desktop on the system and open it.

STEP 6-> After installation, create a docker container using command "docker build -t <docker_container_name>"

STEP 7-> Run the image using command "docker run -p 8090:8080 --name nci -d <docker_container_name>"

STEP 8-> Check the containers which are running by running command "docker ps" and the image by running command "docker image ls".

STEP 9-> Stop the container using "docker stop <container_name>

STEP 10->Run docker compose in detached mode using command "docker-compose up -d"

STEP 11-> Now we can access the CURL command in Git Bash as follows->
## For Transfering ETH ##
curl --header "Content-Type: application/json" --request POST --data'{"address":<receiver_address>,"amount":<amount to transfer>} 'http://localhost:8090/eth
the above command will transfer the eth to the receiver address which is mentioned above.

## For Transfering TOKEN ##
To transfer token enter the following command->
curl --header "Content-Type: application/json" --request POST --data'{"address":<receiver_address>} 'http://localhost:8090/token


