import paramiko
"""
# 使用两种方法实现ssh链接本地虚拟机：
# 方法一：执行指令

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(
    hostname='192.168.146.128',
    port=22,
    username='python',
    password='chuanzhi'
)

# 方法二：文件传输
t = paramiko.Transport('192.168.146.128',22)
t.connect(username='python', password='chuanzhi')
"""

"""
# ssh激活terminal
t = paramiko.Transport(ip,port)
t.connect(username='',password='')
chan = t.open_session()  # 打开一个session通道
chan.settimeout(5)  # 设置超时时间
chan.get_pty()  # 打开远程terminal
chan.invoke_shell()  # 激活terminal
chan.send('')  # 发送指令
"""
"""
# windows对linux运行pwd命令,并将结果输出
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(
    hostname='192.168.146.128',
    port=22,
    username='python',
    password='chuanzhi'
)
stdin, stdout, stder = ssh.exec_command('pwd')
print(stdout.read())
ssh.close()
"""

"""
从widnows端下载linux服务器上的文件:home/python下的test.txt
本地保存路径文件：D:\BaiduNetdiskWorkspace\Super_coder\Soft_test\C66_30 其他Codes\Paramiko\test_今天日期.txt

t = paramiko.Transport('192.168.146.128',22)
t.connect(username='python',password='chuanzhi')
sftp = paramiko.SFTPClient.from_transport(t)
remotepath = r'/home/python/test.txt'
localpath = r'D:\BaiduNetdiskWorkspace\Super_coder\Soft_test\C66_30 其他Codes\Paramiko\test_20220331.txt'
sftp.get(remotepath,localpath)
t.close()
"""
"""
# 设置ssh连接的远程主机地址和端口
t = paramiko.Transport(ip,port)
t.connect(username='',password='')
chan=t.open_session()
"""

"""
从widnows端上传文件到linux服务器：
要发送到linux的位置和文件：r'\home\python\致您的一封信.doc'
要发送文件所在本地位置：r'D:\Work\C-人行-浪潮\C00-浪潮\C03_文档\致您的一封信.doc'
"""
t = paramiko.Transport('192.168.146.128',22)
t.connect(username='python',password='chuanzhi')
sftp = paramiko.SFTPClient.from_transport(t)
remotepath = r''
localpath = r''
sftp.put(localpath,remotepath)
t.close()
