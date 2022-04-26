import pymysql

db = pymysql.connect(
    host = '192.168.146.129',
    user = 'root',
    password = '123456',
    database = 'student'
)

cursor = db.cursor()

sql_query1 = "select * from students where studentno = {}".format(1)

try:
    cursor.execute(sql_query1)
except Exception as res:
    print(res)

db.close()







