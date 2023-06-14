def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# Study Drill 2: Work out the puzzle
# A puzzle for the extra credit, type it in anyway.
print("\nHere is a puzzle.")

# Notice the operations are done inside out, starting with divide.
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")

formula = "(age + (height - (weight * (iq / 2))))"
result = eval(formula)

print(f"\nThe formula is {formula}")
print(f"The result is {result}  Correct? {result == what}")

# Study Drill 3: Write a simple formula and use the functions to calculate it
print("\nNow to calculate the Body Mass Index")
bmi = divide(multiply(703, weight), multiply(height, height))
print(f"Body Mass Index = {round(bmi, 1)}")
