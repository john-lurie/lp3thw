name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

# Study Drills
# 1. Change all the variable names so there is no my_ in front of each one.

# 2. Write variables to convert inches and pounds to centimeters and kilograms.
height_cm = round(height * 2.54, 1)
weight_kg = round(weight * 0.4536, 1)

print()
print(f"{name}'s height is {height_cm} cm and weight is {weight_kg} kg.")
