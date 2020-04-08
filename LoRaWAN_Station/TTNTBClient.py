import paho.mqtt.client as paho                         # mqtt library
import os
import json
import time
import random
from datetime import datetime


# Communication with Thingsboard
ACCESS_TOKEN_E = 'AgS25k4UmqL2BD4v8nZp'                 # Token of device E
ACCESS_TOKEN_F = 'yXkA0gI6h9ZYayhToTYZ'                 # Token of device F
broker = "demo.thingsboard.io"                          # host name
tb_topic = "v1/devices/me/telemetry"                    # Thingsboard topic
tb_port = 1883                                          # data listening port

# Communication with TheThingsNetwork
ttn_host = 'eu.thethings.network'                                       # Host for TheThingsNetwork
ttn_port = 1883                                                         # TTN service Port
ttn_topic = '+/devices/+/up'                                            # TTN topic
ttn_user = 'iotappan'                                                   # TTN Application's name 
ttn_key = 'ttn-account-v2.myG4JDRyLI_p3ylliDwH72pX7bkdRBRL8-fmWpJ0jio'  # TTN Application's Access Key
ttn_dev_e = 'iotappan-dev-e'                                            # device E name
ttn_dev_f = 'iotappan-dev-f'                                            # device F name

# Payload variables
payload_E = ""
payload_F = ""

def on_publish(client,userdata,result):                 # create function for callback
    print("data published to thingsboard \n")
    pass

def on_connect(client, userdata, flags, rc) :           # connect callback for datarec in TTN
    print ("Connected with result coder " + str(rc))
    
def on_subscribe(client, userdata, mid, granted_qos) :
    print ("Subscribed")
    
def on_message(client, userdata, message) :
    #print("Received message '" + str(message.payload) + "' on topic '" + message.topic)
    generic_payload = json.loads(message.payload)       # Capturing the message arrived on TTN Topic
    #print(generic_payload['dev_id'] )
    
    if (generic_payload['dev_id'] == ttn_dev_e) :
        pippo = generic_payload['payload_fields']
        global payload_E
        payload_E = pippo['string']
    elif (generic_payload['dev_id'] == ttn_dev_f) :
        pippo = generic_payload['payload_fields']
        global payload_F
        payload_F = pippo['string']
    else : print("LOOOOL")
    

# Setting Up Client E
client_E = paho.Client("EnvStat_E")                     # create client object
client_E.on_publish = on_publish                        # assign function to callback
client_E.username_pw_set(ACCESS_TOKEN_E)                # access token from thingsboard device
client_E.connect(broker, tb_port, keepalive=60)         # establish connection

# Setting Up Client F
client_F = paho.Client("EnvStat_F")                     # create client object
client_F.on_publish = on_publish                        # assign function to callback
client_F.username_pw_set(ACCESS_TOKEN_F)                # access token from thingsboard device
client_F.connect(broker, tb_port, keepalive=60)         # establish connection


# Setting up Data Receiver from TTN
datarec = paho.Client("DataRec")                        # create client for data receiver from TTN
datarec.on_message = on_message                         # define what to do when a message is received
datarec.username_pw_set(ttn_user, password=ttn_key)     # access with the right credentials
datarec.on_subscribe = on_subscribe
datarec.connect(ttn_host, ttn_port, keepalive=60)       # establish connection
datarec.subscribe(ttn_topic, qos=1)


# Start loooooooooop
client_E.loop_start()
client_F.loop_start()
datarec.loop_start()

# Starting up our rsmb
while (True) :
    
    while (payload_E == "" and payload_F == "") :
        pass
    
    # Device E data transmission to ThingsBoard
    print("EEE ENVIRONMENTAL STATION E ")
    ret = client_E.publish(tb_topic, payload_E)
    print ("Payload : " + payload_E)
    
    print ("\n")
    print ("\n")
    
    # Device F data transmission to ThingsBoard
    print("F ENVIRONMENTAL STATION F ")
    ret = client_F.publish(tb_topic, payload_F)
    print ("Payload : " + payload_F)
    print ("\n")
    print ("\n")
    
    payload_E = ""
    payload_F = ""
