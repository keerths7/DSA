# the tuple elements will be placed adjacent to each other in the memory  

# Time complexity: O(n), accessing a tuple element (list[i]) has O(1) time complexity since tuples are stored contiguously in memory, allowing direct access.  
# Space complexity: O(1), because accessing an element does not require extra memory allocation.  

# tuples can be accessed just like lists
tuple1 = ('a','b','c','d','e')

print(tuple1[0])    
print(tuple1[-1])   # using negative index
print(tuple1[1:3])  # using slice operator

# tuples can be accessed but not be modified as they are immutable
# tuple1[0] = 'z'