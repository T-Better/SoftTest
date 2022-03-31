import pymysql

db = pymysql.connect(
    host='192.168.146.129',
    user='root',
    password='123456',
    database='student'
)
cursor = db.cursor()
sql_insert1 = "insert into scores(id,courseNo,studentno,score)\
              values({},{},{},{})".format('9','2','003','88')

try:
    cursor.execute(sql_insert1)
    db.commit()
except Exception as res:
    print(res)
    db.rollback()

db.close()


