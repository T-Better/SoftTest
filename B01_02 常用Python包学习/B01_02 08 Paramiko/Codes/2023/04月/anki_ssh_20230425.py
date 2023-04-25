import paramiko


ssh = paramiko.SSHClient()
ssh.connect(
    hostname='192.168.146.128',
    port=22,
    username='python',
    password='chuanzhi'
)
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
stdin,stdout,stderr = ssh.exec_command('pwd')

ssh.close()







