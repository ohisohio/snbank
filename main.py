import random

file = open('staff.txt','r')
for row in file:
    field = row.split(",")
    dbusername = (field[0])
    dbpass = (field[1])
  

print("=========Welcome to SN BANK================")

print("=<< 1. Login         >>=")
print("=<< 2. Close app     >>=")

start = input('What would you like to do? 1 or 2: ')

if start == '1':
    print('PLEASE LOGIN')
    username = str(input('Enter your staff username: '))
    password = str(input('Enter your staff password: '))
    if username == dbusername and password == dbpass:
        print('Login Successful')
    else:
        print('unsuccessful')
#with open('staff.txt', 'r') as reader:
# Read & print the entire file
    #print (reader.read())


