# 16 Password Generator
'''
Write a password generator in Python. Be creative with how you generate
passwords - strong passwords have a mix of lowercase letters, uppercase
letters, numbers, and symbols. The passwords should be random, generating
a new password every time the user asks for a new password. Include your
run-time code in a main method.
Extra:
Ask the user how strong they want their password to be. For weak passwords,
pick a word or two from a list.
'''
# http://www.practicepython.org/exercise/2014/05/28/16-password-generator.html

import string
import random


def gen_password(n):
    list_of_symb = list(set(string.printable) - set(string.whitespace))
    password_list = [random.choice(list_of_symb) for i in range(1, n + 1)]
    password = ''.join(password_list)
    return password


print('This is a password generator \n')
user_continue = ''
while user_continue != 'exit':
    user_numb = int(input('Please enter a number of characters in password: '))
    print('Here is your password -', gen_password(user_numb))
    user_continue = input('If you want another password type ENTER, if not type EXIT. ').lower()

''' Output

This is a password generator 

Please enter a number of characters in password: 10
Here is your password - iCvO&+'B"m
If you want another password type ENTER, if not type EXIT. 
Please enter a number of characters in password: 4
Here is your password - x8bD
If you want another password type ENTER, if not type EXIT. ExiT
>>> 
'''
