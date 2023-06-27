print("""You enter a dark room with three doors.
Do you go through door #1, #2, or #3?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

# Study Drill 1: Make a new part of the game.
elif door == "3":
    print("You are greeted by a beautiful merman holding a trident.")
    print("He asks you for a number greater than 3 and less than or equal to 10.")
    
    number = input("> ")

    try:
        number = float(number)
    except ValueError:
        print(f"{number} is not a number.")
        print("The merman kills you with his scorn.")
        quit()
    
    if number <= 3:
        print(f"{number} <= 3. The merman throws his trident through your heart.")
    elif 3 < number <= 10:
        print("The merman lets you pass. You escape the dungeon.")
    else:
        print(f"{number} > 10. The merman throws his trident through your stomach.")
            
else:
    print("You stumble around and fall on a knife and die. Good job!")
