ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) # whoa! fancy
print(stuff.pop())
print(' '.join(stuff)) # what? coo1!
print('#'.join(stuff[3:5])) # super stellar!

# Study Drills
# 1. Take each function that is called and translate them to what Python does.
# 2. Translate these two ways to view the function calls into English.
"""
# call split on ten_things with argument ' '  == 
# call split with arguments ten_things and ' '
ten_things.split(' ') == split(ten_things, ' ')

# Call pop on more_stuff == call pop with argument more_stuff
more_stuff.pop() == pop(more_stuff)

# Call append on stuff with argument next_one == 
# call append with arguments stuff and next_one
stuff.append(next_one) == append(stuff, next_one)

# Call pop on stuff == call pop with argument stuff
stuff.pop() == pop(stuff)

' '.join(stuff) # cannot be translated according to Shaw
'#'.join(stuff[3:5]) # cannot be translated
"""

# 6. Find ten examples of things in the real world that would fit in a list.
# Try writing some scrips to work with them.
"""
1. Presidents of the United States, 2. a library catalog, 
3. ingredients in recipe, 4. book table of contents, 5. nations in the UN,
6. letters in the alphabet, 7. colors of the rainbow, 8. flavors of ice cream,
9. orders of birds, 10. items in this list
"""

letters = "A B C D E F G H I J K M N O P Q R S T U V W X Y Z".split(' ')

print(f"\nThe English alphabet: {letters}")
print("Oops, forgot 'L'. It comes after 'K'.")

letters.insert(letters.index("K") + 1, "L")
print("\nThat's better.")
print(letters)
