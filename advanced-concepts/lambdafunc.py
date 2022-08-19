"""
def sum(a, b):
    return a + b


a = 1
b = 2
c = sum(a, b)
print(c)
"""
# with lambda function now
a = 1
b = 2
sum = lambda a, b: a + b
c = sum(a, b)
print(c)

# Exercise:
# Write a program using lambda functions to check if a number in the
# given list is odd. Print "True" if the number is odd or "False" if
# not for each element.
"""
l = [2, 4, 7, 3, 14, 19]
for i in l:
    if i % 2 == 1:
        print("Number %d, True" % i)
    else:
        print("Number %d, False" % i)
"""

# With Lambda function
list = [2, 4, 7, 3, 14, 19]
for i in list:
    lambda_func = lambda i: (i % 2) == 1
    print(lambda_func(i))
