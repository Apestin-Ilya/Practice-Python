# 09 Guessing Game One
'''
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they
guessed too low, too high, or exactly right.
Extras:
1. Keep the game going until the user types “exit”
2. Keep track of how many guesses the user has taken, and when the
game ends, print this out.
'''
# http://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html

import random

i = 0
guess = ''
print('It is Guessing Game. The computer will generate a random number\n\
between 1 and 9. Type your number in the field or "exit" to quit.')

while guess != 'exit':
    numb = random.randint(1, 9)
    guess = input('Please, enter your guess: ')
    guess = int(guess)
    if guess > numb:
        print('Your guess is too high.')
    elif guess < numb:
        print('Your guess is too low.')
    else:
        i += 1
        print('You guessed! It is {}. You guessed {} times.'.format(numb, i))
    guess = input('Type "exit" if you wan to quit.')
