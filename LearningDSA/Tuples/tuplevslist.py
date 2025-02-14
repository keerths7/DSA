list1 = [0,1,2,3,4,5,6,7]

list1[1] = 3
print(list1)

list1 = [8,9,10,11,12]
print(list1)


# TypeError: 'tuple' object does not support item assignment
# tuple1 = 0,1,2,3,4,5,6,7
# tuple1[2] = 8
# print(tuple1)

# tuples are immutable, but we can reassign the variable to a new tuple.
tuple1 = 8,9,10,11,12
print(tuple1)

del list1[3]
print(list1)

# TypeError: 'tuple' object doesn't support item deletion
# del tuple1[3]
# print(tuple1)

# del list1
# print(list1)     # rasises NameError as list gets deleted 

# # Tuples are immutable, so individual elements cannot be deleted. 
# # However, the entire tuple can be removed using 'del', making it undefined.
# del tuple1
# print(tuple1)    # raises in NameError as tuple gets deleted 

# builtin methods like append(), insert(), remove(), pop(), clear(), sort(), reverse() can't be used for tuples


# using tuples will ensure that our data is write prtected

# since tuples contain immutable elements, it can be used as a key for dictionary 

# Tuples are generally used for homogeneous data (same type of elements),
# while lists are preferred for heterogeneous data (different types of elements).

# Iterating over tuple elements is generally faster than iterating over list elements 
# because tuples are immutable and more memory-efficient. 
# For performance-sensitive iterations, tuples can be a better choice when only iteration is involved.


# lists can be stored in tuples
list1 = [(1,2), (2,5), (6,7)]
tuple1 = ([1,2], [2,5], [6,7])
print(list1)
print(tuple1)

# we can create nested tuples just like nested lists 
nested_tuple = ((1,2), (2,5), (6,7))