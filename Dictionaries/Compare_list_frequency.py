'''
Write a Python function check_same_frequency(list1, list2) that checks whether two given lists have the same frequency of elements, regardless of order.
'''

def check_same_frequency(list1,list2):
    dict1, dict2 = {}, {}
    for i in list1:                         # O(n)
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    for i in list2:                          # O(n)
        if i in dict2:
            dict2[i] += 1
        else:
            dict2[i] = 1
    if dict1 == dict2:                       # O(n)
        print(dict1, dict2, sep = "\n")
        return True
    return False

list1 = [1,2,3,3,1,2,1,4,5,4,3]
list2 = [2,2,3,1,3,1,1,3,4,4,5]
print(check_same_frequency(list1,list2))