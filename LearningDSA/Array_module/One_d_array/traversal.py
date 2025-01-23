# Traversal means to visit all elements of the array

import array

# Time Complexity: O(n)     since we have to traverse through each element in the array  
# Space Complexity: O(1)

def traversal(an_array):
    for i in an_array:
        print(i)

arr1 = array.array('i',[1,2,3,4,5])
traversal(arr1)