from sys import argv

script, input_file = argv

# Read file from current position
def print_all(f):
    print(f.read())

# Move head to start of file
def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    """line_count is independent of current head position.
    It is manually incremented in the script below.
    """
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

# Study Drill 5: use += instead of current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

# Added this to Shaw's original script
current_file.close()
