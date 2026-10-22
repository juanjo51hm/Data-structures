import os
from datetime import date

#functions
def mainMenu():
    print (":::Main menu:::")
    print ("[1]Regsiter aa new user")
    print ("[2]List all users")
    print ("[3]Search user")
    print ("[4]Delete user")
    print ("[5]Update user")
    print ("[6]Show active uses")
    print ("[7]Show inactive users")
    print ("[8]Exit")


ids=[]    
firtsnames=[]
lastnames=[]
mobile_phones=[]
emails=[]
statuses=[]
genders=[]

ages=[]
salarys=[]

created_at=[]
#Main


while True:
    os.system('clear')
    mainMenu()
    opt=input("Press any option [1-8]: ")

    match opt:
        case '1':
            os.system('clear')
            print("::: Register form :::")


            while True:
                id=input("ident number: ")
                count = 0
                i=0
                while i< len(ids):
                    if id == ids[i]:
                        print("identification number already exists! \n try again:::")
                        count += 1
                        break
                    i+=1
                if count == 0:
                    break

            firtsname=input("Firstname: ")
            lastname=input("Lastname: ")

            while True:
                mobile_phone=input("Mobile Phone: ")
                count = 0
                i=0
                while i< len(ids):
                    if id == ids[i]:
                        print("Number Phone already exists! \n try again:::")
                        count += 1
                        break
                    i+=1
                if count == 0:
                    break


            email=input("E-mail: ")
            gender=input("Gender [M/F/O]: ")

            age=input("age: ")
            salary=input("salary: ")


            ids.append(id)
            firtsnames.append(firtsname)
            lastnames.append(lastname)
            mobile_phones.append(mobile_phone)
            emails.append(email)
            statuses.append(True)
            genders.append(gender)

            ages.append(age)
            salarys.append(salary)


            created_at.append(date.today())
            print("User has been created successfully !!")
            any_key = input ("Press any key to back to main menu")



        case '2':
            os.system('clear')
            print(":::List all registered users:::")

            print ('-'*163)
            print (f"| {'id':<15} | {'Firsname':<15} | {'Lastname':<15} | {'Mobile Phone':<15} | {'Emails':<15} | {'Genders':<15} | {'Ages':<15} | {'Salarys':<15} | {'Created':<15} |")
            print ('-'*163)

            i=0
            while i < len(ids):
                print(f'| {ids[i]:<15} | {firtsnames[i]:<15} | {lastnames[i]:<15} | {mobile_phones[i]:<15} | {emails[i]:<15} | {genders[i]:<15} |  {ages[i]:<15}| {salarys[i]:<15} | {created_at[i]}      |')
                print ('-'*163)
                i += 1

            #print(f"IDs: {ids}")
            #print(f"Firsnames: {firtsname}")
            #print(f"Lasnames: {lastname}")
            #print(f"Mobile Phones: {mobile_phone}")
            #print(f"Emails: {email}")
            #print(f"Genders: {gender}")
            #print(f"Created_at: {created_at}")

            any_key = input ("Press any key to back to main menu")



        case '8': 
            any_key=input("bye bye. press any key... ")
            break
        case _ :
            any_key=input("Invalid option. press any key to try again")