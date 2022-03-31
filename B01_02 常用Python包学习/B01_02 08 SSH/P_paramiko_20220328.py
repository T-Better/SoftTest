import paramiko

# 创建ssh对象
ssh = paramiko.SSHClient()

# 允许连接不在know_hosts文件中的助记
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 链接服务器
ssh.connect(
    hostname='192.168.146.128',
    port=22,
    username='python',
    password='chuanzhi'
)

# 执行命令
stdin, stdout, stderr = ssh.exec_command('ls')

# 获取命令结果
result = stdout.read()

print(str(result, encoding='utf-8'))

# 关闭链接
ssh.close()