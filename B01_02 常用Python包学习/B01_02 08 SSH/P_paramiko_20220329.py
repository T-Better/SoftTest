import paramiko

ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
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



