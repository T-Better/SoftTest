import paramiko
"""
t = paramiko.Transport(ip,port)
t.connect(username='',password = '123456')
chan = t.open_session()
"""
# 从widnows端上传文件到linux服务器
t = paramiko.Transport('',22)
t.connect(username='',password='123')
chan = t.open_session()

# ssh打开远程的terminal
t = paramiko.Transport(ip,22)
t.connect(username='',password='123')
chan = t.open_session()
chan.settimeout(12)
chan.get_pty()
# 从widnows端下载linux服务器上的文件:home/python下的test.txt
sftp = paramiko.SFTPClient.from_transport(t)
localpath= ''
remotepath = ''
sftp.get(remotepath,localpath)

# windows对linux运行pwd命令,并将结果输出
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect()
stdin, stdout, stderr = ssh.exec_command('pwd')

#激活terminal
chan.invoke_shell()

print(stdout.readlines())

t.close()







