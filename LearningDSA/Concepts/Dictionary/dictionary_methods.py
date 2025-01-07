# clear() method removes all key-value pairs from the dictionary, it takes no params and returns None
my_dict = {"name": "Keerthana", "age": 23, "address": "India", "hobby": "reading"}
my_dict.clear()
print(my_dict)    # it will print {} as the dictionary is empty now


# copy() method returns a shallow copy of the dictionary, when the method is called it creates a new dictionary and copies the key-value pairs from the original dictionary to the new dictionary
my_dict = {"name": "Keerthana", "age": 23, "address": "India", "hobby": "reading"}
copied_dict = my_dict.copy()
print(copied_dict)   


# fromkeys() method takes two params keys and values, keys (keys can be any literable like list, tuple, set, str, etc.) is a mandatory param and values is an optional param and returns a dictionary with the specified keys and values, if values is not specified it will set the values to None
#  all the keys in the resulting dictionary are assigned the same reference to the value hence they hold the same value.
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

# pop() method removes the item with the specified key name and returns the value
