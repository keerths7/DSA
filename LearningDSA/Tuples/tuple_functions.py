tuple1 = 1,2,3,4,5,6,1
tuple2 = 8,9,10,11,12

# The '+' operator concatenates two tuples, creating a new tuple with elements from both.
print(tuple1+tuple2)

# The '*' operator repeats the tuple multiple times, creating a new tuple with repeated elements.
print(tuple1*4)

print(len(tuple1))

print(tuple1.count(1))

print(tuple1.index(3))

print(min(tuple1))

print(max(tuple1))

# converting list to tuple 
list1 = [3,34,5,6,2]
print(tuple(list1))


# Time Complexity: O(n)     creating a single-element tuple (value,) takes O(1), tuple concatenation, (value,) + input_tuple, requires copying all n elements from input_tuple, so it takes O(n) time.
# Space Complexity: O(n)   a new tuple of size n+1 is created, which requires O(n) additional space.

def insert_at_beginning(input_tuple, value):
    return (value,) + input_tuple               # concatenates the tuples 

t1 = (3,34,5,6,20)
print(insert_at_beginning(t1, 6))