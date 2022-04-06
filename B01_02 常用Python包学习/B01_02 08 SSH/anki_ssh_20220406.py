import paramiko

"""
t = paramiko.Transport()
t.connect()
chan = t.open_session()
chan.settimeout(5)
chan.get_pty()


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
"""

# 使用两种方法实现ssh链接本地虚拟机：
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect()

# 二
t = paramiko.Transport()
t.connect()
sftp = paramiko.SFTPClient.from_transport(t)
remotepath = r'\home\python\致您的一封信.doc'
localpath = r'D:\Work\C-人行-浪潮\C00-浪潮\C03_文档\致您的一封信.doc'
sftp.put(localpath, remotepath)
sftp.get(localpath, remotepath)
t.close()

# 将滚动条滑到最顶层
js1 = "window.scrollTo(0,0)"
driver.execute_script(js1)

