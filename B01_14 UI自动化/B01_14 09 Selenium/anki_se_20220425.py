# ssh
import paramiko


# 从widnows端下载linux服务器上的文件:home/python下的test.txt
t = paramiko.Transport('192.168.146.128',22)
t.connect(username='python',password='chuanzhi')
sftp = paramiko.SFTPClient.from_transport(t)
remotepath = r'/home/python/test.txt'
localpath = r'D:\BaiduNetdiskWorkspace\Super_coder\Soft_test\C66_30 其他Codes\Paramiko\test_20220425.txt'
sftp.get(remotepath,localpath)

t.close()

# allure+pytest
# pytest -s --allure-feature=feature




