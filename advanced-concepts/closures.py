# Example 1

def transmit_to_space(message):
    "This is the enclosing function"

    def data_transmitter():
        "The nested function"
        print(message)

    data_transmitter()


print(transmit_to_space("Test message"))


# Example 2
def print_msg(number):
    def printer():
        "Here we are using the nonlocal keyword"
        nonlocal number
        number = 3
    printer()
    print(number)


print_msg(5)


# Example 3
def transmit_to_space(message):
    "This is the enclosing function"
    def data_transmitter():
        "The nested function"
        print(message)
    return data_transmitter


transmitter = transmit_to_space("Burn the Sun!")
transmitter()

# Exercise
# Make a nested loop and a python closure to make
# functions to get multiple multiplication functions
# using closures. That is using closures, one could
# make functions to create multiply_with_5() or
# multiply_with_4() functions using closures.


# your code goes Here

def multiply_function(num):
    def multiplier_of(number):
        return number * num

    return multiplier_of


multiplywith5 = multiply_function(5)
print(multiplywith5(9))
