# Simple Calculator

def calc():
    operation = int(input('\nEnter the value of operation :- '))
    if operation == 1:
        print('Operation :- Addition')
        a = int(input('\nEnter 1st value :- '))
        b = int(input('Enter 2nd value :- '))
        print('\nAddition :- {}'.format(a + b))
    elif operation == 2:
        print('Operation :- Subtraction')
        a = int(input('\nEnter 1st value :- '))
        b = int(input('Enter 2nd value :- '))
        print('\nSubtraction :- {}'.format(a - b))
    elif operation == 3:
        print('Operation :- Multiplication')
        a = int(input('\nEnter 1st value :- '))
        b = int(input('Enter 2nd value :- '))
        print('\nMultiplication :- {}'.format(a * b))
    elif operation == 4:
        print('Operation :- Division')
        a = int(input('\nEnter 1st value :- '))
        b = int(input('Enter 2nd value :- '))
        print('\nDivision :- {}'.format(a / b))
    else:
        print('Enter proper value')
        calc()


# Creating this function to ask if user wants to use the app again ot not.
def replay():
    ask = input('\nDo you want to use again :- ')
    if ask == 'Y' or ask == 'y' or ask == 'yes' or ask == 'YES':
        calc()
        replay()
    elif ask == 'N' or ask == 'n' or ask == 'no' or ask == 'NO':
        print('\nThanks for using the calculator.')
    else:
        print('\nEnter proper value')
        replay()

# Driver Code
print('Welcome to Calculator!! ')
print('\nWhich operation do you want :- ')
print('\n1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division')

calc()
replay()