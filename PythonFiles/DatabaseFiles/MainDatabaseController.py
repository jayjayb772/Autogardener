#Import packages


from mysql import connector

mydb = connector.connect(
    host='192.168.0.137',
    port='8457',
    user='root',
    passwd='pi',
    database='myDB'
)


def getPlayers(gameCode):
    cursor = mydb.cursor(dictionary=True)
    sql="SET @gameCode =\""
    sql = sql+gameCode
    sql=sql+"\";"
    print(sql)
    cursor.execute(sql)
    sql = "SELECT * FROM t_players WHERE gameCode = @gameCode;"
    cursor.execute(sql)
    all = cursor.fetchall()
    cursor.close()
    return all

def getEvents():
    cursor = mydb.cursor(dictionary=True)
    sql = "SELECT * FROM t_events ORDER BY id DESC LIMIT 5;"
    cursor.execute(sql)
    all = cursor.fetchall()
    cursor.close()
    return all


#Save temp
def saveTemp(temp, adjustData):
    cursor = mydb.cursor(dictionary=True)
    sql = "INSERT INTO t_temp (timestamp, temp,adjustData) VALUES (%s, %s);"
    val = (temp, adjustData)
    cursor.execute(sql, val)
    mydb.commit()
    cursor.close()

def getTemp(num):
    cursor = mydb.cursor(dictionary=True)
    sql = "SELECT * FROM t_temp;"
    cursor.execute(sql)
    all = cursor.fetchall()
    cursor.close()
    return all


#Save Humidity
def saveHumidity(humidity, adjustData):
    cursor = mydb.cursor(dictionary=True)
    sql = "INSERT INTO t_humidity (timestamp, humidity,adjustData) VALUES (%s, %s);"
    val = (humidity, adjustData)
    cursor.execute(sql, val)
    mydb.commit()
    cursor.close()

def getHumidity(num):
    cursor = mydb.cursor(dictionary=True)
    sql = "SELECT * FROM t_humidity;"
    cursor.execute(sql)
    all = cursor.fetchall()
    cursor.close()
    return all


#Save soil moisture
def saveMoisture(moisture, adjustData):
    cursor = mydb.cursor(dictionary=True)
    sql = "INSERT INTO t_humidity (timestamp, humidity,adjustData) VALUES (%s, %s);"
    val = (moisture, adjustData)
    cursor.execute(sql, val)
    mydb.commit()
    cursor.close()

def getMoisture(num):
    cursor = mydb.cursor(dictionary=True)
    sql = "SELECT * FROM t_moisture;"
    cursor.execute(sql)
    all = cursor.fetchall()
    cursor.close()
    return all