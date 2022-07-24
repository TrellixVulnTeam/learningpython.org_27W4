# This prints out "Hello, Juliano!"
name = "Juliano"
print("Hello, %s!" % name)

# This prints out "Juliano is 31 years old"
name = "Juliano"
age = 31
print("%s is %d years old." % (name, age))

# This prints out: A list: [1, 2, 3]
mylist = [1, 2, 3]
print("A list: %s" % mylist)

# Exercise You will need to write a format string which
# prints out the data using the following syntax:
# Hello John Doe. Your current balance is $53.44

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)
