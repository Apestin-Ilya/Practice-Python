# 14 List Remove Duplicates
'''
Write a program (function!) that takes a list and returns a new list that
contains all the elements of the first list minus all the duplicates.
Extras:
1. Write two different functions to do this - one using a loop and constructing
a list, and another using sets.
2. Go back and do Exercise 5 using sets, and write the solution for that in a
different function.
'''
# http://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html

import random


def list_remove_dupl_using_loop(some_list):
    new_list = []
    for i in some_list:
        if i not in new_list:
            new_list.append(i)
    return new_list


def list_remove_dupl_using_set(some_list):
    new_list = list(set(some_list))
    return new_list


def random_list():
    return [random.randint(1, 10) for i in range(random.randint(10, 15))]


first_list = random_list()
print('Initial list ', first_list)
print('List without duplicates using loop ', list_remove_dupl_using_loop(first_list))
print('List without duplicates using set ', list_remove_dupl_using_set(first_list))

'''
Output

Initial list  [3, 3, 7, 4, 10, 9, 4, 7, 2, 7, 3, 10, 1]
List without duplicates using loop  [3, 7, 4, 10, 9, 2, 1]
List without duplicates using set  [1, 2, 3, 4, 7, 9, 10]
'''
