def filter_dict(my_dict):
    new_dict = {}
    for key, val in my_dict.items():
        if val % 2 == 0: 
            new_dict[key] = val
    return new_dict


def filter_dict_compre(my_dict):
    return {key:val for key,val in my_dict.items() if val % 2 == 0}

my_dict = {'a': 5, 'b': 10, 'c': 15, 'd': 20}
print(filter_dict(my_dict))
print(filter_dict_compre(my_dict))