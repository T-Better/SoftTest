import paramiko


t = paramiko.Transport('127.0.0.1',22)
t.connect(username='zhangsan',password='123456')
chan = t.open_session()


