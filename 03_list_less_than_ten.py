# 03 List Less Than Ten
# http://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
'''
Exercise 3
Take a list, say for example this one:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements
of the list that are less than 5.

Extras:

1. Instead of printing the elements one by one, make a
new list that has all the elements less than 5 from
this list in it and print out this new list.
2. Write this in one line of Python.
3. Ask the user for a number and return a list that contains
only elements from the original list a that are smaller
than that number given by the user.
'''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for element in a:
    if element < 5:
        print(element)

# Extra 1

b = []
for element in a:
    if element < 5:
        b.append(element)
print(b)

# Extra 2

c = [element for element in a if element < 5]
print(b)

# Extra 3

less_than = input("Please, enter a number that has to be greater than the numbers in the list a: ")
d = [element for element in a if element < less_than]
print(d)
