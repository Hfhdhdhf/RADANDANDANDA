import os
import time
import math
import random
nmap = True
money = 0
InstallTime = 30
NetLevel2 = True

def mainGame():
    global nmap, money, InstallTime, NetLevel2
    if NetLevel2 == True:
        InstallTime = 15
    if nmap == True:
        money += 1000
        print("ur money is now:", money)
    print("Hello welcome back to the main menu")
    e = input("Please enter a command enter help for help>> ")
    if e == "generate random password":
        password = ""
        for i in range(random.randint(8, 16)):
            password += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()")
        print(password)
    if e == "hack":
        ip = random.randint(1, 1000)
        print("ip is now:", ip)
        ipselect = input("Please enter ur IP to access it>>")
        if ipselect == ip:
            print("1 Hack the ip by SSH port -- level 2")
            print("2 use nmap to level up")
            SelectedIP = input("Enter your choice: ")
            if SelectedIP == "2":
                if nmap == True:
                    #generate a random number between 1 and 99
                    port = random.randint(1, 99)
                    print("port is now:", port)
                    mainGame()
            if SelectedIP == "1":
                if nmap == True:
                    PasswordToHack = input("Enter your password -- we still dont have a tutorial>> ")
                    # set a variable with the entire alphabet and numbers and use random to shuffle it randomly
                    Alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLM"
                    Numbers = "0123456789"
                    Password = Alphabet + Numbers
                    GeneratedPass = random.shuffle(Password)
                    if PasswordToHack == GeneratedPass:
                        print("Congratulations you have hacked the ip")
                        print("You have hacked the ip by SSH port -- level 2")
                        money += 10000
                        print("ur money is now:", money)

    if e == "help":
        print("apt --installs dependencies")
        print("web --web browser")
        print("help --shows this prompt")
        print("Im still working on making this commands work")
        print("hack -- hacks someone")
        mainGame()
    if e == "apt install nmap":
        print("installing nmap... --get a better conection for better speeds")
        time.sleep(InstallTime)
        print("nmap installed")
        nmap = True
        mainGame()
    if e == "web":
        print("welcome to ur web browser")
        print("1 darkweb --missions")
        webmap = input("select option:")
        if webmap == "1":
            print("mission 1 -- install nmap using apt install nmap")
            print("mission 2 -- get a better inthernet - 1000$ type 2")
            GetBetterNet = input("select a mission>> ")
            if GetBetterNet == "2":
                if money > 1:
                    NetLevel2 = True
                else:
                    print("IMAGINE TRYING TO CHEAT CLOSING GAME L + RATIO")
                    exit()
            mainGame()
mainGame()
