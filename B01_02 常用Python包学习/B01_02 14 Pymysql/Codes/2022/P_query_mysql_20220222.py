import pymysql

# 创建链接
db = pymysql.connect(
    host = '192.168.146.129',
    user = 'root',
    password = '123456',
    database = 'student'
)
# 创建游标
cursor = db.cursor()

# 创建sql查询语句
sql = "SELECT * FROM students WHERE AGE > %s" % ('20')
# 执行sql
try:
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        sname = row[1]
        ssex = row[2]
        shometown = row[3]
        sage = row[4]
        sclass = row[5]
        print("name=%s,sex=%s,hometown=%s,age=%s,class=%s" % (sname, ssex, shometown, sage, sclass ))
except Exception as res:
    print ("Error: unable to fetch data")
    print(res)
