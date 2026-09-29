from random import randint
import os

def rollDice():
    die1 = randint(1,6)
    die2 = randint(1,6)
    return die1, die2
    
os.system('clear')
dice = rollDice()
print(f"dice: {dice}")

if dice[0] == 6 and dice[1] == 6:
    print("you win!!") 
    
else:
        print("try again!")