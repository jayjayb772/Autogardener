#Import packages
import time
import datetime

from mysql import connector

mydb = connector.connect(
    host='192.168.0.165',
    port='8457',
    user='root',
    passwd='pi',
    database='mydb'
)

#Save temp
def saveTemp(temp, adjustData):
    cursor = mydb.cursor(dictionary=True)
    sql = "INSERT INTO t_temp (temp,reading_data,timestamp) VALUES (%s, %s, %s);"
    val = (temp, adjustData,timestamp())
    cursor.execute(sql, val)
    mydb.commit()
    cursor.close()

def getTemp(num):
    cursor = mydb.cursor(dictionary=True)
    sql = "SELECT * FROM t_temp ORDER BY reading_id DESC LIMIT 1;"
    cursor.execute(sql)
    all = cursor.fetchall()
    cursor.close()
    return all


#Save Humidity
def saveHumidity(humidity, adjustData):
    cursor = mydb.cursor(dictionary=True)
    sql = "INSERT INTO t_humidity (humidity,reading_data, timestamp) VALUES (%s, %s, %s);"
    val = (humidity, adjustData, timestamp())
    cursor.execute(sql, val)
    mydb.commit()
    cursor.close()

def getHumidity(num):
    cursor = mydb.cursor(dictionary=True)
    sql = "SELECT * FROM t_humidity ORDER BY reading_id DESC LIMIT 1;"
    cursor.execute(sql)
    all = cursor.fetchall()
    cursor.close()
    return all


#Save soil moisture
def saveMoisture(moisture, adjustData):
    cursor = mydb.cursor(dictionary=True)
    sql = "INSERT INTO t_moisture (moisture, reading_data, timestamp) VALUES (%s, %s, %s);"
    val = (moisture, adjustData, timestamp())
    cursor.execute(sql, val)
    mydb.commit()
    cursor.close()

def getMoisture(num):
    cursor = mydb.cursor(dictionary=True)
    sql = "SELECT * FROM t_moisture ORDER BY reading_id DESC LIMIT 1;"
    cursor.execute(sql)
    all = cursor.fetchall()
    cursor.close()
    return all

def timestamp():
    return str(time.ctime(datetime.datetime.now().timestamp()))

def test():
    tempData = "rasied by 2"
    temp = "70"
    humidityData = "not changed"
    humidity = "50"
    moistureData = "not watered"
    moisture = "55"
    #saveTemp(temp, tempData)
    print(getTemp(1))
    #saveHumidity(humidity,humidityData)
    print(getHumidity(1))
    #saveMoisture(moisture,moistureData)
    print(getMoisture(1))

test()