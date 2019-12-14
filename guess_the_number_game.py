"""
import random

print('----------------------------------------------')
print('               Guess The Number')
print('----------------------------------------------')
print()


#computer random number
computer_guess = random.randint(0, 100) #range beginning at 0 to 100

user_enters_number = -1



#checks to see if the str turned into an int
#print(user_guess, type(user_guess))
#print(user_enters_number, type(user_enters_number))
while user_enters_number != computer_guess:
    # these two variables were originally declared outside of the loop
    # user will enter a guess
    user_guess = input('Guess a number between 0 and 100 : ')
    # converts user_guess str to an int
    user_enters_number = int(user_guess)

    if user_enters_number < computer_guess:
        print('Too low')
    elif user_enters_number > computer_guess:
        print('Too high')
    else:
        print('You Win!')

print('Done')
"""





import random


print('---------------------------------------------------')
print('               Guess The Number ')
print('---------------------------------------------------')
print()


computer_game = random.randint(0, 100) #computer will pick from 0 - 100

user_guess = -1

name = input('Hey, what is your name? ')

while user_guess != computer_game:
    # we need to ask the user for their input for the loop to work
    user_turn = input('Guess A Number from 0 - 100 ')
    user_guess = int(user_turn)
    if user_guess < computer_game:
        print('Sorry {}, your guess of {} was too LOW'.format(name, user_guess))
    elif user_guess > computer_game:
        print('Sorry {}, your guess of {} was too HIGH'.format(name, user_guess))
    else:
        print('Congratulations {}, your guess of {} was the CORRECT answer!'.format(name, user_guess))
