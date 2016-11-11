# Current_users list with four various names
current_users = ['mary', 'joe', 'steve', 'sarah']

# This converts the list above to lowercase, so even if the input is capital, it will still not be accepted.
[item.lower() for item in current_users]

# Commented out to compare to new statement below
# new = input('Type in a user name: ')
#
# while len(current_users) < 10:
#     if new.lower() not in current_users:
#         print('Contratulations ' + new.title() + ', that user name is available!')
#         current_users.append(new)
#     else:
#         print('I\'m sorry, the user name of ' + new.title() + ' is taken.')

# Changing up, I went with a while look that runs 'forever' as set to True, until there is a break
while True:
    # This asks for a user name to be input
    new = input('Type in a user name: ')
    # This is asking, if the length of the list 'current_users' is less than 8, to run what's underneath
    if len(current_users) < 8:
        # This confirms if the input from 'new' is NOT in the 'current_users' list
        if new.lower() not in current_users:
            # If it isn't, it runs the message below, including the 'new' text
            print('Congratulations ' + new.title() + ', that user name is available!')
            # And here, the name is appended to the end of the list, increasing it by one
            current_users.append(new)
        # If the name IS within the list, the following runs
        else:
            # This states that the name entered is taken
            print('I\'m sorry, the user name of ' + new.title() + ' is taken. Please try again.')
            # This runs the loop again, asking for another name
            continue
    else:
        # This runs if the list length hits 8
        print('There is no more room for any more users.')
        # And finally, this stops the 'forever' loop from continuing
        break



