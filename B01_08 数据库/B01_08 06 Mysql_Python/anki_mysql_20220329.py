import pymysql

db = pymysql.connect(
    host='192.168.146.129',
    user='root',
    password='123456',
    database='student'
)

cursor = db.cursor()

sql_delete = "delete from scores where id={}".format(9)

try:
    cursor.execute(sql_delete)
    db.commit()
except Exception as res:
    db.rollback()
    print(res)

cursor.close()
db.close()




