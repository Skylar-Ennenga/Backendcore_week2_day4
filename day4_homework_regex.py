# 1. Python Regular Expressions Mastery


# Task 1: Name Verification


# Problem Statement:  Write a function that takes in a list of names, and verifies that the names are valid names using a regex pattern and match(), and prints the name if it is valid, "Invalid name" if the name is not.

# Use the following list as an argument to test your function.





# Expected Outcome:

# Abraham Lincoln
# Andrew P Garfield
# Invalid name
# Connor Milliken
# Jordan Alexander Williams
# Invalid name
# Invalid name


import re

# Funstion takes in a list of names
# Verify that they are valid names based on a regex pattern
# If it is Valid then print out that name
# Print out and invalid name sting if its not

# Code Example:
names = ["Abraham Lincoln", "Andrew P Garfield", "peter pan", "Connor Milliken", "Jordan Alexander Williams", "Madonna", "programming is cool"]

def name_verfiication (names): #Function takes in names
    pattern = re.compile(r"([A-Z][a-z]+) ([A-z]* )?([A-Z][a-z]+)") 
    # pattern = re.compile(r"^[A-Z][a-z]*(?: [A-Z](?:[a-z]*)?)? [A-Z][a-z]*$") #Pattern that we will be checking against ^ = Start of string [A-Z] = first letter Capital [a-z] = preceding lower letters * = 0 or more occurances of a lower case letter
    # (?: [A-Z] = Accounts for the occurance of just a capital middle initial (?: [A-Z](?:[a-z]*)?)? = accounts for the possiblity of a middle name with a capital - "?" = mean that its not required but accounted for if there
    # [A-Z][a-z]* = Same as first word $ = asserts the end of the string
    
    for name in names:                                                       
        if re.match(pattern, name):                                          
            print(name)
        else:
            print("Invalid Name")

    
    
name_verfiication(names)    
    
    
    
  
