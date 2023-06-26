"""A program to quiz knowledge of truth tables

This is not part of Shaw's book. I wrote it for practice.
"""

from sys import argv
from random import shuffle

tables = ["not False", "not True", 
"True or False", "True or True", "False or True", "False or False",
"True and False", "True and True", "False and True", "False and False",
"not (True or False)", "not (True or True)", "not (False or True)", "not (False or False)",
"not (True and False)", "not (True and True)", "not (False and True)", "not (False and False)",
"1 != 0", "1 != 1", "0 != 1", "0 != 0",
"1 == 0", "1 == 1", "0 == 1", "0 == 0"]

input_lookup = {'t': True, 'f': False, 'quit': None}

print("\nThis is a quiz of the truth tables.")
print("Type 't' (True), 'f' (False), or 'quit'.\n") 

if 'shuffle' in argv:
    print("Tables have been randomly shuffled!\n")
    shuffle(tables)

ii = 0

while ii <  len(tables):
    statement = tables[ii]
    answer = input(f"{statement} ? ")

    if answer not in input_lookup:
        print("Invalid input. Must be 't' (True), 'f' (False), or 'quit'.\n")
    elif answer == 'quit':
        print("")
        break
    else:
        if input_lookup[answer] == eval(statement):
            print("Correct\n")
        else:
            print("Incorrect\n")
        ii += 1
