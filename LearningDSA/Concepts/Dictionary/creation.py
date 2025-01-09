
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


# Amortised?
# If we add pairs to the dict and the capacity of the dictionary is reached, the space allocated is doubled