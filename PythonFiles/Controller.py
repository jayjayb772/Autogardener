import math

from PythonFiles.ControlFiles.MainPartsController import *
from PythonFiles.DatabaseFiles.MainDatabaseController import *
from PythonFiles.SensorFiles.MainSensorController import *
import time


class Controller:
    def __init__(self):
        self.curTemp = 0
        self.lastTemp = 0
        self.curHumidity = 0
        self.lastHumidity = 0
        self.curMoisture = 0
        self.lastMoisture = 0
        self.maxTemp = 78
        self.minTemp = 70
        self.minMoisture = 40
        self.maxMoisture = 70
        self.idealMoisture = 55

    def lowerTemp(self):
        turnFanOn()
        change = 0
        time.sleep(10)
        self.curTemp = getTemp()
        if self.curTemp < self.maxTemp:
            turnFanOff()
            return self.curTemp
        else:
            t = self.curTemp
            change = math.abs(t - self.raiseTemp(self.curTemp))
        return (str(change), "Lowered by " + str(change))

    def raiseTemp(self):
        turnHeaterOn()
        change = 0
        time.sleep(10)
        self.curTemp = getTemp()
        if self.curTemp > self.minTemp:
            turnHeaterOff()
            return self.curTemp
        else:
            t = self.curTemp
            change = math.abs(t - self.raiseTemp(self.curTemp))
        return (str(change), "Raised by " + str(change))

    def tempCheck(self):
        self.lastTemp = self.curTemp
        self.curTemp = getTemp()
        returnData = ("0", "not changed")
        if self.curTemp > self.maxTemp:
            returnData = self.lowerTemp(self.curTemp)
        if self.curTemp < self.minTemp:
            returnData = self.raiseTemp(self.curTemp)
        return returnData

    def humidityCheck(self):
        humidityData = ("0", "not changed")
        self.lastHumidity = self.curHumidity
        self.curHumidity = getHumidity()
        return humidityData

    def waterPlant(self, count):
        turnWaterOn()
        time.sleep(20 / count)
        turnWaterOff()
        time.sleep(60)
        self.curMoisture = getMoistureLevel()
        if self.curMoisture < self.idealMoisture:
            self.waterPlant(count + 1)

    def moistureCheck(self):
        returnData = ""
        self.lastMoisture = self.curMoisture
        self.curMoisture = getMoistureLevel()
        if self.curMoisture < self.minMoisture:
            self.waterPlant(1)
            returnData = "watered."
        else:
            returnData = "not watered."
        return returnData

    def runChecks(self):
        returnMessage = "Temperature was "
        tempData = self.tempCheck()
        returnMessage += tempData[1]
        saveTemp(self.curTemp, tempData)
        returnMessage += ". Humidity was "
        humidityData = self.humidityCheck()
        returnMessage += humidityData[1]
        saveHumidity(self.curHumidity, humidityData)
        returnMessage += ". The plant was "
        moistureData = self.moistureCheck()
        returnMessage += moistureData
        return returnMessage
