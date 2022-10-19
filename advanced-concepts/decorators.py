"""
def repeater(old_function):
    def new_function(*args, **kwds):
        old_function(*args, **kwds)
        old_function(*args, **kwds)
    return new_function

>>> @repeater
def multiply(num1, num2):
    print(num1 * num2)


>>> multiply(2, 3)
6
6
"""


"""
def double_out(old_function):
    def new_function(*args, **kwds):
        return 2 * old_function(*args, **kwds)
    return new_function
"""


# def double_Ii(old_function):
#    def new_function(arg):
#        return old_function(arg * 2)
#    return new_function
"""
def check(old_function):
    def new_function(arg):
        if arg < 0:
            raise (ValueError, "Negative Argument")  # This causes an
            # error, wich is better
            # than it doing the wrong thing
        old_function(arg)
    return new_function
"""


def multiply(multiplier):
    def multiply_generator(old_function):
        def new_function(*args, **kwds):
            return multiplier * old_function(*args, **kwds)
        return new_function
    return multiply_generator  # it returns the new generator


# Usage
@multiply(3)
def return_num(num):
    return num


print(return_num(5))  # should return 15


# Exercise:
# Make a decorator factory which returns a decorator that decorates functions
# with one argument. The factory should take one argument, a type, and then
# returns a decorator that makes function should check if the input is the
# correct type. If it is wrong, it should print("Bad Type") (In reality, it
# should raise an error, but error raising isn't in this tutorial). Look at
# the tutorial code and expected output to see what it is if you are confused
# (I know I would be.) Using isinstance(object, type_of_object) or type(object)
# might help.


def type_check(correct_type):
    def check(old_function):
        def new_function(arg):
            if isinstance(arg, correct_type):
                return old_function(arg)
            else:
                print("Bad Type")
        return new_function
    return check


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
times2('Not A Number')


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter("Juliano"))
first_letter(['Not', 'A', 'String'])
