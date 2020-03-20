import paho.mqtt.client as paho                     # mqtt library
import os
import json
import time
from datetime import datetime

from Sensors import *                               # Import sensor classes and environmental station class 

# Creating Sensors and Environmental Station 1
temperature_sensor_A = SensorTemperature(0)
humidity_sensor_A = SensorHumidity(50)
wind_dir_sensor_A = SensorWindDirection(180)
wind_int_sensor_A = SensorWindIntensity(50)
rain_height_sensor_A = SensorRainHeight(25)

env_station_A = EnvironmentalStation(temperature_sensor_A, humidity_sensor_A,
                                     wind_dir_sensor_A, wind_int_sensor_A,
                                     rain_height_sensor_A)

ACCESS_TOKEN='vgFztmvT6bps7JCeOEZq'                 # Token of your device
broker="demo.thingsboard.io"                        # host name
port=1883                                           # data listening port

def on_publish(client,userdata,result):             # create function for callback
    print("data published to thingsboard \n")
    pass
client1= paho.Client("control1")                    # create client object
client1.on_publish = on_publish                     # assign function to callback
client1.username_pw_set(ACCESS_TOKEN)               # access token from thingsboard device
client1.connect(broker,port,keepalive=60)           # establish connection

while True:
  
   payload = env_station_A.getPayload()
   ret= client1.publish("v1/devices/me/telemetry",payload) # topic-v1/devices/me/telemetry
   print("Please check LATEST TELEMETRY field of your device")
   print(payload);
   time.sleep(5)
