# 12 List Ends
'''
Write a program that takes a list of numbers (for example,
a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last
elements of the given list. For practice, write this code inside a function.
'''
# http://www.practicepython.org/exercise/2014/04/25/12-list-ends.html

import random


def first_and_last(list_name):
    new_list = [list_name[0], list_name[-1]]
    return new_list


def random_list():
    return [random.randint(1, 100) for i in range(random.randint(5, 15))]


a = [5, 10, 15, 20, 25]

print(a)
print(first_and_last(a))
b = random_list()
print(b)
print(first_and_last(b))

'''
Output
[5, 10, 15, 20, 25]
[5, 25]
[28, 29, 45, 94, 23, 16, 82, 93, 45, 73, 65, 72, 32, 74]
[28, 74]
'''
