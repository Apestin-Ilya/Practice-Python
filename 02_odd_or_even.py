# 02 Odd Or Even
# http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
'''
Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user. Hint: how does an even / odd
number react differently when divided by 2?
Extras:
1. If the number is a multiple of 4, print out a different message.
2. Ask the user for two numbers: one number to check (call it num) and one
number to divide by (check). If check divides evenly into num, tell that to
the user. If not, print a different appropriate message.
'''

num = int(input('Please, enter some number: '))

if num % 4 == 0 :     # Extra task 2
  print('The number you entered multiple of four')
elif num % 2 == 0 :
  print('The number you entered is odd')
else :
  print('The number you entered is even')

# Extra task 2
num = int(input('Please, enter some number: '))
check = int(input('Please, enter a number to divide by: '))

if num % check == 0 :
  print('{} is multiple of {}'.format(num, check))
else :
  print('{} is not multiple of {}'.format(num, check))
