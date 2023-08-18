#Dependancies
import paho.mqtt.client as mqtt
import logging
import sys
import uuid
import ssl
import random
import os

LOGGING_PATH = './logging'
#Creates a directory for logging if it does not exist already
if not os.path.exists(LOGGING_PATH):
    os.makedirs(LOGGING_PATH)
    print(f"Directory '{LOGGING_PATH}' created successfully.")
else:
    print(f"Directory '{LOGGING_PATH}' already exists.")

#The 3 following lines create a uuid for the current session
#Then, using the built in logging library, a log file is created at ./logging/DEBUG with the ID attatched to the file name
#Logging is then added to stdout for conveinience
ID = str(uuid.uuid4())
logging.basicConfig(filename='./logging/DEBUG'+ID,level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

#Used as an override of the client's built in function
#If a return code of zero is observed, the client will then subscribe to test/topic/a1
def on_connect(client, userdata,flags,rc):
    if(rc == 0):
        logging.info('Connection Successful')
        client.subscribe('test/topic/a1')

#Used as an override of the client's built in function
#Logs any messages received from the broker
def on_message(client, userdata, message):
    logging.log(logging.DEBUG,message.payload.decode())
    
#initializing the client
client = mqtt.Client(client_id='cool dude',protocol=4,clean_session=0)  
#Overiding built in methods
client.on_connect = on_connect
client.on_message = on_message

#enable built in logging
client.enable_logger()
#Specifying device port
client._port = 4300

#uncomment below for CA chain auth
#client.tls_set(ca_certs='.\\ssl\\CAFILE.cer',certfile='.\\ssl\\cert.cer',keyfile='.\\ssl\key.key', cert_reqs=ssl.CERT_NONE)
#uncomment command below for thumbprint authentication
client.tls_set(certfile='cert.cer',keyfile='key.key')

#specify the authenticaiton name for the connect packet here
#this must run before attempting to connect
client.username_pw_set(username='test-client1',password=None)

#connects the client to the specified broker, on the specified port with a specified timeout timer
client.connect('BrokerHere',8883,60)

#Maintians connection loop
client.loop_forever()