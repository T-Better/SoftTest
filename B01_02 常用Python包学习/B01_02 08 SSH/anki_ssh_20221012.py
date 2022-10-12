import paramiko

# windows对linux运行pwd命令,并将结果输出
"""
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(
    hostname='192.168.146.128',
    port = 22,
    username = 'python',
    password = 'chuanzhi'
)
stdin,stdout,stderr = ssh.exec_command('pwd')
print(stdout.readlines())
ssh.close()
"""

# 默写
"""
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(
    hostname = '',
    port = ,
    username='',
    password = ''
)
stdin,stdout,stderr = ssh.exec_command('pwd')
print(stdout.readlines())
ssh.close()
"""

# ssh激活terminal
"""
# 指定连接点
t = paramiko.Transport('1.1.1.1',22)
# 建立连接
t.connect(username='',password='')
# 打开通道
chan = t.open_session()
# 设置会话时间
chan.settimeout(5)
# 打开远程终端
chan.get_pty()
# 激活终端
chan.invoke_shell()
# 发送指令
chan.send('pwd')
# 接收指令
chan.recv('ls')
t.close()
"""

# 使用两种方法实现ssh链接本地虚拟机
"""
# 方法一
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(
    "1.1.1.1",
    22,
    'username',
    'password'
)

# 方法二
t = paramiko.Transport('1.1.1.1',22)
t.connect(username='zs',password='123')
sftp = paramiko.SFTPClient()
"""

# 从widnows端下载linux服务器上的文件:home/python下的test.txt
t = paramiko.SFTPClient('1.1.1.1',22)
t.connect(username = '1',password = 'a')
chan = t.open_session()
sftp = paramiko.SFTPClient.from_transport(t)
remotepath = r'/home/python/test.txt'
localpath = r'D:\BaiduNetdiskWorkspace\Super_coder\Soft_test\C66_30 其他Codes\Paramiko\test_20221012.txt'
sftp.get(remotepath,localpath)
t.close()




