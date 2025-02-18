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
# Space Complexity: O(n)    a new tuple of size n+1 is created, which requires O(n) additional space.

def insert_at_beginning(input_tuple, value):
    return (value,) + input_tuple               # concatenates the tuples 

t1 = (3,34,5,6,2)
print(insert_at_beginning(t1, 6))


def tuple_elementwise_sum(): 
    if len(tuple1) != len(tuple2):
        raise ValueError("Check the length of the tuples to be equal.")
    sum = 0
    tuple3 = ()
    for i in tuple1, tuple2:
        sum = tuple1[i] + tuple[i]
        tuple3.append(sum)
    return tuple3


def tuple_elementwise_sum(t1, t2):
    if len(t1) != len(t2):
        raise ValueError("Input tuples must have the same length.")

    result = tuple(a + b for a, b in zip(t1, t2))
    return result


def tuple_elementwise_sum(tuple1, tuple2):
    return tuple(map(sum, zip(tuple1, tuple2)))

t1 = (1, 2, 3)
t2 = (4, 5, 6)
print(tuple_elementwise_sum(t1, t2))
    


