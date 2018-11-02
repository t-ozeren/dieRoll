import random
import math
import os

def clrscreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def rndm(num):
    rndm_num=random.randint(1,num)

    print(rndm_num)
def menu():
    while True:
        clrscreen()
        key=input("""
    1-Roll a dice
    0-Quit
    Choice: """)
        if key is '1':
            clrscreen()
            key_num=input("\nHow many side you want ? ")
            print("Your result:",end=' ')
            rndm(int(key_num))
            input()
        elif key is '0':
            clrscreen()
            break
        else:
            input("Pls choose correctly.")

menu()
