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
#Logging is then added to stdout for simplicity
ID = str(uuid.uuid4())
logging.basicConfig(filename='./logging/DEBUG'+ID,level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

#this function will report a successful connection if the return code (rc) is zero, then publish to
#test/topic/a1 with qos 1
def on_connect(client, userdata,flags,rc):
    if(rc == 0):
        logging.info('Connection Successful')
        client.publish('test/topic/a1','1',qos=1)


#This function is triggered after every call back
#The current implementation logs the message of the last pub, then generates a random number
#the client then publishes this random number as a string payload with the phrase 'payload' preceding it
def on_publish(client, obj,mid):
        logging.log(5,f'MID: {mid}')
        i = random.randint(0,99999)
        client.publish('test/topic/a1','payload'+str(i),qos=1)
     
#Initialize the client MQTT 3.1.1
client = mqtt.Client(client_id='sender',protocol=4,clean_session=0)  
#overiding built in functions
client.on_connect = on_connect
client.on_publish = on_publish
#Enable logging to use the clients built in logging
#It uses the configuration of the built in logger
client.enable_logger()
client._port = 9000
#uncomment below for CA chain auth
client.tls_set(ca_certs='.\\ssl\\CAFILE.cer',certfile='.\\ssl\\cert.cer',keyfile='.\\ssl\\key.key', cert_reqs=ssl.CERT_NONE)
#uncomment command below for thumbprint authentication
#client.tls_set(certfile='.\\ssl\\thumbprint\\cert.cer',keyfile='.\\ssl\\thumbprint\\key.key')

#specify the authenticaiton name for the connect packet here
#this must run before attempting to connect
client.username_pw_set(username='uri:1:one',password=None)

#connects the client to the specified broker, on the specified port with a specified timeout timer
client.connect('',8883,60)

#maintains the connection loop forever
client.loop_forever()