# asking for the name of the user
# choosing of a random number by the computer
# asking the user to enter the number of his choice
# player wins if the number he guessed is correct
# else if the guessed number is not correct tell the user that the value is too high or too low.
# show the number of the moves
# if the user guessed the correct number in less than given number of chances user won else user loose.

print(('WELCOME TO GUESSING NUMBER GAME.').center(100, '-'))

# user name input
name = input('Enter your name :- ')
print("\nHello " + name + ".")

# choosing of a random number by a computer using random module
import random

x = random.randint(1, 10)

# giving a counter to count how many times user has entered the value
count = 0

# choosing of a number by user by giving chances
while count < 3:
    count += 1
    num = int(input('\nEnter a number of your choice between 1 to 9 :- '))
    if num == x:
        print('\nYou guessed the correct number in {} moves.'.format(count))
        print('The answer is :- {}'.format(x))
        break
    elif num > x:
        print('Your guess is greater than the given number.')
    elif num < x:
        print('Your guess is smaller than the given number.')

while not count < 3:
    print('\nYou loose the game.')
    print('The correct answer is :- {}'.format(x))
    break