from random import randint
from colored import *


while True:
    v = randint(0,10)
    num = int(input("Enter guess numer: "))
    if num == v:
        print("You win \U0001F60E   \n")

    elif num>v:
        print("Too high \U0001F616  \n")

    elif num<v:
        print("Too low \U0001F629   \n")

    print(fg('green'),"Wining number was \U0001F4A5 : ",v)

        

