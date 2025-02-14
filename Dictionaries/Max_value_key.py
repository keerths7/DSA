'''
 Write a Python function max_value_key(my_dict) that takes a dictionary as input and returns the key corresponding to the maximum value in the dictionary.
'''
# Solution 1- Iterating through loops
# Time Complexity: O(n) as the loop iterates through all the elements in the dict 
# Space Complexity: O(1) as no additional space is required 
def max_value_key(my_dict):
    max_val = float('-inf')     # initialize to the smallest possible value
    max_key = None
    for x,y in my_dict.items():
        if y > max_val:
            max_val  = y 
            max_key = x 
    return max_key


# This max() function finds the key in my_dict that has the highest value.
# max() iterates over the dictionary keys: ['a', 'b', 'c']
# The key parameter (my_dict.get) is used to extract values for each key.
#         - my_dict.get('a') → 10
#         - my_dict.get('b') → 25
#         - my_dict.get('c') → 5
# max() compares these extracted values and finds the highest one (25).
# The corresponding key ('b') is returned and stored in max_key.

# Solution 1- Iterating through loops
# Time Complexity: O(n) as the loop iterates through all the elements in the dict
# max() iterates over all keys in the dictionary → O(n)
# key=my_dict.get retrieves each value in O(1) time on average
# Since max() compares the values for all n keys, the total time complexity is O(n)
# Space Complexity: O(1) as no additional space is required 
def max_value_key_inbuilt(my_dict): 
    return max(my_dict, key= my_dict.get)

my_dict = {'a': 10, 'b': 25, 'c': 5}
print(max_value_key(my_dict))
print(max_value_key_inbuilt(my_dict))
