import pymysql

db = pymysql.connect(
    host = '192.168.146.129',
    user = 'root',
    password = '123456',
    database = 'student'
)

cursor = db.cursor()

sql_query1 = "select * from scores"

sql_update1 = "update scores set score = {} where id = {}".format(77, 9)

try:
    cursor.execute(sql_update1)
    db.commit()
    print('update success')

    cursor.execute(sql_query1)
    data = cursor.fetchall()
    for row in data:
        print(row)
    # print(data)
except Exception as res:
    db.rollback()
    print(res)

db.close()





