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


def tuple_elementwise_sum(tuple1, tuple2): 
    if len(tuple1) != len(tuple2):
        raise ValueError("Check the length of the tuples to be equal.")
    sum = 0
    tuple3 = ()
    for i in range(len(tuple1)):
        sum = tuple1[i] + tuple2[i]
        tuple3 += (sum,)
    return tuple3

def tuple_elementwise_sum_zip(tuple1, tuple2):
    if len(tuple1) != len(tuple2):
        raise ValueError("Input tuples must have the same length.")
    result = tuple(a + b for a, b in zip(tuple1, tuple2))
    return result

def tuple_elementwise_sum_zip_map(tuple1, tuple2):
    return tuple(map(sum, zip(tuple1, tuple2)))

t1 = (1, 2, 3)
t2 = (4, 5, 6)
print(tuple_elementwise_sum(t1, t2))
print(tuple_elementwise_sum_zip(t1, t2))
print(tuple_elementwise_sum_zip_map(t1, t2))


def concatenate_strings(input_tuple):
    output_string = ""
    for i in input_tuple:
        output_string = output_string + i + " "
    return output_string.strip()

def concatenate_strings(input_tuple):
    return " ".join(input_tuple)
    
input_tuple = ("hi","hello","bonjour","vanakkam")
print(concatenate_strings(input_tuple))


def diagonal_tuple(matrix_tuple):
    if len(matrix_tuple) == len(matrix_tuple[0]):
        return matrix_tuple[0][0], matrix_tuple[1][1], matrix_tuple[2][2]
    return "diagonal matrix only applies to square matrices"

def diagonal_tuple_loop(matrix_tuple):
    diagonal_tuple = ()
    if len(matrix_tuple) == len(matrix_tuple[0]):
        for i in range(len(matrix_tuple)):
            diagonal_tuple += (matrix_tuple[i][i],)
        return diagonal_tuple
    return "diagonal matrix only applies to square matrices"

def diagonal_tuple_direct(matrix_tuple):
    if len(matrix_tuple) == len(matrix_tuple[0]):
        diagonal_tuple = tuple(matrix_tuple[i][i] for i in range(len(matrix_tuple)))
        return diagonal_tuple
    return "diagonal matrix only applies to square matrices"

matrix_tuple = ((1,2,3), (4,5,6), (7,8,9))
print(diagonal_tuple(matrix_tuple))
print(diagonal_tuple_loop(matrix_tuple))
print(diagonal_tuple_direct(matrix_tuple))


def common_elements(tuple1, tuple2):
    common_tuple = ()
    for i in tuple1:
        for j in tuple2:
            if i == j:
                common_tuple += (i, )
    return common_tuple

def common_elements_set(tuple1, tuple2):
    return tuple(set(tuple1) & set(tuple2))
    return tuple(set(tuple1).intersection(set(tuple2)))

tuple1 = (1,2,5,6,7,3)
tuple2 = (3,5,6,9,4,9,8,7)
print(common_elements(tuple1, tuple2))
print(common_elements_set(tuple1, tuple2))