# python实现数据库更新操作：将scores表中id=9的score更新为66
import pymysql

db = pymysql.connect(
    host = '',
    user = '',
    password = '',
    database = ''
)

cursor = db.cursor()
sql_update = 'update scores set score={} where id = 9'.format(66)

try:
    cursor.execute(sql_update)
    db.commit()

except Exception as res:
    db.rollback()
    print(res)
db.close()

