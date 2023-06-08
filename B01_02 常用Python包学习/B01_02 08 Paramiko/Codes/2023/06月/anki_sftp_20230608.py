import paramiko


t = paramiko.Transport('1.1.1.1',22)
t.connect(username='1',password='2')
sftp = paramiko.SFTPClient.from_transport(t)
lp = ''
rp = ''
sftp.get(rp,lp)

sftp.close()
t.close()








