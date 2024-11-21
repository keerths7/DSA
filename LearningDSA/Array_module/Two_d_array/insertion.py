import numpy as np

arr1 = np.array([[1, 2, 3, 4],[5, 6, 7, 8], [9, 10, 11, 12],[13, 14, 15, 16]])
print(arr1)

# Inserting a row or column involves creating a new array, copying all m * n elements from the original array, and adding either m or n new elements, resulting in both time and space complexities of O(m * n).
# you would have to move n number of elements m times down
# Time Complexity- O(m*n)
# Space Complexity: O(m*n)

inserted_row_arr1 = np.insert(arr1, 0, [17,18,19,20], axis = 0)
print(inserted_row_arr1)

# Inserting a row or column involves creating a new array, copying all m * n elements from the original array, and adding either m or n new elements, resulting in both time and space complexities of O(m * n).
# you would have to move m number of elements n number of times to the right
# Time Complesity : O(m*n)
# Space Complexity: O(m*n)

inserted_column_arr1 = np.insert(arr1, 0, [21,22,23,23], axis = 1)
print(inserted_column_arr1)