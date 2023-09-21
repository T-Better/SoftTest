import pymysql


db = pymysql.connect(
    username='',
    password='',
    port='',
    database = ''
)

sql = r"delete from scores where id=9;"

cursor = db.cursor()

try:
    cursor.execute(sql)
    db.commit()
except Exception as r:
    print(r)
    db.rollback()

db.close()









