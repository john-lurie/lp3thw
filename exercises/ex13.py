from sys import argv
# read the WYSS section for how to run this

script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# Study Drill 2: Write scripts with fewer and more arguments
"""
filename, arg1, arg2 = argv

print(f"The filename is: {filename}")
print(f"The first argument is: {arg1}")
print(f"The second argument is: {arg2}")
"""

"""
dotpyfile, var1, var2, var3, var4 = argv

print("The python file is named: {}".format(dotpyfile))
print("The 1st variable is: {}".format(var1))
print("The 2nd variable is: {}".format(var2))
print("The 3rd variable is: {}".format(var3))
print("The 4th variable is: {}".format(var4))
"""

# Study Drill 3: Combine input with argv
"""
first_name = argv[1]

last_name = input(f"Hello, {first_name}. What is your last name? ")
print(f"Nice to meet you, {first_name} {last_name}.")
"""