import random;
import os
from colorama import Fore
import getch


name =  """
                                        █▀█ ▄▀█ █▀ █▀ █░█░█ █▀█ █▀█ █▀▄   █▀▀ █▀▀ █▄░█ █▀▀ █▀█ ▄▀█ ▀█▀ █▀█ █▀█
                                        █▀▀ █▀█ ▄█ ▄█ ▀▄▀▄▀ █▄█ █▀▄ █▄▀   █▄█ ██▄ █░▀█ ██▄ █▀▄ █▀█ ░█░ █▄█ █▀▄ 
"""
output_string = """            
\n[1] Complex password
[2] Pin code
"""
def clear():
    os.system("clear")

def wait():
    print("\nPress Enter to continue...")
    getch.getch()
    clear()
    print(Fore.CYAN + name + Fore.RESET)

def pin_code(n):
    character = "1234567890"
    Password = ""
    for i in range(n):
        Password += random.choice(character)
    return Password
def Complex_password(n):
    character = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
    Password = ""
    for i in range(n-2):
        Password += random.choice(character)
    return Password

clear()
print(Fore.CYAN + name + Fore.RESET)
if __name__ == '__main__':

    while True:
        print(Fore.GREEN + output_string + Fore.RESET)
        user_input = input("Enter your option :" )
        
        if("1" in user_input or "complex password" in user_input):
            n = int(input("Enter Complex password length : "))
            print("\nComplex password : " + Fore.YELLOW +  Complex_password(n) + Fore.RESET)
            wait()

        elif("2" in user_input or "pin code" in user_input):
            n = int(input("Enter pin code length : "))
            print("\nPin Code : " + Fore.YELLOW +  pin_code(n) + Fore.RESET)
            wait()
        
        else:
            print("Password Generate failed!")

