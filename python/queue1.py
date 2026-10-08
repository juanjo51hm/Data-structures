from random import randint
import os

numbers = []
status = True

while status:
    num = randint(1,100)
    numbers.append(num)
    print(f"Display list: {numbers}")
    print(f"total rows:{len(numbers)}")
    key = input("do you want to insert other number?[y/Y/n/N]")
    if key == 'n' or key == 'n':
        break
                  
