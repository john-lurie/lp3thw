people = 20
cats = 30
dogs = 15


if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")


if people == dogs:
    print("People are dogs.")


"""
Study Drills

1. What do you think the "if" does to the code under it?
The code under the "if" is run only if the statement is True.

2. Why does the code under the "if" need to be indented four spaces?
The code is indented to tell Python the if statement applies to that code.

3. What happens if it isn't indented?
Assuming there is an if statement above, Python will raise an IndentationError.

4. Can you put other Boolean expressions from Ex. 27 in the if-statements? Try it.
"""
if people != cats:
    print("People are not cats.")
 
if dogs > people and cats > people:
    print("Too many animals!")

"""
5. What happens if you change the initial values for people, cats, and dogs?
Some if-statements will run that did not run before, and vice-versa.
"""