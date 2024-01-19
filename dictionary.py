# Learning Data Structures - DICTIONARY
# In Dictionary each key is separated from its value by a colon (:), the items
# are separated by commas, and the whole thing is enclosed in curly braces.
# An empty dictionary without any items is written with just two curly braces,
# like this − {}.
# Keys are unique within a dictionary while values may not be. The values of
# a dictionary can be of any type, but the keys must be of an immutable data
# type such as strings, numbers, or tuples.

dict_one = {"Name": "Joseph", "Age": 21, "Subject": "Mathematics"}

# Accessing values
print(f"dict_one['Name']: {dict_one['Name']}")

# Updating dictionary
dict_one['Age'] = 22
print(f"dict_one['Age']: {dict_one['Age']}")

# Delete dictionary elements
del dict_one['Subject']  # remove entry with key 'Subject'
dict_one.clear()         # remove all entries in dict_one
del dict_one             # delete entire dictionary



