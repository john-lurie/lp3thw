print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# Study Drill 2: Try other ways to use input().
number = float(input("\nEnter a number to square: "))
print(f"{number} x {number} = ", number * number)

# Study Drill 3: Write another form to ask some questions.
city = input("\nWhat city do you live in? ")
state = input("What state do you live in? ")

print("You live in {}, {}.".format(city, state))
