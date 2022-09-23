# Example 1
import json
import pickle

json_string = json.dumps([1, 2, 3, "a", "b", "c"])
print(json.loads(json_string))


# Example 2

pickled_string = pickle.dumps([1, 2, 3, "a", "b", "c"])
print(pickle.loads(pickled_string))


# Exercise: The aim of this exercise is to print
# out the JSON string with key-value pair "Me": 800 added to it.


# fix this function, so it adds the given name
# and salary pair to salaries_json, and return it
def add_employee(salaries_json, name,  salary):
    salaries = json.loads(salaries_json)
    salaries[name] = salary

    return json.dumps(salaries)


# test code
salaries = '{"Alfred" : 300, "Jane" : 400 }'
new_salaries = add_employee(salaries, "Me", 800)
decoded_salaries = json.loads(new_salaries)
print(decoded_salaries["Alfred"])
print(decoded_salaries["Jane"])
print(decoded_salaries["Me"])
