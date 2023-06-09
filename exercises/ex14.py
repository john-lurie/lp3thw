from sys import argv

script, user_name, language = argv
input_str = '---> '

print(f"\nYou selected {language}.\n")

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(input_str)

print(f"Where do you live {user_name}?")
lives = input(input_str)

print("What kind of computer do you have?")
computer = input(input_str)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")

# Study Drill 2: Change the prompt variable to something else entirely.
# Study Drill 3: Add a second argument: language
