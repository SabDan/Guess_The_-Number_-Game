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
