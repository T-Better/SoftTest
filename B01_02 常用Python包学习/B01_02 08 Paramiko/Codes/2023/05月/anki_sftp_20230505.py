import paramiko


t = paramiko.Transport('',22)
t.connect(username = '',password = '')

lp = r'/home/python/test.txt'
rp = r'/home/python/test.txt'
sftp = paramiko.SFTPClient.from_transport(t)
sftp.get(rp,lp)


