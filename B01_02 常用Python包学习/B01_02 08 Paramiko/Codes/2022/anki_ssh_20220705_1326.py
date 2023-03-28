import paramiko

t = paramiko.Transport(ip,port)
t.connect(username='',password='')
chan = t.open_session()
chan.settimeout(3)
chan.get_pty()
chan.invoke_shell()
chan.send('pwd')



