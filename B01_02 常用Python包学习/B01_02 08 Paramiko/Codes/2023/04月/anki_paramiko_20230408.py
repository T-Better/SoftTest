import paramiko


rp = r'\home\python\致您的一封信.doc'
lp = r'D:\Work\C-人行-浪潮\C00-浪潮\C03_文档\致您的一封信.doc'

t = paramiko.Transport('1.1.1.1',22)
t.connect(username='',password='')
sftp = paramiko.SFTPClient.from_transport(t)
# 从widnows端上传文件到linux服务器
sftp.put(lp, rp)

# TODO

t.close()

