# Learning Data Structures - LISTS

list_one = ["physics", "mathematics", 1983, 1986]
list_two = [123, 456, 789, 999]

# Accessing values
print(f"list_one[0]: {list_one[0]}")
print(f"list_two[1:2] {list_two[1:3]}")

# Updating lists
list_two[3] = 777
print(f"New value at index 3: {list_two[3]}")

# Delete list elements
del list_two[3]
for x in list_two:
    print(x)

# Concatenation
list_three = ["New York", "Los Angeles", 444, 28.5]
list_four = [34.5, 9999, "Canada", "Mexico"]
list_five = list_three + list_four
for x in list_five:
    print(x)

# Membership
print("Canada" in list_five)

# Repetition
list_six = ["Hello!"] * 7
for x in list_six:
    print(x)

# Length
print(len(list_six))





