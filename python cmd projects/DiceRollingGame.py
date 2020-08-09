import random

#giving user a menu
print('Menu')
print('1. Roll the dice')
print('2. End game')

# defining a token for the loop
token = 1

#main loop
while token > 0:

    #taking input
    user_input = input('What to do? :  ')

    #main operations
    if user_input == '1':
        print(random.randint(1,6))
        print("")
    elif user_input == '2':
        print('GoodBye!')
        break
    else:
        print('Wrong input! Enter again')
