# Learning Data Structures - LINKED LISTS

# Linked Lists are a data structure that store data in the form of a chain.
# The structure of a linked list is such that each piece of data has
# a connection to the next one (and sometimes the previous data as well).
# Each element in a linked list is called a node.

# Advantages of Linked Lists:
# Because of the chain-like system of linked lists, you can add and remove
# elements quickly. This also doesn't require reorganizing the data structure
# unlike arrays or lists. Linear data structures are often easier to implement
# using linked lists. Linked lists also don't require a fixed size or initial
# size due to their chain like structure.

# Disadvantages of a Linked Lists:
# More memory is required when compared to an array. This is because you need
# a pointer (which takes up its own memory) to point you to the next element.
# Search operations on a linked list are very slow. Unlike an array, you don't
# have the option of random access

# When Should You Use a Linked List?
# You should use a linked list over an array when:
# You don't know how many items will be in the list (that is one of the
# advantages - ease of adding items).
# You don't need random access to any elements (unlike an array, you cannot
# access an element at a particular index in a linked list).
# You want to be able to insert items in the middle of the list.
# You need constant time insertion/deletion from the list (unlike an array,
# you don't have to shift every other item in the list first).

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head


