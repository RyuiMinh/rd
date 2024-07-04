import os
import subprocess

# Nhập mã CRD SSH và các thông tin người dùng
CRD_SSH_Code = input("Google CRD SSH Code: ")
username = "ns"
password = "root"
Pin = 654321

# Tạo người dùng mới và thiết lập quyền sudo
os.system(f"useradd -m {username}")
os.system(f"adduser {username} sudo")
os.system(f"echo '{username}:{password}' | sudo chpasswd")
os.system("sed -i 's/\/bin\/sh/\/bin\/bash/g' /etc/passwd")


class CRDSetup:
    def __init__(self, user):
        os.system("apt --assume-yes update")
        os.system("apt --assume-yes upgrade")
        self.installCRD()
        self.installGoogleChrome()
        self.installDesktopEnvironment()
        self.finish(user)

    @staticmethod
    def installCRD():
        deb_file = 'chrome-remote-desktop_current_amd64.deb'

        if not os.path.exists(deb_file):
            subprocess.run(
                ['wget', 'https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb'])

        if os.path.exists(deb_file):
            subprocess.run(['dpkg', '--install', deb_file])
            subprocess.run(['apt', 'install', '--assume-yes', '--fix-broken'])
            print("Chrome Remote Desktop Installed!")

    @staticmethod
    def installDesktopEnvironment():
        os.system("export DEBIAN_FRONTEND=noninteractive")
        os.system("apt install --assume-yes gnome-shell ubuntu-gnome-desktop gnome-terminal")
        os.system("bash -c 'echo \"exec /etc/X11/Xsession /usr/bin/gnome-session\" > /etc/chrome-remote-desktop-session'")
        os.system("apt remove --assume-yes xfce4-terminal")
        os.system("apt install --assume-yes gnome-screensaver")
        os.system("sudo service gdm3 stop")
        os.system("sudo apt-get install dbus-x11 -y")
        os.system("service dbus start")
        print("Installed GNOME Desktop Environment!")

    @staticmethod
    def installGoogleChrome():
        deb_file = 'google-chrome-stable_current_amd64.deb'

        if not os.path.exists(deb_file):
            subprocess.run(
                ['wget', 'https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb'])

        if os.path.exists(deb_file):
            subprocess.run(['dpkg', '--install', deb_file])
            subprocess.run(['apt', 'install', '--assume-yes', '--fix-broken'])
            print("Google Chrome Installed!")
        else:
            print(f"Download of {deb_file} failed. Installation aborted.")

    @staticmethod
    def finish(user):
        os.system(f"adduser {user} chrome-remote-desktop")
        command = f"{CRD_SSH_Code} --pin={Pin}"
        os.system(f"su - {user} -c '{command}'")
        os.system("service chrome-remote-desktop start")
        print(" ..........................................................")
        print(f"Log in PIN : {Pin}")
        print(f"User Name : {user}")
        print("User Pass : root")
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
