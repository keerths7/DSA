'''
 Write a Python function reverse_dict(my_dict) that takes a dictionary as input and returns a new dictionary with the key value pairs reversed
'''

def reverse_dict(my_dict):
    return dict(reversed(list(my_dict.items())))


def reverse_dict(my_dict):
    return {key:value for key,value in reversed(list(my_dict.items()))}
        

blue = {"name":"Amelia","age":12,"nationality":"British"}
print(reverse_dict(blue))
print(reverse_dict(blue))