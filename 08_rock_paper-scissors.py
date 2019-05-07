# 08 Rock Paper Scissors
'''
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays
(using input), compare them, print out a message of congratulations to
the winner, and ask if the players want to start a new game)
Remember the rules: Rock beats scissors. Scissors beats paper. Paper beats rock.
'''
# http://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

print('It is a two-player Rock-Paper-Scissors game.\n\
Players print their option such as rock, scissors or paper.\n\
The programm will show who is the winner.')

choice = 'yes'
while choice == 'yes':
    hand_1 = input('First Player turn: ').lower()
    hand_2 = input('Second Player turn: ').lower()
    if hand_1 and hand_2 in ['rock', 'scissors', 'paper']:
        if hand_1 != hand_2:
            if hand_1 == 'rock':
                if hand_2 == 'scissors':
                    print('Rock beats scissors. Player 1 wins!')
                else:
                    print('Paper beats rock. Player 2 wins!')
            elif hand_1 == 'scissors':
                if hand_2 == 'paper':
                    print('Scissors beats paper. Player 1 wins!')
                else:
                    print('Rock beats scissors. Player 2 wins!')
            elif hand_1 == 'paper':
                if hand_2 == 'rock':
                    print('Paper beats rock. Player 1 wins!')
                else:
                    print('Scissors beats paper. Player 2 wins!')
        else:
            print('Players have same hands')
    else:
        print('Inapropriate hands')
    choice = input('Want to start a new game?\n').lower()
