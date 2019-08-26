#Import packages

#init
from sqlite3.dbapi2 import Time

from PythonFiles.SensorFiles.MainSensorController import *
from PythonFiles.ControlFiles.MainPartsController import *
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