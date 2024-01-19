# Learning Data Structures - SETS

# The elements in the set cannot be duplicates.
# The elements in the set are immutable(cannot be modified) but the set as a
# whole is mutable.
# There is no index attached to any element in a python set. So they do not
# support any indexing or slicing operation.

months = {"Jan", "Feb", "Mar", "Apr"}
days = {"Mon", "Tue", "Wed", "Thu"}

# Accessing values
for d in days:
    print(d)

# Adding items to a set
days.add("Fri")

# Removing item from a set
days.discard("Fri")

# Union of sets
days_a = {"Mon", "Tue", "Wed", "Thu"}
days_b = {"Fri", "Sat", "Sun"}
all_days = days_a | days_b
print(all_days)

# Intersection of sets
numbers_a = {22, 33, 44, 55}
numbers_b = {55, 66, 77, 88, 99}
numbers_c = numbers_a & numbers_b
print(numbers_c)

# Difference of sets
days_d = {"Mon", "Tue", "Wed"}
days_e = {"Wed", "Thu", "Fri", "Sat", "Sun"}
days_f = days_d - days_e
print(days_f)

# Compare sets
days_g = {"Mon", "Tue", "Wed"}
days_h = {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"}
subset_res = days_g <= days_h
superset_res = days_h >= days_g
print(subset_res)
print(superset_res)




