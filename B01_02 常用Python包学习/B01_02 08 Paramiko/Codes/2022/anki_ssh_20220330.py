import paramiko
"""
windows对linux运行pwd命令,并将结果输出

"""

"""
从widnows端下载linux服务器上的文件:home/python下的test.txt
本地保存路径文件：D:\BaiduNetdiskWorkspace\Super_coder\Soft_test\C66_30 其他Codes\Paramiko\test_今天日期.txt

t = paramiko.Transport('192.168.146.128',22)
t.connect(username='python',password='chuanzhi')
sftp = paramiko.SFTPClient.from_transport(t)
remotepath = r'home/python/test.txt'
localpath = r'D:\BaiduNetdiskWorkspace\Super_coder\Soft_test\C66_30 其他Codes\Paramiko\test_20220330.txt'
sftp.get(remotepath, localpath)

t.close()
"""

"""
使用两种方法实现ssh链接本地虚拟机：

# 方法一：非文件传输
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(
    hostname='192.168.146.128',
    port=22,
    username='python',
    password='chuanzhi'
)

# 方法二：文件传输
t = paramiko.Transport('ip',22)
t.connect(username='',password='')
"""

# 设置ssh连接的远程主机地址和端口
t = paramiko.Transport(ip,port)

# ssh:设置登录名和密码
t = paramiko.Transport(ip,port)
t.connect(username='',password='')

# ssh#连接成功后打开一个channel
t = paramiko.Transport(ip,port)
t.connect()
chan = t.open_session()

# ssh设置会话超时时间
chan.settimeout(session_timeout)

# ssh打开远程的terminal
chan.get_pty()

# ssh激活terminal
chan.invoke_shell()
chan.send('')
chan.recv()
