print(set("my name is Eric and Eric is my name".split()))


a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.intersection(b))
print(b.intersection(a))

print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

print(a.difference(b))
print(b.difference(a))

print(a.union(b))

# Exercise: In the exercise below, use the given lists to print out a set
# containing all the participants from event A which did not attend event B.

a = ["Jake", "John", "Eric"]
b = ["John", "Jill"]
