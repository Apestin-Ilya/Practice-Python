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
print('c - ', c)

### Extra 1

a = [random.randint(1,11) for i in range(random.randint(10,21))]
b = [random.randint(1,11) for i in range(random.randint(10,21))]

print('a - ', a)
print('b - ', b)

extra_1 = []
for i in a:
    for j in b:
        if j == i and j not in extra_1:
            extra_1.append(j)
print('extra_1 - ', extra_1)

### Extra 2

#extra_2 = []
#extra_2 = [j for i in a for j in b if j == i and j not in extra_2]
#print('extra_2 - ', extra_2)
