# rock paper scissor game
# importing random module
# taking input from user
# taking input from computer
# checking the possible outcomes
# declaring the winner
# 3 move game one who gets highest points wins the game
# in case of tie game will be played again

print('Rock Paper and Scissor game')

# importing a random module
import random

# declaring global variables
computer = 0
user = 0
tie = 0
cp_turn = ''
usr_input = ''


# computer input
def computer_turn():
    computer_input = random.choice(['rock', 'paper', 'scissor'])
    return computer_input


# user's input
def user_turn():
    user_input = input('\nEnter a value from rock paper and scissor :- ')
    if user_input in ['rock', 'paper', 'scissor']:
        return user_input


def enter_proper_value():
    user_input = input('Enter the proper value :- ')
    if user_input in ['rock', 'paper', 'scissor']:
        return user_input
    else:
        return enter_proper_value()


# checking the outcome
def check_outcome(cp_turn, usr_input):
    global computer, user, tie

    if cp_turn == "rock" and usr_input == "rock":
        print("Computer : " + cp_turn + '   ' + "User : " + usr_input + " = " + 'A tie.')
        tie += 1

    elif cp_turn == "rock" and usr_input == "paper":
        print("Computer : " + cp_turn + '   ' + "User : " + usr_input + " = " + 'User wins')
        user += 1

    elif cp_turn == "rock" and usr_input == "scissor":
        print("Computer : " + cp_turn + '   ' + "User : " + usr_input + " = " + 'Computer wins')
        computer += 1

    elif cp_turn == "paper" and usr_input == "rock":
        print("Computer : " + cp_turn + '   ' + " User : " + usr_input + " = " + 'Computer wins')
        computer += 1

    elif cp_turn == "paper" and usr_input == "paper":
        print("Computer : " + cp_turn + '   ' + "User : " + usr_input + " = " + 'A tie.')
        tie += 1

    elif cp_turn == "paper" and usr_input == "scissor":
        print("Computer : " + cp_turn + '   ' + "User : " + usr_input + " = " + 'User wins')
        user += 1

    elif cp_turn == "scissor" and usr_input == "rock":
        print("Computer : " + cp_turn + '   ' + "User : " + usr_input + " = " + 'User wins')
        user += 1

    elif cp_turn == "scissor" and usr_input == "paper":
        print("Computer : " + cp_turn + '   ' + " User : " + usr_input + " = " + 'Computer wins')
        computer += 1

    elif cp_turn == "scissor" and usr_input == "scissor":
        print("Computer : " + cp_turn + '   ' + "User : " + usr_input + " = " + 'A tie.')
        tie += 1


# final winner
def final_winner():
    print()
    print('\nWINNER :- ')

    # final winner
    if user > computer:
        print('\nCOMPUTER :- {}    USER :- {}    TIE :- {}'.format(computer, user, tie))
        print('\nUSER wins with {} points.'.format(user))

    elif computer > user:
        print('\nCOMPUTER :- {}    USER :- {}    TIE :- {}'.format(computer, user, tie))
        print('\nCOMPUTER wins with {} points.'.format(computer))

    elif computer == user:
        print('\nCOMPUTER :- {}    USER :- {}    TIE :- {}'.format(computer, user, tie))
        print("\nTIE.")


# starting the game
def play_the_game():
    global computer, user

    for i in range(0, 3):
        global cp_turn, usr_input

        # computer's Turn
        cp_turn = computer_turn()

        # user's turn
        usr_input = user_turn()

        if usr_input in ['rock', 'paper', 'scissor']:
            # checking the outcome
            check_outcome(cp_turn, usr_input)
        else:
            x = enter_proper_value()
            check_outcome(cp_turn, x)
    # checking the final winner
    final_winner()


play_the_game()