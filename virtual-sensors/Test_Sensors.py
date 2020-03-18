from Sensors import *

temp = SensorTemperature(0)
hum = SensorHumidity(50)
wdir = SensorWindDirection(180)
wint = SensorWindIntensity(50)
rain = SensorRainHeight(25)

print ( "Temperature : " + str(temp.getValue() ))
print ("Humidity : " + str(hum.getValue() ))
print ("Wind Direction : " + str(wdir.getValue() ))
print ("Wind Intensity : " + str(wint.getValue() )) 
print ("Rain Height : " + str(rain.getValue() ))
