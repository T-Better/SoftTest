import paramiko


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(
    hostname='',
    port=22,
    username='',
    password=''
)

stdin,stdout,stderr = ssh.exec_command('pwd')

ssh.close()




