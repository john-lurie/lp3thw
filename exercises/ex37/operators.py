print("\nOPERATORS")

### +, -, *
print("\n'+, -, *'")
print("Addition, subtraction, multiplication")

print(">>>", 3 - 1 + 2 * 4)

### **
print("\n'**'")
print("Exponentiation")

print(">>>", 2 ** 8)

### /, //
print("\n'/, //'")
print("Float and floor division")

print(">>>", 5 / 2)
print(">>>", 5 // 2)

### %
print("\n'%'")
print("Modulus")

print(">>>", 5 % 2)

### >, <
print("\n'>, <'")
print("Greater-than, less-than")

print(">>>", 9 > 8)
print(">>>", 9 < 8)

### >=, <=
print("\n'>=, <='")
print("Greater-than-equal, less-than-equal")

print(">>>", 9 >= 8)
print(">>>", 9 <= 9)

### ==, !=
print("\n'==, !='")
print("Equal, not-equal")

print(">>>", 6 == 3 * 2)
print(">>>", "cat" != "cat")

### (), [], {}
print("\n'(), [], {}'")
print("Parentheses, square brackets, curly brackets")

print(">>>", type((1, 2, 3)))
print(">>>", type([1, 2, 3]))
print(">>>", type({"one": 1, "two": 2, "three": 3}))

### @
print("\n'@'")
print("At (decorators)")
print("Used to modify a function by wrapping it inside another function.")
print("Helpful in defining classes.")

def announce_decorator(function):

    def inner():
        print(f">>> {function} has been decorated")
        function()

    return inner

@announce_decorator
def hello():
    print(f">>> Hello!")

hello()

# Same as this:
# say_hello = announce_decorator(hello)
# say_hello()

### ,
print("\n','")
print("Comma")

print(">>> How", "are", "you", "today?")

### :
print("\n':'")
print("Colon")

for ii in range(3):
    print(">>>", ii)

### .
print("\n'.'")
print("Dot")

print(">>>", "wow!".upper())

### =
print("\n'='")
print("Assign equal")
variable = ">>> something"
print(variable)

### ;
print("\n';'")
print("Semicolon")

number = 17; print(">>>", number)

### +=, -=
print("\n'+=, -='")
print("Add and assign, subtract and assign")

number = 5
number += 1
number -= 2
print(">>>", number)

### *=, /=
print("\n'*=, /='")
print("Multiply and assign, float divide and assign")

number = 3
number *= 7
number /= 2
print(">>>", number)

### //= %=
print("\n'//=, %='")
print("Floor divide and assign, modulus and assign")

number = 9
number //= 2
number %= 4
print(">>>", number)

### **=
print("\n'**='")
print("Exponentiation and assign")

number = 9
number **= 2
print(">>>", number)
