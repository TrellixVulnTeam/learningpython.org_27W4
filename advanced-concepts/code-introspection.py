# Exercise:
# Print a list of all atributes of the given Vehicle objectself.

"""
help(dir)
help(hasattr)
help(id)
"""


# Define the Vehicle classself.
class Vehicle:
    name = "Beatle"
    kind = "car"
    color = "Red"
    value = 100.000

    def description(self):
        desc_str = "%s is a %s %s and worth $%.2f."\
            % (self.name, self.color, self.kind, self.value)
        return desc_str


# print(dir(Vehicle)) This will print all attributes of the Vehicle class.

vehicle = Vehicle()
print(vehicle.description())
