import pandas as pd

dict = {
    "country": ["Brazil", "Russia", "India", "China", "South Africa"],
    "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
    "area": [8.516, 17.10, 3.286, 9.597, 1.221],
    "population": [200.4, 143.5, 1252, 1357, 52.98]
}

brics = pd.DataFrame(dict)
print(brics)
print("\n")

# Change index value from number 0 to 4 to the
# two characters representing the country
brics.index = ["BR", "RU", "IN", "CH", "SA"]
print(brics)
print("\n")

# Import the cars.csv data: cars
cars = pd.read_csv('csv/cars.csv')
print(cars)
"""
cars = pd.read_csv('csv/cars.csv', index_col=0)
print(cars['cars_per_cap'])
print(cars[['cars_per_cap']])
print(cars[['cars_per_cap', 'country']])
"""
