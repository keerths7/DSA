import numpy as np

arr1 = np.array([[1,2,3,4,], [5,6,7,8], [9,10,11,12]])
print(arr1)

# Time Complexity: O(1)     
# This is because array elements are stored in contiguous memory locations,
# so the program can compute the exact location of an element
# Space Complexity: O(1)

def access_2darr_element(arr, row_index, column_index):
    if row_index >= len(arr1) or column_index >= len(arr1[0]):
        return "Check the row and column index"
    return arr[row_index] [column_index]

row_index = int(input("Enter row index: "))
column_index = int(input("Enter column index: "))

print(access_2darr_element(arr1, row_index, column_index))