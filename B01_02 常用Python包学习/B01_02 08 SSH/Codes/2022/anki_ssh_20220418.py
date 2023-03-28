import paramiko

# ssh打开远程的terminal
t = paramiko.Transport('ip',22)
t.connect(username='',password='')
chan = t.open_session()
chan.settimeout(4)
chan.get_pty()

# windows对linux运行pwd命令,并将结果输出
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(
    hostname='',
    port = ,
    username = '',
    password = ''
)
stdin, stdout, stderr = ssh.exec_command('pwd')
print(stdout)

ssh.close()

# 显式与隐式区别
# 引用模块不同，隐式可以直接用driver驱动，无需引入。显式需要重新引入模块，然后实例化使用；
# 超时结果不同，隐式等待会报未发现错误，显式等待会报超时

# 从widnows端上传文件到linux服务器：
t = paramiko.Transport('ip',22)
t.connect(username='',password='')
sftp = paramiko.SFTPClient.from_transport(t)
remotepath = ''
localpath = ''
sftp.put(localpath,remotepath)
t.close()

# 从widnows端下载linux服务器上的文件:home/python下的test.txt
sftp.get(remotepath,localpath)



