#导包
import pymysql
#创建连接
conn = pymysql.connect(host="192.168.91.134",user="litemall",password="litemall123456",database="litemall",port=3306,charset='utf8')
#创建游标
cursor = conn.cursor()
#添加用户的SQL语句
user_sql = "INSERT INTO `litemall`.`litemall_user` (`id`, `username`, `password`, `gender`, `birthday`, `last_login_time`, `last_login_ip`, `user_level`, `nickname`, `mobile`, `avatar`, `weixin_openid`, `session_key`, `status`, `add_time`, `update_time`, `deleted`) VALUES ('{}', '{}', '$2a$10$SrnVvS/D6N0XNd4MHNjQR.W3VUfJhOdBylPC3Ika0zTvmxyiJ52AS', '0', NULL, '2020-08-14 12:00:58', '192.168.91.1', '0', 'xiaoh', '{}', 'https://yanxuan.nosdn.127.net/80841d741d7fa3073e0ae27bf487339f.jpg?imageView&quality=90&thumbnail=64x64', '', '', '0', '2020-08-12 14:14:37', '2020-08-14 12:00:58', '0');"
#循环插入数据
user_start = 100000
for i in range(100000):
    user_id = user_start + i
    username = "test" + str(user_id)
    mobile = "13012" + str(user_id)

    print("插入第{}条数据ID为{}".format(i+1,user_id))
    sql = user_sql.format(user_id,username,mobile)
    cursor.execute(sql)

    conn.commit()
#关闭游标
cursor.close()
#关闭连接
conn.close()