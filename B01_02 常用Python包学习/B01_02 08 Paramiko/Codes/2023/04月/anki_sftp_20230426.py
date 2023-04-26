import paramiko


t = paramiko.Transport('',22)
t.connect(
    username = "",
    password = ""
)
sftp = paramiko.SFTPClient.from_transport(t)
lp = ''
rp = ''
sftp.get(rp,lp)

sftp.close()
t.close()







