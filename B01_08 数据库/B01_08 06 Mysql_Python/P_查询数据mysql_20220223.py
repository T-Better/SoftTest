import pymysql

# 创建链接
db = pymysql.connect(
    host = '192.168.146.129',
    user = 'root',
    password = '123456',
    database = 'student'
)

# 获取游标
cursor = db.cursor()

# 查询sql
sql_query = "SELECT * FROM scores"
# 增加sql
sql_insert = "insert into scores(id,courseNo,studentno,score) \
            values(%s, %s, %s, %s)" % ('9', '2', '003', '88')
# 修改sql
sql_update = "update scores set score=%s where id=9" % ('66')

# 删除sql
sql_delete_scores = "delete from scores where id = 9"

# 执行sql
try:
    # 改之前先查询
    cursor.execute(sql_query)
    data1 = cursor.fetchall()
    print(data1)
    print("------------------------")

    # # 增加一行
    # cursor.execute(sql_insert)
    # db.commit()
    # cursor.execute(sql_query)  # 增加完再查
    # data2 = cursor.fetchall()
    # print(data2)
    # print('insert成功')

    # 更新：将scores表中id=9的score更新为66
    # cursor.execute(sql_update)
    # db.commit()
    # print('更新成功')
    # # 查询
    # cursor.execute(sql_query)
    # data3 = cursor.fetchall()
    # print(data3)

    # 删除
    cursor.execute(sql_delete_scores)
    db.commit()
    print('删除成功')

    # 删完再查
    cursor.execute(sql_query)
    data4 = cursor.fetchall()
    print(data4)

except Exception as res:
    db.rollback()
    print(res)
    print('查询失败')
