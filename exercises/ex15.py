# Import the argv function from the sys module.
from sys import argv

# Unpack script (script name) and filename from argv.
script, filename = argv

# Instantiate file object as txt.
txt = open(filename)

# Announce that contents of filename are about to be printed.
print(f"Here's your file {filename}:")
# Print contents of txt.
print(txt.read())

# Study Drill 7: Call close() on txt and txt_again
txt.close()

# Study Drill 4: Get rid of second reading of file.
"""
# Prompt for the filename again.
print("Type the filename again:")
# Assign user input to file_again.
file_again = input("> ")

# Instantiate file object as txt_again.
txt_again = open(file_again)

# Print contents of txt_again.
print(txt_again.read())

txt_again.close()
"""

# Study Drill 5: Use input to get filename instead of argv
"""
filename = input("Name of file to open: ")

txt = open(filename)

print(f"\nHere's your file {filename}:\n")
print(txt.read())

txt.close()
"""