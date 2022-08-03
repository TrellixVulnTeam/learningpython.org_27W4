import numpy as np

weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Create a numpy array np_weight_kg from weight_kg
np_weight_kg = np.array(weight_kg)

np_weight_lbs = np_weight_kg * 2.2

# I don't need to do this way because arrays in numpy format
# are more easy to work with and make math operations
"""
for weight_lbs in np_weight_kg:
    weight_lbs = np_weight_kg * 2.2
    np_weight_lbs = weight_lbs
"""

print(np_weight_lbs)
