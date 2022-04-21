import paramiko


# 使用两种方法实现ssh链接本地虚拟机：
# 方法一：
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('127.0.0.1',22,'zhangsan','111111')


# 方法二：
t = paramiko.Transport('127.0.0.1',22)
t.connect(username='zhangsan',password='111111')
sftp = paramiko.SFTP








