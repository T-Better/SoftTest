import paramiko

"""# 法一
t = paramiko.Transport('111.1.1.1',22)
t.connect(username='username',password='password')
chan = t.open_session()
chan.settimeout(5)
chan.get_pty()
chan.invoke_shell()
sftp = paramiko.SFTPClient.from_transport(t)
remotepath = ''
localpath = ''
sftp.get(remotepath,localpath)
t.close()
"""

"""# 法二
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connet('',22,'','')
stdin,stdout,stderr = ssh.exec_command('pwd')
ssh.close()
"""



