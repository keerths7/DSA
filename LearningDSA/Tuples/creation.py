# tuples are immutable
# it is advisable to put tuples in a () to indentify it easily, but it is not mandatory

# Time Complexity: O(n)   since it involves copying the tuple elements to the referenced tuple
# Space Complexity : O(n)  for memory allocation

tuple1 = ('a','b','c','d')

# when creating a tuple with one element we should put a comma after the element, otherwise python thinks it is a string with parenthesis,l try printing just like this ('a') to understand the difference. 
tuple2 = ('a',)

print(tuple1)
print(tuple2)

# creating a tuple with built-in tuple() function
tuple3 = tuple()
print(tuple3)

# each character will be a seperater element in the tuple
tuple3 = tuple('abcde')
print(tuple3)
