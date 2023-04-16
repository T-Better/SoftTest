"""
hostname='192.168.146.128',
port=22,
username='python',
password='chuanzhi'
要发送到linux的位置和文件：r'\home\python\致您的一封信.doc'
要发送文件所在本地位置：r'D:\Work\C-人行-浪潮\C00-浪潮\C03_文档\致您的一封信.doc'
"""
import paramiko

rp = r'\home\python\致您的一封信.doc'
lp = r'D:\Work\C-人行-浪潮\C00-浪潮\C03_文档\致您的一封信.doc'

t = paramiko.Transport('192.168.146.128',22)
t.connect(username='',password='')
sftp = paramiko.SFTPClient(t)


# 从widnows端上传文件到linux服务器
sftp.put(lp,rp)

# 下载
sftp.get(lp,rp)

sftp.close()
t.close()
