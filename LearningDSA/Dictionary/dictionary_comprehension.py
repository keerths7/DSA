# to create new dictionary from any iterable like a list or a dictionary 

# Syntax: new_dict = {new_key:new_value for item in list}
import random            # to generate random temperature values
city_names = ["Paris", "London", "New York", "Tokyo", "Delhi", "Mumbai", "Bangalore", "Chennai"]
city_temps = {city:random.randint(20,50) for city in city_names}
print(city_temps)

# Syntax for creating dict from existing dict, new_dict = {new_key:new_value for (key,value) in dict.items()}, we use items() method as it returns the key value pairs as tuples

# Syntax for creating dict from existing dict with filtering, new_dict = {new_key:new_value for (key,value) in dict.items() if condition}

above_30 = {city:temp for (city, temp) in city_temps.items() if temp>30}
print(above_30)


