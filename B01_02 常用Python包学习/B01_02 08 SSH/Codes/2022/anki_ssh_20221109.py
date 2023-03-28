import paramiko

t = paramiko.Transport('1.1.1.1',22)
t.connect(username='',password='')
chan = t.open_session()
chan.settimeout(3)
chan.get_pty()





