# Learning Data Structures - 2-D ARRAYS
# Two dimensional array is an array within an array. It is an array of arrays.
# In this type of array the position of an data element is referred by
# two indices instead of one. So it represents a table with rows and columns of
# data.

from array import *

array2d_one = [[22, 33, 44], [55, 66, 77, 88], [123, 456, 789]]

# Accessing values
print(array2d_one[0])
print(array2d_one[1][2])

for r in array2d_one:
    for c in r:
        print(c, end=" ")
    print()

# Inserting values
array2d_one.insert(1, [456, 567, 789])

for r in array2d_one:
    for c in r:
        print(c, end=" ")
    print()

# Updating values
array2d_one[2] = [999, 999, 999]
array2d_one[0][1] = 3333

# Deleting values
del array2d_one[0]

for r in array2d_one:
    for c in r:
        print(c, end=" ")
    print()
