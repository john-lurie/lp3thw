# Two types of people in binary looks like ten in decimal.
types_of_people = 10

# Put the above integer inside this string.
x = f"There are {types_of_people} types of people."

# Put two strings inside of a string.
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

# Print the strings
print(x)
print(y)

# Print the strings again, embedded in yet more strings.
print(f"I said: {x}")
print(f"I also said: '{y}'")

# Put a Boolean inside of a string.
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# Print the string
print(joke_evaluation.format(hilarious))

# Concatenate two strings.
w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
