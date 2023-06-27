# Study Drills: Convert while-loop into function with end and step as variables.
def while_looper(end, step=1):
    """Print the process and results of a while-loop

    Parameters:
    -----------
    end : int
        The while loop stops at this value
    step : int, optional
        Advance by this amount per iteration
    """
    i = 0
    numbers = []

    while i < end:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + step
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)

# Study Drill: Use a for-loop instead of a while-loop.
def for_looper(end, step=1):
    """Print the process and results of a for-loop"""
    numbers = []
   
    for i in range(0, end, step):
        print(f"At the top i is {i}")
        numbers.append(i)

        # This will mimic the printing of while_looper.
        # It doesn't affect i in the next iteration or change numbers list.
        i = i + step
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)

# Test the functions
while_looper(6)
while_looper(10, 2)

print("\nNow test a for-loop\n")
for_looper(6)
for_looper(10, 2)
