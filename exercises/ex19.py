def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


# Study Drill 3: Write at least one function of your own design, run 10 ways
def do_arithmetic(arg1, arg2, operator):
    fstr = f"{arg1} {operator} {arg2}"
    print(f"{fstr} = {eval(fstr)}")

print("Study Drill 3")
print("Some testing of my do_arithmetic function (really a test of eval):")

do_arithmetic(2, 3, '+')             # with ints
do_arithmetic('2', '3', '+')         # with strings
do_arithmetic(4, -7, '+')            # with negative int
do_arithmetic(3.14159, 3.14159, '-') # arbitrary precision
do_arithmetic(9, 1, '*')             # multiplication by unity
do_arithmetic(1/2, 4, '*')           # rational number as int division
do_arithmetic('1/2', 4, '*')         # rational number as str
do_arithmetic(121, 11, '/')          # float division
do_arithmetic(121, 11, '//')         # integer division
do_arithmetic(3, '(1/2)', '/')       # parentheses needed
