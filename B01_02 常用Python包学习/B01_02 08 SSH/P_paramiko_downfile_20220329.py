import paramiko

t = paramiko.Transport(("192.168.146.128",22))
t.connect(username="python",password="chuanzhi")
sftp = paramiko.SFTPClient.from_transport(t)
remotepath='/home/python/test.txt'
localpath=r'D:\BaiduNetdiskWorkspace\Super_coder\Soft_test\C66_30 其他Codes\Paramiko\test_20220329.txt'
sftp.get(remotepath, localpath)
t.close()
