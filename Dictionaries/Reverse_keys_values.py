'''
 Write a Python function reverse_dict(my_dict) that takes a dictionary as input and returns a new dictionary with its keys and values swapped.
'''

# Remember:  for x,y in my_dict.items():    my_dict[y] = x
# 🔴 Error: RuntimeError: dictionary changed size during iteration
# This happens because when we add a new key (y), Python modifies the dictionary while it is still being iterated, causing conflicts.

def reverse_keys_values(my_dict):
    reversed_dict = {}
    for x,y in my_dict.items():
        reversed_dict[y] = x
    return reversed_dict


def reverse_keys_values_compre(my_dict):
    return {y:x for x,y in my_dict.items()}


blue = {"name":"Amelia","age":12,"nationality":"British"}
print(reverse_keys_values(blue))
print(reverse_keys_values_compre(blue))
