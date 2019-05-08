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

print('a=', a)
print('b=', b)
print('ab=', ab)

x = [random.randint(1, 10) for i in range(10)]
y = [random.randint(1, 10) for i in range(20)]
print('x=', x)
print('y=', y)

xy = []
xy = [j for j in y for i in x if j == i and j not in xy]
print('xy=', xy)

'''
Output

a= [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
ab= [1, 1, 2, 3, 5, 8, 13]
x= [2, 6, 3, 6, 4, 6, 9, 5, 1, 5]
y= [6, 6, 8, 3, 9, 5, 1, 3, 6, 2, 3, 3, 10, 8, 4, 4, 5, 2, 3, 10]
xy [6, 6, 6, 6, 6, 6, 3, 9, 5, 5, 1, 3, 6, 6, 6, 2, 3, 3, 4, 4, 5, 5, 2, 3]
'''
