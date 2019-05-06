# 07 List Comprehensions
'''
A list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
Write one line of Python that takes this list a and makes a new list
that has only the even elements of this list in it.
'''
# http://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even_a = [item for item in a if item % 2 == 0]
print(even_a)
