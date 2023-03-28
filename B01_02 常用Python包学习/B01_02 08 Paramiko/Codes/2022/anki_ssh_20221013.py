import paramiko

# 从widnows端上传文件到linux服务器：
t = paramiko.Transport('1.1.1.1',22)
t.connect(username='zs',password='pd')
chan = t.open_session()
sftp = paramiko.SFTPClient.from_transport(t)
remotepath = ''
localpath = ''
sftp.put(remotepath,localpath)
t.close()








