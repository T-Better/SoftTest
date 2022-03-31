import pymysql

db = pymysql.connect(
    host='192.168.146.129',
    user='root',
    password='123456',
    database='student'
)

cursor = db.cursor()

sql_query1 = "SELECT * FROM students where studentno = 1"

sql_query2 = "select * from students where age > 20"

sql_insert = "insert into scores(id,courseNo,studentno,score)\
            values({},{},{},{})".format(10,3,"002","69")

try:
    cursor.execute(sql_query2)
    data = cursor.fetchall()
    # print(data)
    for row in data:
        dname = row[1]
        dsex = row[2]
        dhometown = row[3]
        dage = row[4]
        dclass = row[5]
        print("name={},sex={},hometown={},age={},class={}".format(dname,dsex, \
                    dhometown, dage, dclass))
except Exception as res:
    db.rollback()
    print(res)


