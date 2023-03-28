import pymysql
"""
# 1
db = pymysql.connect(
    host = '',
    user = '',
    password = '',
    database = ''
)

cursor = db.cursor()

sql_u = "update scores set score = {} where id=9".format(66)

try:
    cursor.execute(sql_u)
    db.commit()
    print('success')
except Exception as res:
    db.rollback()
    print('fail')

db.close()
"""

#2
db = pymysql.connect(
    host = '',
    user = '',
    password = '',
    database = ''
)

cursor = db.cursor()

sql_i = "insert into scores(id,courseNo,studentno,score) values('10','2','005','88')"

try:
    cursor.execute(sql_i)
    db.commit()
    print('insert success')
except Exception as res:
    db.rollback()
    print('insert fail')

db.close()











