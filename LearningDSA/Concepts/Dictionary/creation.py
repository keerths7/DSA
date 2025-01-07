# it only creates the hash table but has no values in it 

# Two ways to create an empty dictionary
empty_dict1= dict()
empty_dict2= {}
print(empty_dict1)
print(empty_dict2)

dict1 = {one= "English", two= "Spanish", three= "Dutch"}
print(dict1)

dict2 = {"one": "English", "two": "Spanish", "three": "Dutch"}
print(dict2)

# Only memory for initial hash table structure is allocated hence space complexity is O(1)
# When we the use dict constructor just provide the name of the keys and then = values, which should be specified if str then " " else normally for num
# For n
# Since each key and value pair needs to be inserted the tc is O(n)
# Each of the tuple should be added to dict and time and space is hence O(n)
# Amortised?
# If we add pairs to the dict and the capacity of the dictionary is reached, the space allocated is doubled