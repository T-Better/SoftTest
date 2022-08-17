import paramiko

t = paramiko.Transport('192.168.11.11',22)
t.connect(username='root',password='123')
sftp = paramiko.SFTPClient.from_transport(t)
remotepath=''
localpath=''
sftp.put(localpath,remotepath)

# ssh打开远程的terminal
chan = t.open_session()
chan.settimeout(5)
chan.get_pty()
t.close()








