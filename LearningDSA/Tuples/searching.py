tuple1 = ('a','b','c','d','e')

# using in operator 
# Time Complexity: O(n)   in operator searches through all the elements in the tuple
# Space Complexity : O(1)  
print('a' in tuple1)
# print("f" in tuple1)

# using index method- it returns the index of the element
# Time Complexity: O(n)    .index() method scans the tuple sequentially until it finds the element, making it linear in time.
# Space Complexity : O(1) 
print(tuple1.index("c"))
print(tuple1.index("e"))
# print(tuple1.index("f"))

# using custom function 
# Time Complexity: O(n)     since we are searching through all the elements in the tuple 
# Space Complexity : O(1) 
def search_tuple(tuple1, target):
    for i in range(len(tuple1)):
        if tuple1[i] == target:
            return f"The element is at {i} index"
    return -1

target = 'c'
print(search_tuple(tuple1, target))


# In tuples and lists, the .index() method loops through all elements from index 0 onward and stops as soon as it finds the target element, returning its index.
# In dictionaries, searching for a key by value requires comparing each key-value pair until a match is found, making it O(n).  
