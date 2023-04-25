import paramiko

t = paramiko.Transport('1.1.1.1',22)
t.connect(username='',password='')

sftp = paramiko.SFTPClient(t)
rp = ''
lp = ''
sftp.put(lp,rp)


sftp.close()
t.close()




