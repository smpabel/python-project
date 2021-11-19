from random import randint
from colored import *

count = 0
randNum = randint(0,10)
num = int(input("Enter guess numer: "))

while True:
    
    if num == randNum:
        count+=1
        print(fg('green'),f"Congress! You win by trying {count} times \U0001F60E   \n")
        break
    else:
        if num>randNum:
            print("Too high \U0001F616  \n")
        else:
            print("Too low \U0001F629   \n")

        num = int(input("Enter again: "))
        count+=1
print("Wining numbe was: ",randNum)
