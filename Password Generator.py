# importing a random module for choosing characters in python
import random

# creating a sequence of characters
seq = "ABCDEFGHIJKLMNOPQRSTUVWXY!@#$%^&*0123456789abcdefghijklmnopqrstivwxyz"


def password_generator():
    # entering the length of password
    num = int(input('\nEnter the length of the password :- '))

    if num >= 8:
        password = ''

        # using for loop for generating of characters
        for i in range(0, num):
            password += random.choice(seq)
        print("\nPassword is :- " + password)

    else:
        print('\nMinimum password of length 8 required.')
        print('Enter your password again :- ')
        password_generator()


password_generator()