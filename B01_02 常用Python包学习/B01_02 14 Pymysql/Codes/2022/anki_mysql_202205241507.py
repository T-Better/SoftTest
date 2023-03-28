import pymysql

db = pymysql.connet(
    host='192.168.146.129',
    user='root',
    password='123456',
    database='student'
)

cursor = db.cursor()

sql1 = "insert into scores(id,courseNo,studentno,score)\
values('9','2','003','88');"

try:
    cursor.execute(sql1)
    db.commit()
except Exception as res:
    print(res)
    db.rollback()
