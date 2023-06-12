import paramiko


t = paramiko.Transport('1.1.1.1', 22)
t.connect(username='python',password = 'chuanzhi')
sftp = paramiko.SFTPClient.from_transport(t)

lp = ''
rp = ''
sftp.put(lp,rp)

sftp.close()
t.close()







