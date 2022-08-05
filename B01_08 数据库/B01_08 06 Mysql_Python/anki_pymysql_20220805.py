import pymysql

db = pymysql.connect(
    host = '',
    user = '',
    password = '',
    database = ''
)

cursor = db.cursor()

sql1 = "SELECT * FROM students where age > %s" % ('20')

try:
    cursor.execute(sql1)
    results = cursor.fetchall()
    for row in results:
        sname = row[1]
        ssex = row[2]
        shometown = row[3]
        sage = row[4]
        sclass = row[5]
        print("name=%s,sex=%s,hometown=%s,age=%s,class=%s" % (sname,ssex,shometown,sage,sclass))
except Exception as res:
    db.rollback()
    print(res)

db.close()


