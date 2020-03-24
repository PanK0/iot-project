import paho.mqtt.client as paho                     # mqtt library
import os
import json
import time
from datetime import datetime

from Sensors import *                               # Import sensor classes and environmental station class 

# Creating Sensors and Environmental Station A
temperature_sensor_A = SensorTemperature(0)
humidity_sensor_A = SensorHumidity(50)
wind_dir_sensor_A = SensorWindDirection(180)
wind_int_sensor_A = SensorWindIntensity(50)
rain_height_sensor_A = SensorRainHeight(25)

env_station_A = EnvironmentalStation(temperature_sensor_A, humidity_sensor_A,
                                     wind_dir_sensor_A, wind_int_sensor_A,
                                     rain_height_sensor_A)

# Creating Sensors and Environmental Station B
temperature_sensor_B = SensorTemperature(0)
humidity_sensor_B = SensorHumidity(50)
wind_dir_sensor_B = SensorWindDirection(180)
wind_int_sensor_B = SensorWindIntensity(50)
rain_height_sensor_B = SensorRainHeight(25)

env_station_B = EnvironmentalStation(temperature_sensor_B, humidity_sensor_B,
                                     wind_dir_sensor_B, wind_int_sensor_B,
                                     rain_height_sensor_B)

# Communication
ACCESS_TOKEN_A = 'vgFztmvT6bps7JCeOEZq'                # Token of device A
ACCESS_TOKEN_B = 'BKJK0j5zVyh3hIkCBWDI'                # Token of device B
broker = "demo.thingsboard.io"                         # host name
topic = "v1/devices/me/telemetry"
port = 1883                                            # data listening port

def on_publish(client,userdata,result):             # create function for callback
    print("data published to thingsboard \n")
    pass

# Setting Up Client A
client_A = paho.Client("EnvStat_A")                    # create client object
client_A.on_publish = on_publish                     # assign function to callback
client_A.username_pw_set(ACCESS_TOKEN_A)               # access token from thingsboard device
client_A.connect(broker,port,keepalive=60)           # establish connection

# Setting Up Client B
client_B = paho.Client("EnvStat_B")                    # create client object
client_B.on_publish = on_publish                     # assign function to callback
client_B.username_pw_set(ACCESS_TOKEN_B)               # access token from thingsboard device
client_B.connect(broker,port,keepalive=60)           # establish connection


while True:
    
    payload_A = env_station_A.getPayload()
    ret = client_A.publish(topic, payload_A) # topic-v1/devices/me/telemetry
    print("AAA ENVIRONMENTAL STATION A ")
    print(payload_A)
    print ("\n")

    payload_B = env_station_B.getPayload()
    ret = client_B.publish(topic, payload_B)
    print("BBB ENVIRONMENTAL STATION B ")
    print(payload_B)
    print ("\n")

    time.sleep(2)
