# Assignment: Type List
# Write a program that takes a list and prints a message for each element in the list, based on that element's data type.

# Your program input will always be a list. For each item in the list, test its data type. If the item is a string, concatenate it onto a new string. If it is a number, add it to a running sum. At the end of your program print the string, the number and an analysis of what the list contains. If it contains only one type, print that type, otherwise, print 'mixed'.

# Here are a couple of test cases. Think of some of your own, too. What kind of unexpected input could you get?

# #input
# a = ['magical unicorns',19,'hello',98.98,'world']
# #output
# "The list you entered is of mixed type"
# "String: magical unicorns hello world"
# "Sum: 117.98"
# Copy
# # input
# a = [2,3,1,7,4,12]
# #output
# "The list you entered is of integer type"
# "Sum: 29"
# Copy
# # input
# a = ['magical','unicorns']
# #output
# "The list you entered is of string type"
# "String: magical unicorns"

def type_list(var):
    sum = 0
    words = ""

    for val in var:
        if isinstance(val, int) or isinstance (val, float):
            sum = sum + val
        elif isinstance(val, str):
            words = words + val

    if words and sum:
        print words
        print sum
        print "mixed"

    if words:
        print words
        print "string"

    if sum:
        print sum
        print "numbers"

type_list(a)