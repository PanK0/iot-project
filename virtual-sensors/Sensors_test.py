from Sensors import *

temp = SensorTemperature(0)
hum = SensorHumidity(50)
wdir = SensorWindDirection(180)
wint = SensorWindIntensity(50)
rain = SensorRainHeight(25)

station = EnvironmentalStation(temp, hum, wdir, wint, rain)
print (station.getTemperaturePayload())
print (station.getHumidityPayload())
print (station.getWindDirectionPayload())
print (station.getWindIntensityPayload())
print (station.getRainHeightPayload())
print (station.getPayload())
