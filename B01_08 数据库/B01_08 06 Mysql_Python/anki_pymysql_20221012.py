import pymysql

db = pymysql.connect(
    host = '192.168.146.129',
    user = 'root',
    password = '123456',
    database = 'students'
)

cursor = db.cursor()

sql_d = "delete from scores where id={}".format(9)

try:
    cursor.execute(sql_d)
    db.commit()
    print('success')
except Exception as res:
    db.rollback()
    print('fail')

db.close()



















