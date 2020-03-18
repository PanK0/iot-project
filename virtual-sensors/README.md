# Sensors
The simulation represents a virtual environmental station that periodically generates a set of random values for each sensor:

1. temperature (-50 ... 50 Celsius)
2. humidity (0 ... 100%)
3. wind direction (0 ... 360 degrees)
4. wind intensity (0 ... 100 m/s)
5. rain height (0 ... 50 mm / h) 

Each virtual sensor should publish these random values on an MQTT channel.
Refs @ http://ichatz.me/Site/InternetOfThings2020-Assignment1
