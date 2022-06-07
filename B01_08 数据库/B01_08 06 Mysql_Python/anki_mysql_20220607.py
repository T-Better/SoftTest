import pymysql

db = pymysql.connect(
    host = '',
    user = '',
    password = '',
    database = ''
)

cursor = db.cursor()

sql1 = 'update scores set score=66 where id=9';

try:
    cursor.execute(sql1)
    db.commit()
except Exception as res:
    db.rollback()
    print(res)

db.close()






