import os
import subprocess

CRD_SSH_Code = input("Google CRD SSH Code: ")
username = "ns"
password = "root"
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
        print(f"Log in PIN : {Pin}")
        print(f"User Name : {user}")
        print(f"User Pass : {password}")
        while True:
            pass


try:
    if CRD_SSH_Code == "":
        print("Please enter authcode from the given link")
    elif len(str(Pin)) < 6:
        print("Enter a pin more or equal to 6 digits")
    else:
        CRDSetup(username)
except NameError as e:
    print("'username' variable not found, Create a user first")
