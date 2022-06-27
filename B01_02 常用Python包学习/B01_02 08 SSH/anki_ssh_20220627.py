import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(
    hostname='192.168.146.128',
    port=22,
    username='python',
    password='chuanzhi'
)

# 2
t = paramiko.Transpost('192.168.146.128',22)
t.connect(username='python',password='chuanzhi')
localpath = r'D:\Work\C-人行-浪潮\C00-浪潮\C03_文档\致您的一封信.doc'
remotepath = r'\home\python\致您的一封信.doc'
t.put(localpath,remotepath)
t.close()
