# Sensors
The simulation represents a virtual environmental station that periodically generates a set of random values for each sensor:

1. temperature (-50 ... 50 Celsius)
2. humidity (0 ... 100%)
3. wind direction (0 ... 360 degrees)
4. wind intensity (0 ... 100 m/s)
5. rain height (0 ... 50 mm / h) 

The virtual environmental station uses a unique ID (identity) to publish these random values on an MQTT channel. You need to have at least 2 such virtual stations running and publishing their values on the MQTT channel. 

Refs @ http://ichatz.me/Site/InternetOfThings2020-Assignment1

## How To
- To Send data to the device via MQTT protocol:
```
python Simulation.py
```
- To see the data visualized on Thinsboard (https://thingsboard.io/):
    Go @ [Thingsboard DASHBOARD](https://demo.thingsboard.io/dashboard/3406b610-6aa3-11ea-8e0a-7d0ef2a682d3?publicId=623f71c0-6aa3-11ea-8e0a-7d0ef2a682d3)

## Complete Tutorial
[TUTORIAL](https://www.hackster.io/panicik/iot-assignment-1-991fcc)
