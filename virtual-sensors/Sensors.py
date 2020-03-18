import random

# Temperature Sensor
class SensorTemperature :
    
    def __init__(self, value) :
        self.value = value
        self.minvalue = -50
        self.maxvalue = 50
        
    def getValue(self) :
        self.value = (random.randint(self.minvalue, self.maxvalue) + self.value) / 2
        return self.value

        
# Humidity Sensor
class SensorHumidity :
    
    def __init__(self, value) :
        self.value = value
        self.minvalue = 0
        self.maxvalue = 100
        
    def getValue(self) :
        self.value = (random.randint(self.minvalue, self.maxvalue) + self.value) / 2
        return self.value
    
    
# Wind Direction Sensor
class SensorWindDirection :
    
    def __init__(self, value) :
        self.value = value
        self.minvalue = 0
        self.maxvalue = 360
        
    def getValue(self) :
        self.value = (random.randint(self.minvalue, self.maxvalue) + self.value) / 2
        return self.value
     
     
# Wind Intensity Sensor
class SensorWindIntensity :
    
    def __init__(self, value) :
        self.value = value
        self.minvalue = 0
        self.maxvalue = 100
        
    def getValue(self) :
        self.value = (random.randint(self.minvalue, self.maxvalue) + self.value) / 2
        return self.value
  

# Rain Height Sensor
class SensorRainHeight :
    
    def __init__(self, value) :
        self.value = value
        self.minvalue = 0
        self.maxvalue = 50
        
    def getValue(self) :
        self.value = (random.randint(self.minvalue, self.maxvalue) + self.value) / 2
        return self.value
        
