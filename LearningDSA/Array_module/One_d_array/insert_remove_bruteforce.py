from array import *


def remove_ele(arr1, target_ele):
    for i in range(len(arr1)):
        if arr1[i] == target_ele:
            index = i

    for i in range(index, len(arr1) - 1):
        arr1[i] = arr1[i+1]
    
    return arr1[:-1]

    
arr1 = array('i', [1,2,3,4,5,6,7,8,9])
ele = 4
print(remove_ele(arr1, ele))


def insert_ele(arr1, index, ele):
    for i in range(len(arr1) - 1, index, -1):
        arr1[i] = arr1[i-1]
    print(arr1)
    arr1[index] = ele
    return arr1

index = 3
print(insert_ele(arr1, index, ele))
