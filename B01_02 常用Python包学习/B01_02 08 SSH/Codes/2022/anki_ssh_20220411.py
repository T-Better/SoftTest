import paramiko
"""
t = paramiko.Transport()
t.connect(username='',password='')
chan = t.open_session()
chan.settimeout()
chan.get_pty()
"""
# 从widnows端上传文件到linux服务器
"""
t = paramiko.Transport()
t.connect(username='',passowrd='')
sftp = paramiko.SFTPClient.from_transport(t)
remotepath=''
localpath = ''
sftp.put(localpath, remotepath)
t.close()
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
stdin, stdout, stderr = ssh.exec_command('pwd')
ssh.close()

# t = paramiko.Transport()
# chan = t.open_session()

# 从widnows端下载linux服务器上的文件:home/python下的test.txt
"""
t = paramiko.Transport('ip',22)
t.connect(username='',password = '')
sftp = paramiko.SFTPClient.from_transport(t)
remotepath = ''
localpath = ''
sftp.get(remotepath, localpath)
t.close()
"""
# 三月：march
# alignment:对其

