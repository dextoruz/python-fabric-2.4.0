
from fabric import task,Connection


@task              # hello world
def hello(i):
    i.run("echo 'Hello World!\n'")

@task              # change directory and multiple commands
def list1(i):
    i.run("mkdir -p demo")
    with i.cd("demo/"):
        i.run("touch {1..5}.txt")
        i.run("ls")
    i.run("rm -r demo")


@task              # using parameters
def newuser(ctx, uname, admin):
    print ("Old user {}.\n{} is new admin now.".format(uname,admin))
    # ctx.run("echo 'hello world!'")





from math import pi
def areaCircle(r):
    print("Area of radius {}cm circle is {:.3f}cm sq.".format(r,pi*pow(r,2)))

@task               ## using other functions
def getArea(i):
    areaCircle(3)
    areaCircle(4)
    areaCircle(5)

@task               # function call
def allTasks(i):
    hello(i)
    getArea(i)





from invoke import Responder

@task               # automate/autorespond sudo password
def passd(i):
    sudopass = Responder(
    pattern=r'\[sudo\] password for sasuke:',  #terminal output pattern matching
    response='helloworld\n',)                  #password
    i.run('sudo apt update', pty=True, watchers=[sudopass])




############# EXAMPLE 01 ############


from teacherAttendance import teacherAtt

@task               # mail from admin to academics
def mailAdmin(a):
    a.run("python send_mail.py")                            #
    a.run("echo 'mail has been sent\n'")


@task               # zip files
def zipAtt(a):
    teacherAtt()                                # update attendance
    a.run( "zip teacherAttendance -r teacher")
    a.run( "echo 'directory successfully ziped\n'")
    mailAdmin(a)
    a.run( "rm -r teacherAttendance.zip")


#########################################






############# EXAMPLE 02 ################



from sshClient import sshCommand

hosts = {
# '192.168.8.100' : ["elliot","helloworld"],
"192.168.1.146": ["mackrugeri","macsoft123"]
}


@task               # run commands on other machines or SSH
def runCommand(a):
    command = "cd ~/Desktop && touch hello.txt"
    for i,j in hosts.items():
        sshCommand(i,j[0],j[1],command)



#########################################
