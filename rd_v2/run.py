import os
import subprocess
import shutil

CRD_SSH_Code = input("Google CRD SSH Code :")
username = "ns"
password = "root"
os.system(f"useradd -m {username}")
os.system(f"adduser {username} sudo")
os.system(f"echo '{username}:{password}' | sudo chpasswd")
os.system("sed -i 's/\/bin\/sh/\/bin\/bash/g' /etc/passwd")
try:
    if CRD_SSH_Code == "":
        print("Please enter authcode from the given link")
    elif len(str(Pin)) < 6:
        print("Enter a pin more or equal to 6 digits")
    else:
        CRDSetup(username)
except NameError as e:
    print("'username' variable not found, Create a user first")

Pin = 654321

class CRDSetup:
    def __init__(self, user):
        os.system("apt update")
        self.finish(user)
        
    @staticmethod
    def finish(user):
        os.system(f"adduser {user} chrome-remote-desktop")
        command = f"{CRD_SSH_Code} --pin={Pin}"
        os.system(f"su - {user} -c '{command}'")
        os.system("service chrome-remote-desktop start")
        print(" ..........................................................")
        print("Log in PIN : 654321") 
        print("User Name : user") 
        print("User Pass : root") 
        while True:
            pass
