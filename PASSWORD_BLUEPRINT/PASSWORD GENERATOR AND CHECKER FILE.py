import random
import string
from colorama import Fore, Style
def passwordstrength():
    M=[]
    print("_"*100)
    print("PASSWORD STRENGTH CHECKER")
    print("_"*100)
    global X
    global Z
    while True:
        print("_"*100)
        A=input("Enter the password=")
        print("IS YOUR PASSWORD CORRECT=", A)
        ch=input("Enter YES OR NO (Y/N)=")
        print("_"*100)
        if ch in "Yy":
            break
    lowercas=uppercas=splchar=num=wsp=0
    for i in A:
        if i in string.ascii_lowercase:
            lowercas=lowercas+1
        elif i in string.ascii_uppercase:
            uppercas=uppercas+1
        elif i in string.digits:
            num=num+1
        elif i in " ":
            wsp=wsp+1
        else:
            splchar=splchar+1
    L=[lowercas,uppercas,num,wsp,splchar]
    for i in L:
        if i!=0:
            M.append(i)
    strength=len(M)
    if strength==1:
        Z="THE PASSWORD IS VERY WEAK"
        X="PASSWORD STRENGTH="+Fore.RED+"||"
    elif strength ==2:
        Z="The PASSWORD IS WEAK"
        X="PASSWORD STRENGTH="+Fore.LIGHTRED_EX+"||||"
    elif strength ==3:
        Z="THE PASSWORD IS MODERATE"
        X="PASSWORD STRENGTH="+Fore.BLUE+"||||||"
    elif strength ==4:
        Z="THE PASSWORD IS GOOD"
        X="PASSWORD STRENGTH="+Fore.LIGHTGREEN_EX+"||||||||"
    elif strength == 5:
        Z="THE PASSWORD IS POWERFUL"
        X="PASSWORD STRENGTH="+Fore.GREEN+" ||||||||||"
    print("_"*100)
    print("\t\t\tPASSWORD REPORT")
    print("_" * 100)
    print("YOUR PASSWORD IS", A)
    print("It has ", lowercas, "LOWERCASE letter")
    print("It has ", uppercas,  "UPPERCASE letter")
    print("It has ", wsp, "BLANK SPACE ")
    print("It has ", num, "Numbers")
    print("It has ", splchar, "SPECIAL CHARACTER ")
    print(Z)
    print(X)
    print(Style.RESET_ALL)
    print("_"*100)
def passwordgenerator():
    print("-"*100)
    print("\t\t\t\tPASSWORD GENERATOR")
    A=int(input("Enter the length ="))
    i=0
    K=" "
    B="abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    C=len(B)
    while i!=A:
        s=random.randrange(0,C)
        K=K+B[s]
        i=i+1
    return K
def Menu():
    while True:
        print("_"*100)
        print("MAIN MENU")
        print("press 1 for PASSWORD GENERATOR")
        print("press 2 for PASSWORD STRENGTH REPORT")
        print("press 3 to EXIT")
        ch=int(input("Enter the choice= "))
        if ch ==1:
            print("Your password is", passwordgenerator())
        elif ch==2:
            passwordstrength()
        elif ch==3:
            print("-"*100)
            print("THANKS FOR USING")
            break
        else:
            print("Invalid choice")
Menu()