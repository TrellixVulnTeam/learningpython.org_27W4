mylist = []

mylist.append(1)
mylist.append(2)
mylist.append(3)


print(mylist[0])  # prints 1
print(mylist[1])  # prints 2
print(mylist[2])


# prints out 1, 2, 3
for x in mylist:
    print(x)

""""
mylist = [1, 2, 3]
print(mylist[10])
"""

numbers = []
strings = []
names = ["Michele", "Adriane", "Juliano"]
second_name = names[1]

numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("hello")
strings.append("world!")

print(numbers)
print(strings)
print(names)
print("The second name on the names list is %s" % second_name)
