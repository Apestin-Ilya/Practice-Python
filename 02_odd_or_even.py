# 02 Odd Or Even

# http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

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
