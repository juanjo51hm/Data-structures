print("hello welcome to data structure")

number1 = 10
print(f"var number1 is: {type(number1)}")
gravity = 9.8
print(f"var number1 is: {type(gravity)}")
numberx = 8j
print(f"var number1 is: {type(numberx)}")

#String data types
my_name = "juan"
fullname = "ricardo fort"
description = '''
hello, how s it going?
this is amazin !!!
'''
print(f"var my_name is: {type(my_name)}")
print(f"var fullname is: {type(fullname)}")
print(f"var description is: {type(description)}")
week_days = []
print(week_days)
print(type(week_days))#

fruits = {}
print(fruits)
print(type(fruits))#

months = ()
print(months)
print(type(months))
#lists
personal_info = [
    'juan',
    'ayala',
    50,
    True,
    '300344545',
    'pasto',
    ['juli ', 9]
 ]
print(personal_info)
print(f"father age: {personal_info[2]}")
print("father city: ", personal_info[5])
print(f"daugther name: {personal_info[6][0]}")
print(f"daugther age: {personal_info[6][1]}")
# update father age
personal_info[2] = 55
print(f"new father age: {personal_info[2]}")
#add new information
personal_info.append('malala')
# tuple
user_data = ('benazir', 'butto',35)
print(user_data)
print(user_data[0])
#dictionaries 
countries_info = {
    'country_name' : 'colombia',
    'capital' : 'Bogota',
    'abbrev' : 'CO',
    'code' : 123456
}
print(countries_info)
#print(type(personal_info)