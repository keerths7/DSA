
# A dictionary is a collection of multiple key value pairs, dicts are created using hash tables which help in fast access of values based on the keys.

# Two ways to create an empty dictionary
# Time Complexity- O(1)
# Space Complexity- O(1)     only memory for initial hash table structure is allocated hence space complexity is O(1)
 
empty_dict1= dict()
empty_dict2= {}
print(empty_dict1)
print(empty_dict2)

# When we the use dict constructor just provide the name of the keys- no need to specify "" even though it is a string and then = values, which should be specified properly, if str then " " else normally for num
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
Dictionaries in Python are indexed by keys and are implemented using hash tables. 
A hash table is an array of buckets, where each bucket stores key-value pairs. The index of each bucket is determined by a hash function applied to the keys.
---
Passing the Key to the Hash Function:
When you insert a key-value pair into a dictionary, Python's dict first passes the key through a hash function.
This hash function generates a hash value (a unique or pseudo-unique integer).
Python uses its built-in hash() function for this computation.
hash("apple")  # Might return a hash value like 123456789
---
Calculating the Hash Value and Determining the Bucket (Indexing Process):
The hash value returned by the hash function is then mapped to an index in the internal array of buckets.
This is done using the modulus operator to ensure the index is within the bounds of the array size:
index = hash("apple") % table_size
The bucket at this index is where the key-value pair is stored.
---
Storing the Key-Value Pair in a Bucket:
Each bucket in the dictionary stores one or more key-value pairs.
If the computed bucket is empty, the key-value pair is directly inserted into that bucket.
If the bucket is already occupied (collision occurs), Python resolves the collision using open addressing (probing) or linked lists (depending on the implementation).     


Example:
Without collision:
my_dict = {"name": "Alice", "age": 25}
# Suppose hash("name") → Bucket 2
# Suppose hash("age") → Bucket 5

Hash Table (Buckets)
---------------------
Index | Value
------|-----------------
  2   | ("name", "Alice")
  5   | ("age", 25)

  
With collision:
my_dict = {"name": "Alice", "age": 25, "city": "Chennai"}
# Suppose hash("name") → Bucket 2
# Suppose hash("age") → Bucket 5
# Suppose hash("city") → Bucket 2 (Collision!)

Hash Table (Buckets)
---------------------
Index | Value
------|-----------------
  2   | ("name", "Alice") → ("city", "Chennai")  # Collision handled via chaining
  5   | ("age", 25)

'''