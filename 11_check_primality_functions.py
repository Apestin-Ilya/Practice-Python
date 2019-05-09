# 11 Check Primality Functions
'''
Ask the user for a number and determine whether the number is prime or not.
For those who have forgotten, a prime number is a number that has no divisors.)
You can (and should!) use your answer to Exercise 4 to help you. Take this
opportunity to practice using functions, described below.
'''
# http://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html


def get_integer(text='Type some integer number and you will see is it prime or not: '):
    return int(input(text))


def is_prime(num):
    j = 0
    for i in range(1, num + 1):
        if num % i == 0:
            j += 1
    if j == 2 :
        print('{} is a prime number.'.format(num))
    else:
        print('{} is not a prime number.'.format(num))

do = ''
while do != 'exit':
    is_prime(get_integer())
    do = input('Type exit to quit or ENTER to continue.\n').lower()

'''
Output
Type some integer number and you will see is it prime or not: 1
1 is a prime number.
Type exit to quit or ENTER to continue.

Type some integer number and you will see is it prime or not: 2
2 is a prime number.
Type exit to quit or ENTER to continue.

Type some integer number and you will see is it prime or not: 3
3 is a prime number.
Type exit to quit or ENTER to continue.

Type some integer number and you will see is it prime or not: 4
4 is not a prime number.
Type exit to quit or ENTER to continue.

Type some integer number and you will see is it prime or not: 5
5 is a prime number.
Type exit to quit or ENTER to continue.

Type some integer number and you will see is it prime or not: 6
6 is not a prime number.
Type exit to quit or ENTER to continue.
exit
>>> 
'''
