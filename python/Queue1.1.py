from random import randint
import os

numbers = []
status = True

while status:
    num = randint(1, 100)
    
    if num in numbers:
        print(f"El número {num} ya se encuentra registrado.")
    else:
        numbers.append(num)
        print(f"Display list: {numbers}")
        print(f"Total rows: {len(numbers)}")
    
    while True:
        key = input("quieres registrar otro numero? [y/Y/n/N] ")
        
        if key in ['y', 'Y']:
            break
        elif key in ['n', 'N']:
            status = False
            break
        else:  
            print("Error: Opción no válida. Ingrese y, Y, n o N.")