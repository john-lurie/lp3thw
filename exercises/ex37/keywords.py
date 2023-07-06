import keyword

print("\nKeywords")

print("\nA list of keywords is available from keyword.kwlist:")
print(keyword.kwlist)

print("\nNOTE: Some of Shaw's 'keywords' are in fact built-in functions, such as 'exec'.")
print("To see a list of built-in names: import builtins ; dir(builtins)") 

### and
print("\n'and'")
print("True if BOTH elements are True, False otherwise.")
print(">>> True and True =", True and True)
print(">>> False and True =", False and True)

### as
print("\n'as'")
print("Part of with-as statement. cf. 'with'")

### assert
print("\n'assert'")
print("Used primarily for documenting, debugging, and testing code.")
print("Will raise an AssertionError if statement is False.")

number = 3
# will not raise an AssertionError
assert number > 2, f"Number greater than 2 expected, got: {number}"

number = 1
# raises AssertionError
# assert number > 2, f"Number greater than 2 expected, got: {number}"

### break
print("\n'break'")
print("Stops a loop.")

for ii in range(0, 6):
    if ii > 3:
        break

    print(">>>", ii)

### class
print("\n'class'")
print("Defines a class.")

class Cat:
    def __init__(self):
        self.species = "felis catus"

    def meow(self):
        print(">>> Meow")
        
kitty = Cat()
kitty.meow()

### continue
print("\n'continue'")
print("Stop this iteration in loop, go to next iteration.")

for ii in range(6):
    print(">>> above 'continue':", ii)
    if ii > 3:
        continue
    # this won't run if ii > 3
    print(">>> below 'continue':", ii)
    
### def
print("\n'def'")
print("Define a function.")

def add(x, y):
    return x + y
    
print(">>>", add(2.2, 3.3))

### elif
print("\n'elif'")
print("Second, third, etc. conditions in an if-statement.")
print("See 'if' below for example.")

### else
print("\n'else'")
print("Handles any conditions that don't satisfy if or elif conditions.")
print("See 'if' below for example.")

### except
print("\n'except'")
print("If an exception happens, do this. See 'try' below for example.")

### eval
print("\n'eval'")
print("Evaluates a single line of source code, given as a string.")

number = 3
print("'eval' can return the result of the evaluation.")
result = eval("number + 4")
print(">>>", result) 

print("'eval' cannot modify variables.")
# eval("result = 1") # raises SyntaxError

multiline_code = "print('>>> Hello'); print('>>> Goodbye')"
loop_code = "for jj in range(4): print('>>>', jj)"

print("'eval' cannot run multiple lines of code, including loops.")
# eval(multiline_code) # raises SyntaxError
# eval(loop_code) # so will this

### exec
print("\n'exec'")
print("Executes a block of code, given as a string. More powerful than 'exec'.")

print("'exec' CANNOT return the result of the execution.")
result = exec("number + 4")
print(">>>", result)

print("'exec' CAN modify variables.")
number = 4
exec("number *= 2")
print(">>>", number)

print("'exec' CAN run multiple lines of code, including loops.")
exec(multiline_code)
exec(loop_code)

### finally
print("\n'finally'")
print("Exceptions or not, finally do this no matter what.")
print("See 'try' below for example.")

### for
print("\n'for'")
print("Loop over a collection of things.")
print("See 'break' and 'continue' for examples.")

### from
print("\n'from'")
print("Import from a specific part of a module. (cf. 'import')")
from sys import argv
print(">>>", argv)

### global
print("\n'global'")
print("Make a variable inside a function available outside the function.")

def make_global():
    global color 
    color = "red" # this will be available outside
    size = "large" # this will not

make_global()
print(">>>", color)
# print(size) # raises NameError

### if
print("\n'if'")
print("First line in an if-statement. Used to make decisions.")

number = 2
if number <= 1:
    print(">>> number <= 1")
elif 1 < number <= 3:
    print(">>> 1 < number <= 3")
else:
    print(">>> number > 3")

### import
print("\n'import'")
print("Import a module into the script.")

import sys
print(">>>", sys.argv)

### in
print("\n'in'")
print("Check if value is in a sequence, or for use in for-loops (cf. 'for').")

print(">>>", "a" in "cat")

### is
print("\n'is'")
print("Check if two variable are the same object.")
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(">>>", x is y)
print(">>>", x is z)

### lambda
print("\n'lambda'")
print("Create short functions. Can only have one line.")
multiply = lambda a, b: a * b
print(">>>", multiply(3, 4))

### not
print("\n'not'")
print("Logical not")
print(">>>", not True)

### or
print("\n'or'")
print("Logical or")
print(">>>", True or False)

### pass
print("\n'pass'")
print("Avoids an error when empty code is not allowed.")

# def do_something(): # raises IndentationError
def do_something_else(): pass # will run

### print
print("\n'print'")
print("Prints a string. (Like this one!)")

### raise
print("\n'raise'")
print("Raises an error if something goes wrong.")

digit = "3"
# if not type(digit) is int:
#     raise TypeError(f"int expected, got: {type(digit)}")

### return
print("\n'return'")
print("Exit a function with a return value. (cf. 'def')")

### try
print("\n'try'")
print("Try something. If there is an exception, do something else.")

digit = "three"
try:
    int(digit)
    print(f">>> Here's your int: {digit}")
except ValueError:
    print(f">>> '{digit}' cannot be converted to int.")
finally:
    print(">>> Nice work in any case!")

### while
print("\n'while'")
print("Iterate while condition is True")

ii = 0
while ii < 4:
    print(">>>", ii)
    ii +=1

### with
print("\n'with'")
print("Simplifies resource management, i.e., dealing with files.")

# The file will automatically be closed.
with open("test.txt", "w") as file:
    file.write("Hello!\n")
    
### yield
print("\n'yield'")
print("Turns a function into a generator that can be iterated over.")

def function_generator():
    yield "A"
    yield "B"
    yield "C"

for item in function_generator():
    print(">>>", item)
