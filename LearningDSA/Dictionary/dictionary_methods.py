# clear() method removes all key-value pairs from the dictionary, it takes no params and returns None
my_dict = {"name": "Keerthana", "age": 23, "address": "India", "hobby": "reading"}
my_dict.clear()
print(my_dict)    # it will print {} as the dictionary is empty now

# copy() method returns a shallow copy of the dictionary, when the method is called it creates a new dictionary and copies the key-value pairs from the original dictionary to the new dictionary
my_dict = {"name": "Keerthana", "age": 23, "address": "India", "hobby": "reading"}
copied_dict = my_dict.copy()
print(copied_dict)   

# fromkeys() method takes two params keys and values, keys (keys can be any literable like list, tuple, set, str, etc.) is a mandatory param and values is an optional param and returns a dictionary with the specified keys and values, if values is not specified it will set the values to None
# all the keys in the resulting dictionary are assigned the same reference to the value hence they hold the same value.
keys = ['name', 'age', 'address', 'hobby']
new_dict = dict.fromkeys(keys)
print(new_dict)    

keys = ['name', 'age', 'address', 'hobby']
values = "unknown"
new_dict = dict.fromkeys(keys, values)
print(new_dict) 

# get() method returns the value of the specified key
my_dict = {"name": "Keerthana", "age": 23, "address": "India", "hobby": "reading"}
print(my_dict.get("name"))  
# if we don't specify the second param and the key does not exist it will return None
print(my_dict.get("city"))  
# it takes another optional param which is the value to be returned if the key does not exist
print(my_dict.get("city", "unknown"))   
    
# items() method returns a view object that displays a list of a dictionary's key-value tuple pairs
my_dict = {"name": "Keerthana", "age": 23, "address": "India", "hobby": "reading"}
print(my_dict.items())

# keys() method returns a view object that displays a list of a dictionary's keys
my_dict = {"name": "Keerthana", "age": 23, "address": "India", "hobby": "reading"}
print(my_dict.keys())

# popitem() method returns and removes an arbitrary element from the dictionary, it doesn't take any parameter
my_dict = {"name": "Keerthana", "age": 23, "address": "India", "hobby": "reading"}
print(my_dict.popitem())
print(my_dict)      # we can see that the element it has deleted is missing from the dictionary

# setdefault(key, default_value) method, takaes two params key and default value which is optional, returns value from the key if the key is in the dictionary, else it inserts the key with a value to the dictionary and returns the default value if it is specified else it returns None
my_dict = {"name": "Keerthana", "age": 23, "address": "India", "hobby": "reading"}
print(my_dict.setdefault("age"))
# print(my_dict)
print(my_dict.setdefault("age", "immortal"))    # if age key exists already it directly returns its value, only if the key doesn't exist it adds that key value pair to the dict
# print(my_dict)
print(my_dict.setdefault("lunch"))              # without a default value
print(my_dict)
print(my_dict.setdefault("city", "Neighbourhood"))
print(my_dict)

# pop(key, default_value) method removes the item with the specified key name and returns the value, if the key doesn't exist it returns the default value
my_dict = {"name": "Keerthana", "age": 23, "address": "India", "hobby": "reading"}
hobby = my_dict.pop("hobby")
print(hobby)
print(my_dict)
city = my_dict.pop("city", "not")
print(city)

# values() returns a view object that displays list of values in the dictionary, it doesn't take any params
my_dict = {"name": "Keerthana", "age": 23, "address": "India", "hobby": "reading"}
print(my_dict.values())

# update(other_dictionary or iterable) updates the dictionary with key-value pairs from another dictionary or an iterable (like tuples).
# If a key is not already present in the dictionary, it will be added.
my_dict = {"name": "Keerthana", "age": 23, "address": "India", "hobby": "reading"}
new_dict = {"a":1, "b":2, "c":3}
print(my_dict)

# If the key exists, its value will be updated with the new value.
my_dict = {"name": "Keerthana", "age": 23, "address": "India", "hobby": "reading"}
new_dict = {"name":"Keerthi", "age": 16, "c":3}
print(my_dict)

# If called without any parameters, the method does nothing
my_dict = {"name": "Keerthana", "age": 23, "address": "India", "hobby": "reading"}
my_dict.update()
print(my_dict)

# so using update we can take a dict and put it in another dict