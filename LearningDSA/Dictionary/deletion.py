# del() method delets an element from a dictionary
my_dict = {"name": "Keerthana", "age": 23, "address": "India", "hobby": "reading"}
del my_dict
print(my_dict)

# clear() method removes all key-value pairs from the dictionary, it takes no params and returns None
my_dict = {"name": "Keerthana", "age": 23, "address": "India", "hobby": "reading"}
my_dict.clear()
print(my_dict)      # it will print {} as the dictionary is empty now

# pop(key, default_value) method removes the item with the specified key name and returns the value, if the key doesn't exist it returns the default value
my_dict = {"name": "Keerthana", "age": 23, "address": "India", "hobby": "reading"}
hobby = my_dict.pop("hobby")
print(hobby)
print(my_dict)
city = my_dict.pop("city", "not")
print(city)

# popitem() method returns and removes an arbitrary element from the dictionary, it doesn't take any parameter
my_dict = {"name": "Keerthana", "age": 23, "address": "India", "hobby": "reading"}
print(my_dict.popitem())
print(my_dict)      # we can see that the element it has deleted is missing from the dictionary
