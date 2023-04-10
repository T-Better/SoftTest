import paramiko


t = paramiko.Transport('',22)
t.connect(username='',password='')

sftp = paramiko.SFTPClient.from_transport(t)

rp = r'\home\python\致您的一封信.doc'
lp = r'D:\Work\C-人行-浪潮\C00-浪潮\C03_文档\致您的一封信.doc'
sftp.put(lp,rp)
sftp.get(rp,lp)

sftp.close()
t.close()

# select sex,count(*) as 数量 from students group by sex having sex='男';





