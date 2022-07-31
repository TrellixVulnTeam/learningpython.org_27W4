"""
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a menssage inside the class.")


classobj = MyClass()

print(classobj.variable)
classobj.function()

"""

"""
class NumberHolder:

    def __init__(self, number):
        self.number = number
        print(number)


objectnumber = NumberHolder(10)
"""

##############################################################################
# Exercise: We have a class defined for vehicles. Create two new vehicles
# called car1 and car2. Set car1 to be a red convertible worth $60,000.00 with
# a name of Fer, and car2 to be a blue van named Jump worth $10,000.00.
##############################################################################

# define the Vehicle class


class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 0.0

    def description(self):
        desc_str = "%s is a %s %s worth $%.2f."\
                % (self.name, self.color, self.kind, self.value)
        return desc_str

# your code goes here


car1 = Vehicle()
car1.color = "red"
car1.kind = "convertible"
car1.value = 600000.00
car1.name = "Fer"


car2 = Vehicle()
car2.color = "blue"
car2.kind = "van"
car2.value = 100000.00
car2.name = "Jump"

# test code
print(car1.description())
print(car2.description())
