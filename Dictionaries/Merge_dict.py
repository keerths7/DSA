'''
Write a Python function to merge two dictionaries by adding values of matching keys.
'''

dict1 = {'car': 3, 'cat': 1, 'bat': 2, 'goat': 1}
dict2 = {'apple': 2,'car': 3, 'lemon': 3, 'goat': 1}

merged_dict = dict1.copy()
for i in dict2:
    if i in merged_dict:
        merged_dict[i] += dict2[i]
    else:
        merged_dict[i] = dict2[i] 
    
print(merged_dict)


# using .items()
merged_dict = dict1.copy()
for x,y in dict2.items():
    if x in merged_dict:
        merged_dict[x] += y 
    else:
        merged_dict[x] = y 
print(merged_dict)


# using .get()
merged_dict = dict1.copy()
for x,y in dict2.items():
    merged_dict[x] = merged_dict.get(x,0) + y 
print(merged_dict)