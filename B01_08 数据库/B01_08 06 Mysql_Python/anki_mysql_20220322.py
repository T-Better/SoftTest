import pymysql

db = pymysql.connect(
    host='192.168.146.129',
    user='root',
    password='123456',
    database='student'
)

cursor = db.cursor()

sql_q1 = "select * from students where age > {}".format(20)

try:
    cursor.execute(sql_q1)
    datas = cursor.fetchall()
    for data in datas:
        name1 = data[1]
        sex1 = data[2]
        hometown1 = data[3]
        age1 = data[4]
        class1 = data[5]
        print("name={},sex={},hometown={},age={},class={}".format(name1,sex1,hometown1,age1,class1))
except Exception as res:
    print(res)


