
import paramiko
from sendmail2 import Mail



def sshCommand(hostname, username, password, command):
    try:
        port = 22
        sshClient = paramiko.SSHClient()                                   # create SSHClient instance
        sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())    # AutoAddPolicy automatically adding the hostname and new host key
        sshClient.load_system_host_keys()
        sshClient.connect(hostname, port, username, password)
        print("Connecting ...")
        stdin, stdout, stderr = sshClient.exec_command(command)
        print(stdout.read())
        print("Command executed")
    except paramiko.ssh_exception.NoValidConnectionsError:
        print ("{} address is invalid.".format(hostname))
        # mail1 = Mail('sender_email','sender_password')
        # mail1.sendmail('receiver_email',"Connection is not established with {}\n".format(hostname))
    except paramiko.ssh_exception.AuthenticationException:
        print ("Your username or password is invalid.\n")
        # mail1 = Mail('sender_email','sender_password')
        # mail1.sendmail('receiver_email',"Invalid username or password of {}\n".format(username))
        print ("mail has been sent\n")

# sshCommand('192.168.8.100', 'elliot', 'helloworld',"ls -l")
