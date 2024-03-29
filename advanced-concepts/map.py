my_pets = ['alfred', 'tabitha', 'william', 'arla']
uppered_pets = []


for pet in my_pets:
    pet_receive = pet.upper()
    uppered_pets.append(pet_receive)

print(uppered_pets)

my_pets = ['alfred', 'tabitha', 'william', 'arla']
uppered_pets = list(map(str.upper, my_pets))

print(uppered_pets)

# Python 3

circle_areas = [3.56773, 5.57668, 4.00913, 56.24241, 9.01344, 32.00013]
result = list(map(round, circle_areas, range(1, 7)))

print(result)


circle_areas = [3.56773, 5.57668, 4.00913, 56.24241, 9.01344, 32.00013]
result = list(map(round, circle_areas, range(1, 3)))

print(result)


# Python 3

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1, 2, 3, 4, 5]

results = list(zip(my_strings, my_numbers))


print(results)

my_strings = ['a', 'b', 'c', 'd']
my_numbers = [1, 2, 3, 4, 5, 6]

results = list(map(lambda x, y: (x, y), my_strings, my_numbers))
print(results)

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1, 2, 3, 4, 5]

results = list(map(lambda x, y: (x, y), my_strings, my_numbers))

print(results)
