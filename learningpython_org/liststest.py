from fastapi import FastAPI
from pandas import numpy

list_functions_with_the_word_api = []

for functions in dir(FastAPI):
    if "api" in functions:
        list_functions_with_the_word_api.append(functions)

print(sorted(list_functions_with_the_word_api))

"""
list_functions_with_num = []

for function in dir(numpy):
    if "num" in function:
        list_functions_with_num.append(function)

print(sorted(list_functions_with_num))
"""
