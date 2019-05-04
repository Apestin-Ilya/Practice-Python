# 01 Character Input
# http://www.practicepython.org/exercise/2014/01/29/01-character-input.html
'''
Create a program that asks the user to enter their name and their age. Print
out a message addressed to them that tells them the year that they will turn 100 years old.
Extras:
1. Add on to the previous program by asking the user for another number and printing out
that many copies of the previous message. (Hint: order of operations exists in Python)
2. Print out that many copies of the previous message on separate lines. (Hint: the
string "\n is the same as pressing the ENTER button)
'''

name = input('Please, enter your name:')
age = input('Please, enter your age:')
to_100 = 2019 + 100 - int(age)

print('Hey, {}. You will be 100 years old in {}.'.format(name, to_100))

times = int(input('Please, enter how many times do yo want to see the text above:'))

print(times * 'Hey, {}. You will be 100 years old in {}.\n'.format(name, to_100))
