print("\nSTRING FORMATTING")

print("\nEscape Sequences")

### Backslash
print("\n'Backslash'")
print(">>> It seems \ does't need to be escaped, but it can be: \\")

### Single-quote
print("\n'Single-quote'")
print('>>> This line won\'t work without escaping the apostrophe.')

### Double-quote
print("\n'Double-quote'")
print(">>> The cow says, \"moo\".")

### Bell
print("\n'Bell'")
print(">>> \aThis should sound a bell. It doesn't seem to work.")

### Backspace
print("\n'Backspace'")
print(">>> The number 1 will be overwritten: 1\bX")

### Formfeed
print("\n'Formfeed'")
print(">>> 1\f2\f3")

### Newline
print("\n'Newline'")
print(">>> I use newline\nall the time.")

### Carriage
print("\n'Carriage'")
print("         back to the beginning of the line.\r>>> Goes")

### Tab
print("\n'Tab'")
print(">>> Get\t\taway from me!")

### Vertical tab
print("\n'Vertical tab'")
print(">>> Mind the \vgap.")

print("\n\nString Formatting")
print("\nNOTE: Using Python 3 string formatting instead of Shaw's suggested Python 2.")

### d
print("\n'd'")
print("Decimal integers (not floating point).")
print(">>> {:d}".format(45))

### i
print("\n'i'")
print("Same as d. Deprecated.")

### o
print("\n'o'")
print("Octal (base 8) number.")
print(">>> {:o}".format(1000))

### u
print("\n'u'")
print("Unsigned decimal. Deprecated.")

### x
print("\n'x'")
print("Hexadecimal lowercase.")
# NOTE: Using 2000 instead of 1000 because 1000 == 3e8 looks like exponential.
print(">>> {:x}".format(2000))

### X
print("\n'X'")
print("Hexadecimal uppercase.")
print(">>> {:X}".format(2000))

### e
print("\n'e'")
print("Exponential notation, lowercase 'e'.")
print(">>> {:e}".format(1000))

### E
print("\n'E'")
print("Exponential notation, uppercase 'E'.")
print(">>> {:E}".format(1000))

### f
print("\n'f'")
print("Floating point real number.")
print(">>> {:f}".format(10.34))

### F
print("\n'F'")
print("Same as 'f' but NAN and INF in uppercase.")
print(">>> {:F}".format(float('NaN')))

### g
print("\n'g'")
print("Either e or f, depending on magnitude of number.")
print(">>> {:g}".format(10.34))

### G
print("\n'G'")
print("Same as g but uppercase.")
print(">>> {:G}".format(10.34 * 10 ** 9))

### c
print("\n'c'")
print("Converts integer to Unicode character.")
euro = int("20AC", 16)
print(">>> {0:c}".format(euro))

### !r
print("\n'!r'")
print("Repr (debugging) format.")
print(">>> {!r} (note the quotes)".format("peanut"))

### s
print("\n's'")
print("String format.")
print(">>> {:s}".format("peanut"))

### %%
print("\n'%%'")
print("Puts a percent sign in v2 string formatting.")
print(">>> %g%%" % 10.34)

print("Not to be confused with '%' in v3 formatting.")
print(">>> {:%}".format(0.01))
