# 05 List Overlap
'''
Take two lists, say for example these two:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains
only the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.
    Extras:
1. Randomly generate two lists to test this.
2. Write this in one line of Python.
'''
# http://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html

import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = []
for i in a:
    for j in b:
        if j == i and j not in c:
            c.append(j)

print('a - ', a)
print('b - ', b)
print('c - ', c)

### Extra 1

rand_list_1 = [random.randint(1,11) for i in range(random.randint(10,21))]
rand_list_2 = [random.randint(1,11) for i in range(random.randint(10,21))]

print('rand_list_1 - ', rand_list_1)
print('rand_list_2 - ', rand_list_2)

extra_1 = []
for i in rand_list_1:
    for j in rand_list_2:
        if j == i and j not in extra_1:
            extra_1.append(j)
print('extra_1 - ', extra_1)

### Extra 2

extra_2 = list(set(rand_list_1).intersection(set(rand_list_2)))
print('extra_2 - ', extra_2)

### Flashback from Excercise 14

def list_with_common_elements(list_1, list_2):
    new_list = list(set(list_1).intersection(set(list_2)))
    return new_list

print('using function, c - ', list_with_common_elements(a, b))
print('using function, extra - ', list_with_common_elements(rand_list_1, rand_list_2))

'''
Output

a -  [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b -  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c -  [1, 2, 3, 5, 8, 13]
rand_list_1 -  [3, 10, 5, 5, 3, 5, 2, 11, 3, 9, 8, 11, 4, 4, 8]
rand_list_2 -  [3, 3, 9, 1, 9, 1, 2, 6, 4, 6, 5, 7, 3, 2, 11, 8, 6, 10]
extra_1 -  [3, 10, 5, 2, 11, 9, 8, 4]
extra_2 -  [2, 3, 4, 5, 8, 9, 10, 11]
using function, c -  [1, 2, 3, 5, 8, 13]
using function, extra -  [2, 3, 4, 5, 8, 9, 10, 11]
'''
