from random import randint
# Imports the randint from random

# def roll_die():
#     # Enables you to create a Die, and roll to get a random number depending on the sides you pick
#     sides = input('How many sides are the die? ')
#     # Asks for sides
#     ready = input('Are you ready to roll? (y or n) ')
#     # Asks to roll
#     active = True
#     # While this is true, the WHILE loop will keep going
#     while active:
#         if ready == 'y':
#             roll = randint(1, int(sides))
#             print(roll)
#             again = input('Roll again? (y or n) ')
#             if again == 'y':
#                 # Will run the loop again if they want to roll again
#                 continue
#             else:
#                 # Stops the program if they do not want to roll again
#                 break
#         else:
#             # Closes the program if they are not ready
#             break
#
# roll_die()

# another way to write this

# print('Give me the number of sides on die, I\'ll give you a random number.')
# print('(press \'q\' to quit)')
#
# while True:
#     dice = input('\nNumber of sides on die? ')
#     if dice == 'q':
#         break
#     answer = randint(1, int(dice))
#     print(answer)

# Another version, just for random number, will not accept letters as input except to quit

print('Give me a number, and I will give a random number ranging from 1 to your number.')
print('Press \'q\' to quit.')

while True:
    num = input('\nProvide a number please: ')
    if num == 'q':
            break
    if num.isdigit():
        answer = randint(1, int(num))
        if answer == 34:
            print(str(answer) + '!! That\'s my lucky number!!')
        else:
            print(answer)
    else:
        print('Please provide a number.')