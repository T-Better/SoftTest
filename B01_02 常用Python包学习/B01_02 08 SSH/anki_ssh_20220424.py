import paramiko

t = paramiko.Transport('127.0.0.1',22)
t.connect(username='',password='')
chan = t.open_session()
chan.settimeout(22)
chan.get_pty()
chan.invoke_shell()
sftp = paramiko.SFTPClient.from_transport(t)
remotepath = ''
localpath = ''
sftp.put(localpath, remotepath)
t.close()
# 获取告警框的文字信息
# alert.text

# windows对linux运行pwd命令,并将结果输出
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect()
stdin, stdout, stderr = ssh.exec_command('pwd')
print(stdout)

ssh.close()
