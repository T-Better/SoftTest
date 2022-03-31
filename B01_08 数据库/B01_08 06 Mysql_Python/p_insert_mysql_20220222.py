import pymysql

# 打开数据库链接
db = pymysql.connect(
    host = '192.168.146.129',
    user = 'root',
    password = '123456',
    database = 'student'
)
# 使用cursor()获取操作游标
cursor = db.cursor()

# sql插入语句
'''
# 方法一
sql1 = """
      insert into scores(id, courseNo, studentno, score) \
      values('9','2', '003', '88');"""
'''

# 方法二：可使用变量向SQL语句中传递参数
sql1 = "insert into scores(id, courseNo, studentno, score)\
        values (%s, %s, %s, %s)" % (9, 2, '003', 88)

try:
    # 执行sql语句
    cursor.execute(sql1)
    db.commit()
except Exception as res:
    # 发生错误则回滚
    db.rollback()
    print('fail')
    print(res)

# 关闭数据库链接
db.close()


