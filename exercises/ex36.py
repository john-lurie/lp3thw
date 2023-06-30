"""Hotel Knossos: A text adventure game"""

def reception(props):
    print('\n"Welcome to Hotel Knossos!"')
    print('"What is your name?"')
    props["guest"] = input("> ")

    print(f'\n"Thank you, {props["guest"]}. You will be staying in Room 216."')
    print('"Here is your key card."')
    props["key card"] = True

    print("\nYou walk to the elevator.")
    elevator(props)


def basement(props):
    print("\nYou are in the basement.")
    print("It is dimly lit by torches and smells funny.")
    print("\nDo you wish to continue?")

    further = input("> ").lower()

    if "y" in further:
        print("\nYou wander into the winding maze.")
    else:
        elevator(props)

    if props["thread"]:
        print("Wisely, you unspool the thread the young woman gave you.")

    print("\nSuddenly a terrible monster appears.")
    print("It has the head of bull and the body of a man.")
    print("It roars and begins to charge at you!")

    print("\nWhat do you do?")
    choice = input("> ")

    print("")
    if "flee" in choice and not props["thread"]:
        print("You run in terror, but quickly lose your way.")
        print("The monster eats you alive!")
        dead(props)
    elif "flee" in choice and props["thread"]:
        print("You dash along the maze, following the thread.")
        print("You reach the elevators just in time.")
        elevator(props)
    elif "fight" in choice:
        fight(props)
    else:
        print("You stand in terror as the monster eats you alive!")
        dead(props)


def fight(props):
    print("You bravely stand to face the monster.")

    if props["weapon"]:
        print("You stab the beast through the heart with your sword!")
        print("\nExploring the monster's den, you find a small hand glider.")
        print("Hmm. . . this could come in handy.")
        props["glider"] = True
    else:
        print("But lacking a weapon, you are eaten alive!")
        dead(props)

    if props["thread"]:
        print("\nFollowing the thread, you find your way to the elevator.")
        elevator(props)
    else:
        print("\nYou try to find the elevator, but get lost in the labyrinth.")
        print("You slowly die of dehydration.")
        dead(props)


def second_floor(props):
    print("\nYou are in your room.")
    print("What do you do?")

    choice = input("> ")

    if "search" in choice:
        weapon_search(props)
    elif "sleep" in choice:
        print("\nYou close your eyes and have uneasy dreams.")
    elif "read" in choice:
        print("\nYou read a disturbing tale from Ancient Greece.")
    elif "leave" in choice:
        elevator(props)
    else:
        print("\nYou stare blankly at the wall.")

    second_floor(props)


def weapon_search(props):
    print("\nWhere do you look?")

    choice = input("> ")

    if "closet" in choice:
        print("\nYou find an old banjo.")
    elif "table" in choice:
        print("\nYou find some fresh flowers.")
    elif "bed" in choice and not props["weapon"]:
        print("\nYou find a sharp sword under the bed.")
        print("Hmm. . . this could come in handy.")
        props["weapon"] = True
    else:
        print("\nYou find nothing of value.")

    second_floor(props)


def third_floor(props):
    print("\nOn the third floor is the restaurant.")
    print("It is empty, except for a young woman sitting by herself.")

    print("Do you sit with her or alone?")
    choice = input("> ")

    if "alone" in choice:
        print("\nA waiter appears to take your order.")
        print("You eat dinner quietly and leave the restaurant.")
    elif "with" in choice:
        ariadne(props)
    else:
        print("\nForget about eating.")

    elevator(props)


ariadne_speech = """
"Hello {}."\n
"Yes, I already know who you are. Word travels quickly in this little place. 
If you haven't already figured it out, you are trapped. There is only one hope, 
to defeat the Minotaur that  lives in the basement. But to do that, you will 
need a weapon, perhaps something in the hotel. And this: a spool of thread to 
help you find your way back from the beast's lair. Good luck." """

def ariadne(props):
    if props["thread"]:
        print(f'\n"{props["guest"]}, I already told you what you need to know."')
        print('"Get out now!"')
    else:
        print("\nYou pull up a chair next to the young woman.")
        print(ariadne_speech.format(props["guest"]))
        props["thread"] = True

    elevator(props)


def roof(props):
    print("\nYou are on the roof. It is a pleasant garden.")
    print("What do you do?")

    choice = input("> ")

    if "relax" in choice:
        print("\nYou sunbathe on a chaise lounge chair.")
        roof(props)
    elif "drink" in choice:
        print("\nYou enjoy a glass of wine at the bar.")
        roof(props)
    elif "escape" in choice:
        escape_hotel(props)
    elif "leave" in choice:
        elevator(props)
    else:
        print("\nYou stand there and whistle.")
        roof(props)


def escape_hotel(props):
    print("\nYou walk over to the edge of the roof.")
    print("It is a fifty foot drop to the street below.")
    print("What do you do?")

    choice = input("> ")

    if "jump" in choice and props["glider"]:
        print("\nUsing the hand glider, you fly to safety.")
        win(props)
    elif "jump" in choice and not props["glider"]:
        print("\nYou fall to your death.")
        dead(props)
    else:
        roof(props)


def elevator(props):
    print("")

    if props["key card"]:
        print("You place the key card on the elevator controls.")
        print("The elevator doors open.")
    else:
        print("The elevator controls require a key card.")
        print("You must check in at the reception desk.")
        reception(props)

    while True:
        print("\nChoose a floor: B, 1, 2, 3, R")
        button = input("> ").lower()

        if button == "b":
            basement(props)
        elif button == "1":
            print("Nothing happens. You can't return to the lobby!")
        elif button == "2":
            second_floor(props)
        elif button == "3":
            third_floor(props)
        elif button == "r":
            roof(props)
        else:
            print(f"{button} is not a valid floor.")


def dead(props):
    print("\nYou are dead.")
    print("Would you like to play again?")

    choice = input("> ").lower()

    if "y" in choice:
        start(properties.copy())
    else:
        print("")
        quit()


def win(props):
    print("\n*************************")
    print("Congratulations, you win!")
    print("*************************\n")
    quit()


def start(props):
    print("\n---- HOTEL KNOSSOS ----")
    print("A text adventure game\n")

    print("You are in the hotel lobby.")
    print("Do you go to the reception desk or straight to the elevator?")

    while True:
        choice = input("> ")

        if "reception" in choice or "desk" in choice:
            reception(props)
        elif "elevator" in choice:
            elevator(props)
        else:
            print("\nReception desk or elevator?")


properties = {"guest": None, "key card": False, "thread": False,
              "weapon": False, "glider": False}

start(properties.copy())
