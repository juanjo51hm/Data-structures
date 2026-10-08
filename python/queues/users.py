import os 
from datetime import date
def mainMenu():
    print("::: Main menu:::")
    print("[1].Register a new user")
    print("[2].list all users")
    print("[3].Search users")
    print("[4].Delete users")
    print("[5].Update users")
    print("[6].show active users")
    print("[7].show inactive users")
    print("[8].exit")
ids = []
statuses = []
created_at = []
while True:
    os.system('clear')
    mainMenu()   
    opt = input("press any option [1-8]: ")
    match opt:
        case '1':
            os.system('clear')
            print("::: register form:::")
            id = input("ident number: ")
            firstname =input("firstname: ")
            lastname= input("lastname: ")
            mobile_phone= input("mobile_phone: ")
            email= input("email: ")
            gender= input("Gender [M/F/O]: ")
            ids.append(id)
            ids.append(firstname)
            ids.append(lastname)
            ids.append(mobile_phone)
            ids.append(email)
            statuses.append(True)
            ids.append(gender)
            created_at.append(date.today())
            print("User has been created succesfolly!!")
        case '2':
            print("list all registered users: ")

