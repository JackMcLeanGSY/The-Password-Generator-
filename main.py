print("Welcome to The Password Generator by")
print(" The Password Generator by Version 1.0 ")
print("***************************************************")

print("welcome to password Generator")
print("*****************************")

import random

print('''
Password Generator
==================
''')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

number = input('number of passwords?')
number = int(number)

print('How long should the password be? Please tell me in numbers')

print("*****************************")
length = input('password length?')
length = int(length)

print('\nhere are your passwords:')

for pwd in range(number):
  password = ''
  for c in range(length):
    password += random.choice(chars)
  print(password)
  password =input
password = input("enter your password : ")
password =input
print("Password correct ")

print("Thankyou for using The Password Generator Version 1.0 ")


