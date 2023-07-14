print("\nData Types")

### True
print("\n'True'")
print("True Boolean value.")

condition = True

if condition:
    print(">>> condition is True")

### False
print("\n'False'")
print("False Boolean value.")

condition = False

# This won't run.
if condition:
    print(">>> condition is False")

### None
print("\n'None'")
print("Represents 'nothing' or 'no value'.")

def my_function():
    print(">>> A function without a return statement returns None.")
    
print(">>>", my_function())

### bytes
print("\n'bytes'")
print("Stores bytes, such as text, PNG, or MP3.")

sigma = b"\xce\xa3"
print(">>>", sigma.decode("utf-8"))

byte_list = [f"{byte:0>8b}" for byte in sigma]
print(">>>", byte_list)

### strings
print("\n'strings'")
print("Stores text.")

sentence = ">>> The sky is blue."
print(sentence)

### numbers
print("\n'numbers'")
print("Stores integers.")

number = 57
print(">>>", number, type(number))

### floats
print("\n'floats'")
print("Stores decimals.")

number = 57.0
print(">>>", number, type(number))

### lists
print("\n'lists'")
print("Stores a list of things.")

fruits = ["apple", "banana", "kiwi"]
print(">>>", fruits[-1])

### dicts
print("\n'dicts'")
print("Stores a set of keys and their values.")

vice_presidents = {"Washington": "Adams", "Adams": "Jefferson",
                   "Jefferson": "Burr (1st), Clinton (2nd)"}
print(">>>", vice_presidents["Adams"])
