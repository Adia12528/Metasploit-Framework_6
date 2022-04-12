import os

os.system("pkg update")
os.system("pkg upgrade -y")
print("It will take some time be patient.")
os.system("pkg install wget curl openssh git -y")
os.system("apt install ncurses-utils")
os.system("git clone https://github.com/remo7777/Termux-Metasploit; cd Termux-Metaspl*;bash setup;")
print("You have successfully installed metasploit 6 in your termux")
print("Now you can run meyasploit without any error")
os._exit(1)
