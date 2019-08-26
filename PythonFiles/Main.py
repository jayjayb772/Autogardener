#Import packages

#init

from Time import sleep

from PythonFiles.SensorFiles.MainSensorController import *
from PythonFiles.ControlFiles.MainPartsController import *
from PythonFiles.DatabaseFiles.MainDatabaseController import *

curTemp = 0
lastTemp = 0
curHumid = 0
lastHumid = 0
curSoilMoisture = 0
lastSoilMoisture = 0

maxTemp = 76
minTemp = 70

#Check sensor vals
def checkSensorVals():
    lastTemp = curTemp
    lastHumid = curHumid
    lastSoilMoisture = curSoilMoisture
    curTemp = getTemp()
    curHumid = getHumidity()
    curSoilMoisture = getMoistureLevel()

def tempCheck(temp):
    saveTemp(temp,Time.now())
    if temp > maxTemp:
        lowerTemp()
    if temp < minTemp:
        raiseTemp()


def lowerTemp():
    turnFanOn()
    temp = getTemp()
    if(temp>maxTemp):
        Time.sleep(10)
        lowerTemp()
    else:
        turnFanOff()

def raiseTemp():
    turnHeaterOn()
    temp = getTemp()
    if(temp<minTemp):
        Time.sleep(10)
        raiseTemp()
    else:
        turnHeaterOff()


#Main prog
def main():
    return
