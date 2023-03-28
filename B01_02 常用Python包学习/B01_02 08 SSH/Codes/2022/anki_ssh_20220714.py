import paramiko

t = paramiko.Transport('192.168.146.128',22)
t.connect(username='python',password='')
sftp = paramiko.SFTPClient.from_transport(t)
remotepath = r'D:\Work\C-人行-浪潮\C00-浪潮\C03_文档\致您的一封信.doc'
localpath = r'\home\python\致您的一封信.doc'
sftp.put(localpath,remotepath)

t.close()



