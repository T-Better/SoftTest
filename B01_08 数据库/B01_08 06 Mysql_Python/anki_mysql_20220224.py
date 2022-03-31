import pymysql
import pytest

db = pymysql.connect(
    host='192.168.146.129',
    user='root',
    password='123456',
    database='student'
)

cursor = db.cursor()

mysql_insert = "insert into scores(id,courseNo,studentno,score)\
values('9','2','003','88')"
mysql_select = ""
mysql_update = ""
mysql_delete = ""


def mysql_query(mysql_selete):
    cursor.selete(mysql_selete)
    data = cursor.fetchall()
    return data

try:
    # 查询
    print(mysql_query(mysql_select))
    # 插入
    cursor.execute(mysql_insert)
    db.commit()
    print('插入成功')
    # 查询
    print(mysql_query(mysql_select))

    # 修改
    cursor.execute(mysql_update)
    db.commit()
    print('修改成功')

    # 查询
    print(mysql_query(mysql_select))

    # 删除
    cursor.execute(mysql_delete)
    db.commit()

    # 查询
    print(mysql_query(mysql_select))
except Exception as res:
    db.rollback()
    print(res)







