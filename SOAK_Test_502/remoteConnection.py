import paramiko
import os
import SOAK_Test_502.config as cof


def remoteConnection(lzDirPath):
    try:

        print("LZ directory path in remoteConnection  ",lzDirPath )
        localPath="C:\\Users\\zaloni\\Desktop\\Python_Project\\test_repo\\SOAK_Test_502\\test_local_file.txt"
        remotePath="/home/zaloni/test_copy_out/new.txt"
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        hostname = cof.HOST
        username = cof.CLI_username
        password = cof.CLI_password
        print(hostname,username,password)
        ssh.connect(hostname = hostname, username = username, password = password)
        #sftp = ssh.open_sftp()
        #sftp.put(localPath, remotePath)
        #sftp.close()
        stdin, stdout, stderr = ssh.exec_command('sshpass -p "zdp.1234" scp -r zaloni@10.1.3.6:/home/zaloni/Load_Script_Dir /home/zaloni/')
        print(stdout.readlines())
        print(stderr.readlines())
        a=cof.frequency
        stdin, stdout, stderr=  ssh.exec_command("(cd /home/zaloni/Load_Script_Dir; ./fileDropForSOAK1.sh "+str(a)+" "+str(lzDirPath)+")")
        print(stdout.readlines())
        print(stderr.readlines())
        ssh.close()
        return
    except Exception as e:
        print("Some Exception has been found:", e)





