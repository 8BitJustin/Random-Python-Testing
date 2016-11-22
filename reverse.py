# Simple code, will reverse the word placed within the 'input'

# Input, asks for a word, and stores that word in the 'reverse' variable
reverse = input('Word? ')
# The slice operator takes three parameters, where it starts and ends, but also what step to take as it increments.
# You could pass in 2 to get every second letter, here I pass in a negative value to start at the end and
# work backwards, hence reversing your string.
print(reverse[::-1])