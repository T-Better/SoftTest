import pymysql

db = pymysql.connect(

)

cursor = db.cursor()

cursor.execute('')

data = cursor.fetchall()
print(data)

db.close()
