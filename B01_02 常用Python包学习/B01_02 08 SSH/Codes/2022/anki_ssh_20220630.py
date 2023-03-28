import paramiko

t = paramiko.Transport('192.168.146.128',22)
t.connect(username='',password='')
sftp = paramiko.SFTPClient.from_transport(t)
remotepath = ''
localpath = ''
sftp.get(remotepath,localpath)

t.close()



