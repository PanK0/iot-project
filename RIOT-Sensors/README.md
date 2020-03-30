# RIOT Sensors
In this assignment we will built on-top of the cloud-based components developed in the first assignment. Now we will replace the virtual environmental stations developed using Python/Java, or any other language you decided, with new ones built using the RIOT-OS and MQTT-SN protocol. You will use the native emulator of RIOT-OS to run your stations and generate values over MQTT-SN that need to arrive to the cloud via the MQTT. You will also use IOT-LAB to execute your RIOT-OS application on real devices.

Using RIOT-OS develop an application that represents a virtual environmental station that generates periodically a set of random values for 5 different sensors:

    temperature (-50 ... 50 Celsius)
    humidity (0 ... 100%)
    wind direction (0 ... 360 degrees)
    wind intensity (0 ... 100 m/s)
    rain height (0 ... 50 mm / h) 

The virtual environmental station uses a unique ID (identity) to publish these random values on an MQTT-SN channel. You need to have at least 2 such virtual stations running using the native emulator of RIOT-OS and publishing their values on the MQTT-SN channel.

Refs @ http://ichatz.me/Site/InternetOfThings2020-Assignment2

# How To

## TBCLLIENT.py 
- Copy the file TBCLIENT.py in the _mosquitto.rsmb/rsmb/src/MQTTSClient/Python folder_
