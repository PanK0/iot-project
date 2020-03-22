import paho.mqtt.client as mqtt
import time

dev_id = "c4ef1ec0-6a98-11ea-8e0a-7d0ef2a682d3"
token = "vgFztmvT6bps7JCeOEZq"
broker="demo.thingsboard.io"                        # host name
port=1883
topic = "v1/devices/me/telemetry"

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc) :
    if (rc==0) :
        print("connected OK Returned code = ", rc)
    else :
        print("Bad connection Returned code = ", rc)
    
def on_message(client, userdata, msg) :
    print (msg.topic + " " + str(msg.payload))    


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(token)
client.connect(broker , port, 60)
client.subscribe("aa")

client.loop_forever()
