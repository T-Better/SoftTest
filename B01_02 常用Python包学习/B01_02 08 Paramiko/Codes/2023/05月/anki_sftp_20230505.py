import paramiko


t = paramiko.Transport('',22)
t.connect(username='',password='')

sftp = paramiko.SFTPClient.from_transport(t)

rp = r'\home\python\致您的一封信.doc'
lp = r'D:\Work\C-人行-浪潮\C00-浪潮\C03_文档\致您的一封信.doc'
sftp.get(rp,lp)
sftp.put(lp,rp)

sftp.close()
t.close()




