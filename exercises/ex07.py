# Print "Mary had a little lamb."
print("Mary had a little lamb.")
# Print "Its fleece was white as snow."
print("Its fleece was white as {}.".format('snow'))
# Print "And everywhere that Mary went."
print("And everywhere that Mary went.")
# Print "." ten times
print("." * 10) # what'd that do?

# Assign letters in the words "Cheese Burger" to end1 through end12
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch end = ' ' at the end. try removing it to see what happens
# Concatenate end1 through end 6 to spell "Cheese"
# end=' ' specifies a space at end of line instead of a carriage return?
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
# Concatenate end7 through end 12 to spell "Burger"
print(end7 + end8 + end9 + end10 + end11 + end12)
