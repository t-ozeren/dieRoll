import random
import math
import os

def clrscreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def rndm(num):
    rndm_num=random.randint(1,num)
    print(rndm_num)

def control(key_input):
    if key_input.isnumeric() == True:
        return int(key_input)
    else:
        control(input("pls use only digits:"))

def menu():
    while True:
        clrscreen()
        key=control(input("""
    1-Roll a dice
    0-Quit
    Choice: """))
        if key is 1:
            clrscreen()
            key_num=control(input("\nHow many side you want ? "))
            print("Your result:",end=' ')
            rndm(int(key_num))
            input()
        elif key is 0:
            clrscreen()
            break
        else:
            input("Pls choose correctly.")

menu()
