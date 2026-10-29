import os
from datetime import date

def mainMenu():
    print (":::Main menu:::")
    print ("[1]Register a new user")
    print ("[2]List all users")
    print ("[3]Search user")
    print ("[4]Delete user")
    print ("[5]Update user")
    print ("[6]Show active users")
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

while True:
    os.system('clear')
    mainMenu()
    opt=input("Press any option [1-8]: ")

    match opt:
        case '1':
            os.system('clear')
            print("::: Register form :::")

            while True:
                id = input("ident number: ")
                if not id.isdigit():
                    print("Invalid input! Identification must contain numbers only. \n try again:::")
                    continue
                
                count = 0
                i = 0
                while i < len(ids):
                    if id == ids[i]:
                        print("identification number already exists! \n try again:::")
                        count += 1
                        break
                    i += 1
                if count == 0:
                    break

            firtsname = input("Firstname: ")
            lastname = input("Lastname: ")

            while True:
                mobile_phone = input("Mobile Phone: ")
                if not mobile_phone.isdigit():
                    print("Invalid input! Mobile phone must contain numbers only. \n try again:::")
                    continue

                count = 0
                i = 0
                while i < len(mobile_phones):
                    if statuses[i] and mobile_phone == mobile_phones[i]:
                        print("Number Phone already exists in an active user! \n try again:::")
                        count += 1
                        break
                    i += 1
                if count == 0:
                    break

            while True:
                email = input("E-mail: ")
                count = 0
                i = 0
                while i < len(emails):
                    if statuses[i] and email == emails[i]:
                        print("Email already exists in an active user! \n try again:::")
                        count += 1
                        break
                    i += 1
                if count == 0:
                    break

            while True:
                gender = input("Gender [M/F/O]: ").upper()
                if gender in ['M', 'F', 'O']:
                    break
                print("Invalid gender! Please enter M, F, or O.")

            while True:
                age_input = input("age: ")
                if age_input.isdigit():
                    age = int(age_input)
                    break
                print("Invalid input! Please enter a valid number for age.")

            while True:
                salary_input = input("salary: ")
                if salary_input.isdigit():
                    salary = int(salary_input)
                    break
                print("Invalid input! Please enter a valid numeric salary.")

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
            any_key = input("Press any key to back to main menu")

        case '2':
            while True:
                os.system('clear')
                print("::: List Active Users Submenu :::")
                print("[1] Sort in ascending order by identification")
                print("[2] Sort in descending order by identification")
                print("[3] Sort in ascending order by lastname")
                print("[4] Sort in descending order by lastname")
                print("[5] Exit to main menu")
                
                sort_opt = input("Select an option [1-5]: ")
                
                if sort_opt == '5':
                    break
                
                if sort_opt in ['1', '2', '3', '4']:
                    indices = []
                    i = 0
                    while i < len(ids):
                        if statuses[i] == True:
                            indices.append(i)
                        i += 1
                    
                    if sort_opt == '1':
                        indices.sort(key=lambda i: ids[i])
                    elif sort_opt == '2':
                        indices.sort(key=lambda i: ids[i], reverse=True)
                    elif sort_opt == '3':
                        indices.sort(key=lambda i: lastnames[i].lower())
                    elif sort_opt == '4':
                        indices.sort(key=lambda i: lastnames[i].lower(), reverse=True)

                    os.system('clear')
                    print(":::List all active registered users:::")
                    print ('-'*163)
                    print (f"| {'id':<15} | {'Firsname':<15} | {'Lastname':<15} | {'Mobile Phone':<15} | {'Email':<15} | {'Gender':<15} | {'Age':<15} | {'Salary':<15} | {'Created':<15} |")
                    print ('-'*163)

                    for i in indices:
                        print(f'| {ids[i]:<15} | {firtsnames[i]:<15} | {lastnames[i]:<15} | {mobile_phones[i]:<15} | {emails[i]:<15} | {genders[i]:<15} | {str(ages[i]):<15} | {str(salarys[i]):<15} | {str(created_at[i]):<15} |')
                        print ('-'*163)
                    
                    any_key = input("Press any key to continue...")
                else:
                    any_key = input("Invalid option. Press any key to try again...")

        case '3':
            os.system('clear')
            print("::: Search User :::")
            id_user = input("Enter identification number to search: ")
            
            found = False
            indices = []
            i = 0
            j = 0
            while i < len(ids):
                if id_user== ids[i]:
                    j+= 1
                    break
                i += 1
            
            if j>0:
                os.system('clear')
                print("::: User found :::")
                print (f"ident.user: {ids[i]}")
                print (f"fullname: {firtsnames[i]} {lastnames[i]}")
                print (f"mobile phone: {mobile_phones[i]}")
                print (f"email: {emails[i]}")
                print (f"mobile gender: {genders[i]}")
                print (f" age: {ages[i]}")
                print (f"salary: {salarys[i]}")
            else:
                print("identification number not found.")
            
            any_key = input("\nPress any key to back to main menu")

        
        case '8': 
            any_key = input("bye bye. press any key... ")
            break
        case _:
            any_key = input("Invalid option. press any key to try again")