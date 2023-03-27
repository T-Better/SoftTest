import paramiko

t = paramiko.Transport('',22)
t.connect(username='',password='')
chan = t.open_session()
sftp = paramiko.SFTPClient.from_transport(t)
remotepath = ''# 定好对端地址
localpath = ''# 本端地址
sftp.put(localpath,remotepath)
sftp.get(remotepath,localpath)
t.close()




