def do_stuff_with_number(n):
    print(n)


def catch_this():
    the_list = (1, 2, 3, 4, 5)

    for i in range(20):
        try:
            do_stuff_with_number(the_list[i])
        except IndexError:
            # Raised when accessing a non-existing index of a list
            do_stuff_with_number(0)


catch_this()


# Exercise:
# Handle all the exception! Think back to the
# previous lessons to return the last name of the actor.

# Setup
actor = {
    "name": "John Cleese",
    "rank": "awesome"
}


# First name
def get_first_name():
    return actor["name"].split()[0]


# Function to modify (Last name)!!!
def get_last_name():
    return actor["name"].split()[1]


# Test code
get_first_name()
print("First Name Validation")
print("The first name is %s" % get_first_name())
print("-----------------------")
get_last_name()
print("Last Name Validation")
print("The actor's last name is %s" % get_last_name())
