import paramiko

t = paramiko.Transport(ip,port)
t.connect(username='',password='')
chan = t.open_session()
chan.settimeout(5)
chan.get_pty()


