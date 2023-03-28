import pymysql

# 打开数据库链接
db = pymysql.connect(
    host='192.168.146.129',
    user='root',
    password = '123456',
    database = 'student'
)

# 使用cursor()方法创建一个游标对象cursor
cursor = db.cursor()

# 使用execute()方法执行sql查询
cursor.execute('select * from students where name = "王昭君";')

# 使用fetchone()方法获取单条数据
data = cursor.fetchall()

print(data)

# 关闭数据库链接
db.close()

