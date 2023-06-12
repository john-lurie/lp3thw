from sys import argv

script, filename = argv

print(f"We're going to erase {filename}")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w+')

# Study Drill 5: If opened with 'w' mode, automatically truncated.
"""
print("Truncating the file. Goodbye!")
target.truncate()
"""

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# Study Drill 3: Write the file in one line instead of six.
target.write(f"{line1}\n{line2}\n{line3}\n")

# Study Drill 2: Read the file.
print("\nHere is the file you just wrote:")
# Must be in 'w+' mode and seek to beginning of file.
target.seek(0)
print(target.read())

print("And finally, we close it.")
target.close()
