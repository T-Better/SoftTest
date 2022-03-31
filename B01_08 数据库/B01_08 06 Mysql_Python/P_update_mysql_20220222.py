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

# 写更新sql 变量类型
sql_update_scores = "UPDATE scores set score = %s where id = 9" % (66)

# SQL 更新语句
try:
    # 执行SQL语句
    cursor.execute(sql_update_scores)
    # 提交到数据库执行
    db.commit()
    print('success')
except Exception as res:
    # 发生错误时回滚
    db.rollback()
    print(res)
    print('fail')

# 关闭数据库连接
db.close()
