# LoRaWAN_Station
In this assignment we will built on-top of the cloud-based and edge-based components developed in the first and second assignments. Now we will replace the MQTT protocol and the short-range wireless medium with LoRaWAN and TheThingsNetwork. In this assignment you need to develop a new RIOT-OS application that will be executed on the B-L072Z-LRWAN1 LoRa kit. You will use TheThingsNetwork to interconnect the sensor devices with the cloud infrastructure via the MQTT protocol.

Using RIOT-OS develop an application that represents a virtual environmental station that generates periodically a set of random values for 5 different sensors:

    temperature (-50 ... 50 Celsius)
    humidity (0 ... 100%)
    wind direction (0 ... 360 degrees)
    wind intensity (0 ... 100 m/s)
    rain height (0 ... 50 mm / h) 

The virtual environmental station uses a unique ID (identity) to publish these random values on TheThingsNetwork via LoRaWAN. 

Refs @ http://ichatz.me/Site/InternetOfThings2020-Assignment3
