#Converter Python & Javascript to Exe
#Coded by Lamp, (C) NumeXx

#import module
import os
import time

#Let's goooo
tolol = """
[#]===================================[#]
[+] Converter Coded by Lamp
[+] Credit : NumeXx
[#]===================================[#]
[+] 1. Install Package JS to Exe
[+] 2. Install Package PY to Exe
[+] 3. Convert JS to Exe
[+] 4. Convert PY to Exe
[+] 5. Close Program
[!] Must Install Node.js or Python!
[#]===================================[#]
"""

print(tolol)
choice = input("[#] Enter Your Choice : ")
if choice == "1":
    print("Installing Package...")
    time.sleep(1)
    print("Please Wait..")
    os.system('npm install -g pkg')
    print("Successfuly Install Package")
    input("=*= Press 'Enter' to Continue: ")
    os.system('cls')
    os.system('python Converter.py')

elif choice == "2":
    print("Installing Package...")
    time.sleep(1)
    print("Please Wait..")
    os.system('pip install pyinstaller')
    print("Successfuly Install Package")
    input("=*= Press 'Enter' to Continue: ")
    os.system('cls')
    os.system('python Converter.py')

elif choice == "3":
    print("[!] Example : main.js")
    conv = input("[#] Enter Your JS File Name : ")
    print("Converting File..")
    time.sleep(1)
    os.system(f"pkg {conv}")
    print("Successfuly Converting JS to Exe!")
    input("=*= Press 'Enter' to Continue: ")
    os.system('cls')
    os.system('python Converter.py')

elif choice == "4":
    print("[!] Example : main.py")
    conv2 = input("[#] Enter Your PY File Name : ")
    print("Converting File..")
    time.sleep(1)
    os.system(f"pyinstaller {conv2} --onefile")
    print("Successfuly Converting PY to Exe!")
    input("=*= Press 'Enter' to Continue: ")
    os.system('cls')
    os.system('python Converter.py')


elif choice == "5":
    exit()

else :
    os.system('cls')
    print("You Misstyped! Please Try Again.")
    time.sleep(1)
    os.system('python Converter.py')
    exit()
