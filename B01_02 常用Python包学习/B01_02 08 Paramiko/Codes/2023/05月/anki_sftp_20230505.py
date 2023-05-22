import paramiko

# TODO
t = paramiko.Transport('192.168.146.128',22)
t.connect(
    username = "python",
    password = ""
)
sftp = paramiko.SFTPClient.from_transport(t)
rp = ""
lp = ""
sftp.put(lp,rp)
sftp.close()
t.close()

