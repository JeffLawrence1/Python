# Assignment: Find Characters
# Write a program that takes a list of strings and a string containing a single character, and prints a new list of all the strings containing that character.

# Here's an example:

# # input
# word_list = ['hello','world','my','name','is','Anna']
# char = 'o'
# # output
# new_list = ['hello','world']
# Copy
# Hint: how many loops will you need to complete this task?

def findChar(word_list, char):
    newArr = []
    for i in range (0, len(word_list)):
        if word_list[i].find(char) != -1:
            newArr.append(word_list[i])
    print newArr

findChar(word_list, char)
