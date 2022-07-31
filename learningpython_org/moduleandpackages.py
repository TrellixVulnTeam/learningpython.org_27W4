import re
# game.py
# import the draw module

"""
from draw import draw_game


def play_game():
    ...


def main():
    result = play_game()
    draw_game(result)


# this means that if this script is executed, then
# main() will be executed
if __name__ == '__main__':
    main()

"""
"""
if visual_mode:
    # in visual mode, we draw using graphics
    import draw_visual as draw
else:
    # in textual mode, we print out text
    import draw_textual as draw


def main():
    result = play_game()
    # this can either be visual or textual depending on visual_mode
    draw.draw_game(result)
"""
#################################################################
# Exercise: In this exercise, print an alphabetically sorted list
# of all the functions in the re module containing the word find.
#################################################################

# your code goes here
list_functions = []

for functions in dir(re):
    if "find" in functions:
        list_functions.append(functions)

print(sorted(list_functions))
