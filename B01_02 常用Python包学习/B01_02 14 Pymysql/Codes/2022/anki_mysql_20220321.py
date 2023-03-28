import pymysql

db = pymysql.connect(
    host='192.168.146.129',
    user='root',
    password='123456',
    database='student'
)

cursor = db.cursor()

sql_u = "update scores set score={} where id = 9".format(66)

sql_q = "SELECT * FROM students where studentno = 1"

try:
    # cursor.execute(sql_u)
    # db.commit()
    # print('更新成功')
    cursor.execute(sql_q)
    data = cursor.fetchone()
    print(data)
except Exception as res:
    print(res)
    db.rollback()

db.close()
