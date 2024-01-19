# Learning Data Structures - TUPLES
# A tuple is a sequence of immutable Python objects. Tuples are sequences, just
# like lists. The differences between tuples and lists are, the tuples cannot be
# changed unlike lists and tuples use parentheses, whereas lists use square
# brackets.

tuple_one = ("physics", "mathematics", 777, 888)

# Accessing values
print(f"tuple_one[0:3] {tuple_one[0:3]}")

# "Updating" tuples
tuple_two = (34, 56, 78)
tuple_three = ("a", "b", "c")
tuple_four = tuple_two + tuple_three
print(tuple_four)

# Delete tuples
del tuple_four

# Length
print(len(tuple_two))

# Repetition
tuple_five = ("Hello!" * 9)
for x in tuple_five:
    print(x)

# Membership
print("a" in tuple_three)


