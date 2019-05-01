# 01 Character Input
# http://www.practicepython.org/exercise/2014/01/29/01-character-input.html

name = input('Please, enter your name:')
age = input('Please, enter your age:')
to_100 = 2019 + 100 - int(age)

print('Hey, {}. You will be 100 years old in {}.'.format(name, to_100))

times = int(input('Please, enter how many times do yo want to see the text above:'))

print(times * 'Hey, {}. You will be 100 years old in {}.\n'.format(name, to_100))
