# 15 Reverse Word Order
'''
Write a program (using functions!) that asks the user for a long string
containing multiple words. Print back to the user the same string,
except with the words in backwards order. For example, say I type the string:
  My name is Michele
Then I would see the string:
  Michele is name My
shown back to me.
'''
# http://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html

def string_words_backwards():
    init_string = str(input('Please, type long string with many words: \n'))
    string_list = init_string.split()
    new_string_list = []
    for i in range(1, len(string_list) + 1):
        new_string_list.append(string_list[-i])
    new_string = ' '.join(new_string_list)
    return new_string

print(string_words_backwards())

'''
Output

Please, type long string with many words: 
Today is monday the 13 of May
May of 13 the monday is Today
'''
