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

## Requirements
- pahp-mqtt @ https://pypi.org/project/paho-mqtt/
- Mosquitto @ https://mosquitto.org/
- emcute_mqttsn @ https://github.com/RIOT-OS/RIOT/tree/master/examples/emcute_mqttsn

In order to make the whole thing work see the requirements @ [MAIN PROJECT PAGE](https://github.com/PanK0/iot-project#requirements)

## TBCLIENT.py 
- Copy the file TBCLIENT.py in the _mosquitto.rsmb/rsmb/src/MQTTSClient/Python_ folder

The client receives data from the devices on the topics _devices/dev\_c_ and _devices/dev\_d_ and forwards the telemetry to Thingsboard.

Remember to set the variables _ACCESS\_TOKEN\_C_ and _ACCESS\_TOKEN\_D_ to your Thingsboard's devices tokens.

## main.c
- Copy the file main.c in the _RIOT/examples/emcute_mqttsn_ folder

The file emulates two environmental stations sending data on the choosen topics formatted in a JSON script.

Note that to make the whole thing work you must connect to the topics _devices/dev\_c_ and _devices/dev\_d_.

## Directory Example
Here is an example on how the directory tree can be:

[![dirtree.png](https://i.postimg.cc/zv3dYCsL/dirtree.png)](https://postimg.cc/QKGgpTxs)

## How to run the system
1. Enable TAP :

    - in _RIOT/_ folder:
    
    ```
    sudo ./dist/tools/tapsetup/tapsetup -c 2
    ```
    
    - to check if the taps are running:
    
    ```
    ifconfig | grep tap
    ```

2. Run the Broker :

    - in _mosquitto.rsmb/rsmb/src_ folder:
    
    ```
    ./broker_mqtts config.conf
    ```

3. Run the MQTTSN client:

    - in _mosquitto.rsmb/rsmb/src/MQTTSClient/Python_ folder:
    
    ```
    python TBCLIENT.py
    ```
    
4. Run the RIOT Devices:
    
    - in _RIOT/examples/emcute_mqttsn_ folder:
    
    ```
    ifconfig tapbr0
    ```
    - copy the ipv6 address at the inet6 field. It should be something like _fe90::2567:49ff:fe8e:7f9a_
    
    - run the device: 
    
    ```
    make all term
    ```
    
    - Once the device is running, connect it to the broker:
    
    ```
    con <ipv6_address> <port>
    // Example : con fe90::2567:49ff:fe8e:7f9a 1885
    ```
    - start the transmission:
    
    ```
    start "devices/dev_c" "devices/dev_d"
    ```
    
5. See what's happening:

    Now the device should be emulating the two environmental stations by transmitting random payloads on the two topics _devices/dev\_c_ and _devices/dev\_d_ thorugh the broker we have set at point 2.
    The MQTTSN client receives the data in MQTTSN protocol and forwards them to Thingsboard via MQTT.

