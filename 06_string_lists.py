# 06 String Lists
'''
Ask the user for a string and print out whether this string is a palindrome
or not. (A palindrome is a string that reads the same forwards and backwards.)
'''
# http://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

string = input("Please, enter some string: ")

for i in range(0, len(string)):
    if string[0+i] != string[-1-i]:
        print('not palindrome')
        break
else:
    print('palindrome')
