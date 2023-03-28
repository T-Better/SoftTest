import paramiko
# 从widnows端上传文件到linux服务器
t = paramiko.Transport('192.168.146.128', 22)
t.connect(username='python',password='chuanzhi')
sftp = paramiko.SFTPClient.from_transport(t)
remotepath = r'\home\python\致您的一封信.doc'
localpath=r'D:\Work\C-人行-浪潮\C00-浪潮\C03_文档\致您的一封信.doc'
sftp.put(localpath,remotepath)
t.close()
# 到这了,未加入anki   `