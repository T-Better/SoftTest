import pymysql

db = pymysql.connect(
    host='192.168.146.129',
    user='root',
    password='123456',
    database='student'
)

cursor = db.cursor()

sql_query = "select * from students where age > %s" % (20)

try:
    cursor.execute(sql_query)
    data = cursor.fetchall()
    for each in data:
        sname = each[1]
        ssex = each[2]
        shometown = each[3]
        sage = each[4]
        sclass = each[5]
        print("姓名:{}, 性别:{},家乡：{},\
年龄：{},班级：{}".format(sname, ssex,shometown, sage, sclass))
except Exception as res:
    db.rollback()
    print(res)
