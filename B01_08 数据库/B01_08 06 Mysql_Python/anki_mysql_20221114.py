import pymysql

db = pymysql.connect(
    host = '',
    user = 'root',
    password = '123456',
    database = 'student'
)

sql1 = 'select * from students where studentno = 1'

cursor = db.cursor()

try:
    cursor.execute(sql1)
    db.commit()
except:
    db.rollback()
db.close()

