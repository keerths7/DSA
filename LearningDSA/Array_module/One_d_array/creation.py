'''
 When you create an array, it stores something called as meta data which is consits of the data type, length etc.
 Array module is a part of standard python library hence no additional installation is required
 Arrays created using array module are homogeneous, meaning their elements must be of same data type
 When creating elements of same data type array is preferred over lists as it is memory efficient
'''

import array

# Time Complexity to create an empty array: O(1)  
# Space Complexity to create an empty array: O(1)

arr = array.array('i', [])  # it doesn't store reference to any memory block since it is an empty array, it only stores meta data information
print(arr)

# Time Complexity to create an array: O(n)  since it involves copying the array to the referenced array
# Space Complexity to create an array: O(n) 

arr1 = array.array('i', [1,2,3,4]) # when you create an array with elements in it, a contiguous block of memory is allocated to store the array elements
print(arr1)


'''
Similar to array module arrays, numpy array created using array module are homogeneous, meaning their elements must be of same data type.
Numpy module is not a part of standard python library hence additional installation is required
'''

import numpy as np

# Time Complexity to create an empty array: O(1)  
# Space Complexity to create an empty array: O(1)

np_array = np.array([], dtype = int)
print(np_array)

# Time Complexity to create an array: O(n)  since it involves copying the array elements to the referenced array
# Space Complexity to create an array: O(n)  for memory allocation

np_array1 = np.array([1,2,3,4,5]) 
print(np_array1)