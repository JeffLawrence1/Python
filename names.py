# Assignment: Names
# Write the following function.

# Part I
# Given the following list:

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
# Copy
# Create a program that outputs:

# Michael Jordan
# John Rosales
# Mark Guillen
# KB Tonel
# Copy
# Part II
# Now, given the following dictionary:

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
# Copy
# Create a program that prints the following format (including number of characters in each combined name):

# Students
# 1 - MICHAEL JORDAN - 13
# 2 - JOHN ROSALES - 11
# 3 - MARK GUILLEN - 11
# 4 - KB TONEL - 7
# Instructors
# 1 - MICHAEL CHOI - 11
# 2 - MARTIN PURYEAR - 13
# Copy
# Note: The majority of data we will manipulate as web developers will be hashed in a dictionary using key-value pairs. Repeat this assignment a few times to really get the hang of unpacking dictionaries, as it's a very common requirement of any web application.

def myList(var):
    for x in var:
        print x["first_name"], x["last_name"]
myList(students)


def myList2(var):
    for x in var:
        count = 0
        print x
        for y in var[x]:
            count = count + 1
            first_name = y["first_name"].upper()
            last_name = y["last_name"].upper()
            char = len(first_name) + len(last_name)
            print "{} - {} {} - {}".format(count, first_name, last_name, char)

myList2(users)
