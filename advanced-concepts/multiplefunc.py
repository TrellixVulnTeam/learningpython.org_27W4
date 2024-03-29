"""
def myfunction(first, second, third):
    # do something with the 3 variables
    sum = first + second + third
    return sum


print(myfunction(1, 2, 3))


def foo(first, second, third, *therest):
    print("First: %s" % (first))
    print("Second: %s" % (second))
    print("Third: %s" % (third))
    print("And all the rest... %s" % (list(therest)))


foo(1, 2, 3, 4, 5)


def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: %d" % (first + second + third))

    if options.get("number") == "first":
        return first


result = bar(1, 2, 3, action="sum", number="first")
print("Result %d" % (result))
"""
# Exercise below:
# Fill in the foo and bar functions so they can receive a variable amount of
# arguments (3 or more) The foo function must return the amount of extra
# arguments received. The bar must return True if the argument with the
# keyword magicnumber is worth 7, and False otherwise.


def foo(a, b, c, *args):
    return len(args)


def bar(a, b, c, **kwargs):
    return kwargs["magicnumber"] == 7


# test code
if foo(1, 2, 3, 4) == 1:
    print("Good.")

if foo(1, 2, 3, 4, 5) == 2:
    print("Better.")

if bar(1, 2, 3, magicnumber=6) == False:
    print("Great.")

if bar(1, 2, 3, magicnumber=7) == True:
    print("Awesome!")
