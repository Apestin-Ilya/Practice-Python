# 10 List Overlap Comprehensions
'''
Take two lists, say for example these two:
	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only
the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes. Write
this in one line of Python using at least one list comprehension.
'''
# http://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html

import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

ab = []
ab = [j for j in b for i in a if j == i and j not in ab]

print(a)
print(b)
print(ab)

x = [random.randint(1, 10) for i in range(10)]
y = [random.randint(1, 10) for i in range(20)]
print(x)
print(y)

xy = []
xy = [j for j in y for i in x if j == i and j not in xy]
print(xy)
