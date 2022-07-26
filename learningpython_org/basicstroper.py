# This prints Hello world two times
astring = "Hello world!"
astring2 = 'Hello world!'
print(astring + " " + astring2)

# This prints
astring = "Hello world!"
print("single quotes are ' '")

print(len(astring))

astring = "Hello world!"
print(astring.index("o"))

astring = "Hello world!"
print(astring.count("l"))

astring = "Hello world!"
print(astring[3:7])

# This prints lo w and I don't know why but it does that
astring = "Hello world!"
print(astring[3:7:2])

# This I'm quite not sure what it does
astring = "Hello world!"
print(astring[3:7])
print(astring[3:7:1])

# This prints the reverse string
astring = "Hello world!"
print(astring[::-1])

# This prints the string uppercase and then lowercase
astring = "Hello world!"
print(astring.upper())
print(astring.lower())

astring = "Hello world!"
print(astring.startswith("Hello"))
print(astring.endswith("asdsadsafddas"))

astring = "Hello world!"
afewwords = astring.split(" ")
print(afewwords)

################################################
# Exercise: Try to fix the code to print out...
# the correct information by changing the string
################################################

s = "Strings are awesome!"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurence of "a" should be at index 8
print("The first occurence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5])  # Start to 5
print("The next five characters are '%s'" % s[5:10])  # 5 to 10
print("The thirteenth character is '%s'" % s[12])  # Just number 12
print("The characters with odd index are '%s'" % s[1::2])  # (0-based indexing)
print("The last five characters are '%s'" % s[-5:])  # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))
