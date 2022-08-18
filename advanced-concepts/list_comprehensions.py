# List Comprehensions down below
"""
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []
for word in words:
    if word != "the":
        word_lengths.append(len(word))

print(words)
print(word_lengths)
"""

# now the same code using list Comprehensions
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = [len(word) for word in words if word != "the"]
print(words)
print(word_lengths)

# Exercise: Using a list comprehension, create a new List
# called "newlist" out of the list "numbers", which contains
# only the positive numbers from the list, as integers

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
# this is the list comprehensions way
# newlist = [int(number) for number in numbers if number > 0]

# without list comprehensions
newlist = []
for number in numbers:
    if number > 0:
        newlist.append(int(number))

print(numbers)
print(newlist)
