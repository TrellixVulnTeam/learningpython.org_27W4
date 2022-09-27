from functools import partial


def multiply(x, y):
    return x * y


# Create a new function that multiplies by 2
dbl = partial(multiply, 2)
print(dbl(4))


# Exercise :
# Edit the function provided by calling partial() and replacing
# the first three variables in func(). Then print with the new partial
# function using only one input variable so that the output equals 60.

def func(u, v, w, x):
    return u * 4 + v * 3 + w * 2 + x


func_partial = partial(func, 5, 6, 7)
print(func_partial(8))
