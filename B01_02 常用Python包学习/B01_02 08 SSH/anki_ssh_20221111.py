import paramiko

t = paramiko.Transport('1.1.1.1',22)
t.connect(
    username = '1',
    password = '1'
)
chan = t.open_session()
chan.settimeout()



