import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(
    hostname='192.168.146.128',
    port=22,
    username='python',
    password='chuanzhi'
)
stdin, stdout, stderr = ssh.exec_command('pwd')
print(stdout.readlines())

ssh.close()

# ssh打开远程的terminal
t = paramiko.Transport('ip',22)
t.connect(username='',password='')
chan = t.open_session()  #连接成功后打开一个channel
chan.settimeout(10)
chan.get_pty()
chan.invoke_shell()

