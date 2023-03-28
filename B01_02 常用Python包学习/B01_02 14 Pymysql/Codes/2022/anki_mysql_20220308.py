import pymysql

db = pymysql.connect(
    host = '192.168.146.129',
    user ='root',
    password = '123456',
    database = 'student'
)

cursor = db.cursor()

mysql_delete = "delete from scores where id = {}".format(10)

try:
    cursor.execute(mysql_delete)
    db.commit()
    print('success')
except Exception as res:
    db.rollback()
    print(res)