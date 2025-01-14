
# A dictionary is a collection of multiple key value pairs, dicts are created using hash tables which help in fast access of values based on the keys.

# Two ways to create an empty dictionary
# Time Complexity- O(1)
# Space Complexity- O(1)     only memory for initial hash table structure is allocated hence space complexity is O(1)
 
empty_dict1= dict()
empty_dict2= {}
print(empty_dict1)
print(empty_dict2)

# When we the use dict constructor just provide the name of the keys- no need to specift "" even though it is a string and then = values, which should be specified properly, if str then " " else normally for num
# Time Complexity- O(n)     since each key and value pair needs to be inserted 
# Space Complexity- O(n)     
dict1 = dict(one= "English", two= "Spanish", three= "Dutch")
print(dict1)

# using curly braces
dict2 = {"one": "English", "two": "Spanish", "three": "Dutch"}
print(dict2)

# using list of tuples
# Time Complexity- O(n)     since each tuple should be processed and added to dict 
# Space Complexity- O(n)    and also to be stored in the memory
list_of_tuples = [("one", "English"), ("two", "Spanish"), ("three", "Dutch")]
print(dict(list_of_tuples))


'''
Dictionaries are indexed by keys.
Python dictionaries are implemented using hash tables, it is an array whose indexes are obtained using a hash function on the keys.

Passing the Key to the Hash Function:
    When you insert a key-value pair into a dictionary, Python's dict first passes the key through a hash function. This hash function generates a unique (or pseudo-unique) hash value for that key.
    Python's built-in hash() function is used to compute the hash value. For example:

    hash("apple")  # Might return a hash value like 123456789

Calculating the Hash Value and Index:
    The hash value returned by the hash function is then mapped to an index in the internal array. This is done by using the modulus operator to ensure the index is within the bounds of the array size.

    index = hash("apple") % table_size
    This index is where the key-value pair will be stored in the hash table (i.e., the internal array).

Storing the Key-Value Pair:
    If the computed index is empty, the key-value pair is directly inserted at that index.
    If the index is already occupied (due to a collision), Python's dict uses collision resolution techniques generally adds it to a linked list.  
        
'''

# Amortised?
# If we add pairs to the dict and the capacity of the dictionary is reached, the space allocated is doubled
