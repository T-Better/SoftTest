import pymysql

# 建立链接
db = pymysql.connect(
    host = '192.168.146.129',
    user = 'root',
    password = '123456',
    database = 'student'
)

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# sql删除语句 参数型
sql_delete = "delete from scores where id = 9"

try:
    cursor.execute(sql_delete)  # 执行SQL语句
    db.commit()  # 提交修改
except Exception as res:
    db.rollback()  # 发生错误时回滚
    print(res)

# 关闭连接
db.close()
