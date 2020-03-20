import random

# Temperature Sensor
class SensorTemperature :
    
    def __init__(self, value) :
        self.__value = value
        self.__minvalue = -50
        self.__maxvalue = 50
        self.__name = "Temperature"
        
    def __getValue(self) :
        self.__value = (random.randint(self.__minvalue, self.__maxvalue) + self.__value) / 2
        return self.__value

    def getPayload(self) :
        payload =   "\"" + self.__name + "\":"
        payload +=  str(self.__getValue())
        return payload
        
# Humidity Sensor
class SensorHumidity :
    
    def __init__(self, value) :
        self.__value = value
        self.__minvalue = 0
        self.__maxvalue = 100
        self.__name = "Humidity"
        
    def __getValue(self) :
        self.__value = (random.randint(self.__minvalue, self.__maxvalue) + self.__value) / 2
        return self.__value

    def getPayload(self) :
        payload =   "\"" + self.__name + "\":"
        payload +=  str(self.__getValue())
        return payload
    
    
# Wind Direction Sensor
class SensorWindDirection :
    
    def __init__(self, value) :
        self.__value = value
        self.__minvalue = 0
        self.__maxvalue = 360
        self.__name = "Wind Direction"
        
    def __getValue(self) :
        self.__value = (random.randint(self.__minvalue, self.__maxvalue) + self.__value) / 2
        return self.__value

    def getPayload(self) :
        payload =   "\"" + self.__name + "\":"
        payload +=  str(self.__getValue())
        return payload
     
     
# Wind Intensity Sensor
class SensorWindIntensity :
    
    def __init__(self, value) :
        self.__value = value
        self.__minvalue = 0
        self.__maxvalue = 100
        self.__name = "Wind Intensity"
        
    def __getValue(self) :
        self.__value = (random.randint(self.__minvalue, self.__maxvalue) + self.__value) / 2
        return self.__value

    def getPayload(self) :
        payload =   "\"" + self.__name + "\":"
        payload +=  str(self.__getValue())
        return payload
  

# Rain Height Sensor
class SensorRainHeight :
    
    def __init__(self, value) :
        self.__value = value
        self.__minvalue = 0
        self.__maxvalue = 50
        self.__name = "Rain Height"
        
    def __getValue(self) :
        self.__value = (random.randint(self.__minvalue, self.__maxvalue) + self.__value) / 2
        return self.__value

    def getPayload(self) :
        payload =   "\"" + self.__name + "\":"
        payload +=  str(self.__getValue())
        return payload
        
# Environmental Station
class EnvironmentalStation :
    
    def __init__(self, temperature_sensor, humidity_sensor, wind_direction_sensor,
                wind_intensity_sensor, rain_height_sensor) :
        self.__temperature_sensor = temperature_sensor
        self.__humidity_sensor = humidity_sensor
        self.__wind_direction_sensor = wind_direction_sensor
        self.__wind_intensity_sensor = wind_intensity_sensor
        self.__rain_height_sensor = rain_height_sensor
        
    def getTemperaturePayload(self) :
        return self.__temperature_sensor.getPayload()
    
    def getHumidityPayload(self) :
        return self.__humidity_sensor.getPayload()
    
    def getWindDirectionPayload(self) :
        return self.__wind_direction_sensor.getPayload()
    
    def getWindIntensityPayload(self) :
        return self.__wind_intensity_sensor.getPayload()
    
    def getRainHeightPayload(self) :
        return self.__rain_height_sensor.getPayload()
    
    def getPayload(self) :
        payload =   "{"
        payload +=  self.getTemperaturePayload() + ","
        payload +=  self.getHumidityPayload() + ","
        payload +=  self.getWindDirectionPayload() + ","
        payload +=  self.getWindIntensityPayload() + ","
        payload +=  self.getRainHeightPayload()
        payload +=  "}"
        return payload
