# Accessing array element based on index

import array

# Time Complexity: O(1)     
# This is because array elements are stored in contiguous memory locations,
# so the program can compute the exact location of an element with a simple calculation.
# Space Complexity: O(1)

def access_array_element(arr, index):
    if index >= len(arr):
        print("There is no element with this index.")
    print(arr[index])

arr = array.array('i', [1,2,3,4,5,6,7,8])
index =int(input("Enter index:"))
access_array_element(arr,index)