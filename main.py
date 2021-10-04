#Coded by Lamp (C) Numex
import os, sys

s = """
[+]===================================[+]
[+] Coded by Lamp#1442                [+]
[+] Credit to Numex                   [+]
[+]===================================[+]
[+] 1. Install Package Python to Exe
[+] 2. Install Package JS to Exe
[+] 3. Convert Python to Exe
[+] 4. Convert Javascript to Exe
[+] 5. Exit
[+]===================================[+] """

def pkgpy():
    print("Installing.. Please wait")
    os.system("pip install pyinstaller")
    print("Successfuly install Python Package!")
    input("Press 'Enter' to Back :")
    os.system('cls')
    main()

def pkgjs():
    print("Installing.. Please wait")
    os.system("npm i -g pkg")
    print("Successfuly install Javascript Package!")
    input("Press 'Enter' to Back :")
    os.system('cls')
    main()

def convpy():
    print("Example = main.py")
    cpy = input("Enter Python file name : ")
    if cpy == "":
        print("Please enter the file name!")
        convpy()
    else :
        os.system(f"pyinstaller {cpy} --onefile")
        print("Successfuly Convert python to exe")
        input("Press 'Enter' to Back :")
        os.system('cls')
        main()

def convjs():
    print("Example = index.js")
    cjs = input("Enter Js file name : ")
    if cjs == "":
        print("Please enter the file name!")
    else:
        os.system(f"pkg {cjs}")
        print("Successfuly Convert javascript to exe")
        input("Press 'Enter' to Back :")
        os.system('cls')
        main()

def main():
    print(s,"\n")
    m = input("[?] Enter Your Choice : ")
    if m == "1":
        pkgpy()
    elif m == "2":
        pkgjs()
    elif m == "3":
        convjs()
    elif m == "4":
        convpy()
    elif m == "5":
        sys.exit()

main()
