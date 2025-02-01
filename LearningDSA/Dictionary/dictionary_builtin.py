my_dict = {
    3 : "three",
    5 : "nine",
    9 : "nine",
    2 : "two",
    1 : "one",
    4 : "four"
}

# in operator in the dictionary
print(3 in my_dict)
print("three" in my_dict)           # the output is False here, which is incorrec, by default in operator works with the keys not the values, so to check for values
print("three" in my_dict.values())            # we can check the presence of a value in the dict using the values() method 

# similarly not in 
print(10 not in my_dict)
print("ten" not in my_dict) 

print(len(my_dict))                # len()returns the number of key-value pairs

print(all(my_dict))                # all() checks the keys of a dictionary and returns True if all keys are truthy. Keys are falsy if they are 0, "", None, or False. If even one key is falsy, all() will return False.
print(any(my_dict))                # any() checks the keys of a dictionary and returns True if at least one key is truthy. Keys are falsy if they are 0, "", None, or False. If all keys are falsy, any() will return False.