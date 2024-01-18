from array import *

array_one = array('i', [11, 22, 33, 44, 55, 66, 77, 88, 99])

for x in array_one:
    print(x)

# Accessing array elements
print(array_one[0])
print(array_one[1])

# Insertion operation
array_one.insert(0, 99)
# Deletion operation
array_one.remove(44)

for x in array_one:
    print(x)

# Search operation
print(array_one.index(77))
# Update operation
array_one[3] = 45

