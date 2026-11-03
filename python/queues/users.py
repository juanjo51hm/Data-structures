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
                print("::: List All Users Submenu :::")
                print("[1] Sort in ascending order by identification")
                print("[2] Sort in descending order by identification")
                print("[3] Sort in ascending order by lastname")
                print("[4] Sort in descending order by lastname")
                print("[5] Exit to main menu")
                
                sort_opt = input("Select an option [1-5]: ")
                
                if sort_opt == '5':
                    break
                
                if sort_opt in ['1', '2', '3', '4']:
                    # Incluye todos los índices registrados (tanto activos como inactivos)
                    indices = list(range(len(ids)))
                    
                    if sort_opt == '1':
                        indices.sort(key=lambda i: ids[i])
                    elif sort_opt == '2':
                        indices.sort(key=lambda i: ids[i], reverse=True)
                    elif sort_opt == '3':
                        indices.sort(key=lambda i: lastnames[i].lower())
                    elif sort_opt == '4':
                        indices.sort(key=lambda i: lastnames[i].lower(), reverse=True)

                    os.system('clear')
                    print("::: List all registered users :::")
                    print ('-'*182)
                    print (f"| {'id':<15} | {'Firsname':<15} | {'Lastname':<15} | {'Mobile Phone':<15} | {'Email':<15} | {'Status':<12} | {'Gender':<8} | {'Age':<8} | {'Salary':<12} | {'Created':<12} |")
                    print ('-'*182)

                    for i in indices:
                        status_str = "Active" if statuses[i] else "Inactive"
                        print(f'| {ids[i]:<15} | {firtsnames[i]:<15} | {lastnames[i]:<15} | {mobile_phones[i]:<15} | {emails[i]:<15} | {status_str:<12} | {genders[i]:<8} | {str(ages[i]):<8} | {str(salarys[i]):<12} | {str(created_at[i]):<12} |')
                        print ('-'*182)
                    
                    any_key = input("\nPress any key to continue...")
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
                if id_user == ids[i]:
                    j += 1
                    break
                i += 1
            
            if j > 0:
                os.system('clear')
                print("::: User found :::")
                print (f"ident.user: {ids[i]}")
                print (f"fullname: {firtsnames[i]} {lastnames[i]}")
                print (f"mobile phone: {mobile_phones[i]}")
                print (f"email: {emails[i]}")
                print (f"status: {'Active' if statuses[i] else 'Inactive'}")
                print (f"gender: {genders[i]}")
                print (f"age: {ages[i]}")
                print (f"salary: {salarys[i]}")
            else:
                print("identification number not found.")
            
            any_key = input("\nPress any key to back to main menu")

        case '5':
            os.system('clear')
            print("::: Update User :::")
            id_user = input("Enter identification number to update: ")
            user_index = 0
            while user_index < len(ids) and ids[user_index] != id_user:
                user_index += 1
            if user_index == len(ids):
                print("identification number not found.")
                input("\nPress any key to back to main menu")
                continue

            while True:
                os.system('clear')
                current_status = "Active" if statuses[user_index] else "Inactive"
                print(f"::: Update User: {ids[user_index]} :::")
                print(f"[1] Update firstname (current: {firtsnames[user_index]})")
                print(f"[2] Update lastname (current: {lastnames[user_index]})")
                print(f"[3] Update mobile phone (current: {mobile_phones[user_index]})")
                print(f"[4] Update email (current: {emails[user_index]})")
                print(f"[5] Update status (current: {current_status})")
                print(f"[6] Update age (current: {ages[user_index]})")
                print(f"[7] Update salary (current: {salarys[user_index]})")
                print("[8] Update all fields")
                print("[9] Exit to main menu")

                update_opt = input("Select an option [1-9]: ")

                if update_opt == '9':
                    break

                elif update_opt == '1':
                    firtsnames[user_index] = input(
                        f"Firstname (current: {firtsnames[user_index]}): "
                    )

                elif update_opt == '2':
                    lastnames[user_index] = input(
                        f"Lastname (current: {lastnames[user_index]}): "
                    )

                elif update_opt in ['3', '4']:
                    is_phone = update_opt == '3'
                    values = mobile_phones if is_phone else emails
                    field_name = "Mobile Phone" if is_phone else "E-mail"
                    current_val = values[user_index]

                    while True:
                        new_val = input(f"{field_name} (current: {current_val}): ")
                        if is_phone and not new_val.isdigit():
                            print("Invalid input! Mobile phone must contain numbers only.")
                            continue

                       
                        duplicate = False
                        for idx, val in enumerate(values):
                            if idx != user_index and statuses[idx] and val == new_val:
                                duplicate = True
                                break
                        
                        if duplicate:
                            print(f"{field_name} already exists in an active user! Try again.")
                        else:
                            values[user_index] = new_val
                            break

                elif update_opt == '5':
                    while True:
                        st_input = input(f"Status (current: {current_status}) [A]ctive/[I]nactive: ").strip().lower()
                        if st_input in ['a', 'active']:
                            statuses[user_index] = True
                            break
                        elif st_input in ['i', 'inactive']:
                            statuses[user_index] = False
                            break
                        print("Invalid status. Please enter A (Active) or I (Inactive).")

                elif update_opt == '6':
                    while True:
                        age_in = input(f"Age (current: {ages[user_index]}): ")
                        if age_in.isdigit():
                            ages[user_index] = int(age_in)
                            break
                        print("Invalid input! Age must be a number.")

                elif update_opt == '7':
                    while True:
                        sal_in = input(f"Salary (current: {salarys[user_index]}): ")
                        if sal_in.isdigit():
                            salarys[user_index] = int(sal_in)
                            break
                        print("Invalid input! Salary must be numeric.")

                elif update_opt == '8':
                    firtsnames[user_index] = input(f"Firstname (current: {firtsnames[user_index]}): ")
                    lastnames[user_index] = input(f"Lastname (current: {lastnames[user_index]}): ")

                    
                    while True:
                        new_phone = input(f"Mobile Phone (current: {mobile_phones[user_index]}): ")
                        if not new_phone.isdigit():
                            print("Invalid input! Mobile phone must contain numbers only.")
                            continue
                        if any(idx != user_index and statuses[idx] and val == new_phone for idx, val in enumerate(mobile_phones)):
                            print("Mobile phone already exists in an active user! Try again.")
                        else:
                            mobile_phones[user_index] = new_phone
                            break

                    
                    while True:
                        new_email = input(f"E-mail (current: {emails[user_index]}): ")
                        if any(idx != user_index and statuses[idx] and val == new_email for idx, val in enumerate(emails)):
                            print("E-mail already exists in an active user! Try again.")
                        else:
                            emails[user_index] = new_email
                            break

                    
                    while True:
                        st_input = input(f"Status (current: {current_status}) [A]ctive/[I]nactive: ").strip().lower()
                        if st_input in ['a', 'active']:
                            statuses[user_index] = True
                            break
                        elif st_input in ['i', 'inactive']:
                            statuses[user_index] = False
                            break
                        print("Invalid status. Enter A or I.")

                    
                    while True:
                        age_in = input(f"Age (current: {ages[user_index]}): ")
                        if age_in.isdigit():
                            ages[user_index] = int(age_in)
                            break
                        print("Invalid input! Age must be a number.")

                    
                    while True:
                        sal_in = input(f"Salary (current: {salarys[user_index]}): ")
                        if sal_in.isdigit():
                            salarys[user_index] = int(sal_in)
                            break
                        print("Invalid input! Salary must be numeric.")

                else:
                    input("Invalid option. Press any key to try again...")
                    continue

                print("User has been updated successfully!")
                input("Press any key to continue...")

        case '8': 
            any_key = input("bye bye. press any key... ")
            break
        case _:
            any_key = input("Invalid option. press any key to try again")