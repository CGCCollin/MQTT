This repository contains basic MQTT publishers and subscribers made using the Paho python library.
Additionally, a seperate folder is available for creating docker containers to run the clients.
Instructions are available below:

Ensure all commands are performed in either powershell or bash. 
This folder contains ple mqtt clients written in python using the paho-mqtt library for publishing and subscribing respectively. 
A folder is also available for creating docker containers which use these clients. 
To create the docker container, switch to the container folder and enter the command: docker compose up This should start a container attatched. 
Should you wish to detatch the container and have it run in the background, simply add the -d flag.
 
To create the python environement, enter the command: python -m venv ./venv 
Then activate the environement using: ./venv/Scripts/Activate.ps1 
Finally install dependancies using: pip install -r requirements.txt You should now be able to run both clients. 
Note that for the clients to function properly you will need to specify a link to an MQTT broker with a corresponding CA.

INPUTS: certificates for connecting to your desired broker. 
Ensure to update cert paths in scripts such that they match your file structure. 
For creating docker containers with certificates (certs), ensure to update the docker file with the names and extensions of your certificates. 
Script paths will also need to be updated in the Cotainer folder. 
Update them such that certificates and keys will be found by the program in the root Container folder. 
This is for simplicity, and will make it easier to get the container up and running.

OUTPUTS: logging data from MQTT clients, and optionally docker containers/images.
