import numpy as np

arr1 = np.array([[1,2,3,4,], [5,6,7,8], [9,10,11,12]])
print(arr1)

# Time Complexity: O(m*n) - Creating a new array without the deleted row or column requires copying m*n elements.
# Space Complexity: O(m*n) - A new array is created to hold the result, which requires space proportional to the size of the original array.

deleted_row_arr1 = np.delete(arr1, 0, axis = 0)
print(deleted_row_arr1)

print(arr1)

deleted_column_arr1 = np.delete(arr1, 1, axis = 1)
print(deleted_column_arr1)