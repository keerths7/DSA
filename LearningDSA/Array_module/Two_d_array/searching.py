import numpy as np

arr1 = np.array([[1, 2, 3, 4],[5, 6, 7, 8], [9, 10, 11, 12],[13, 14, 15, 16]])
print(arr1)

# Time Complexity: O(m*n) - considering the worst case
# Space Complexity: O(1) 

def search_2darray(arr1, target):
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            if arr1[i][j] == target:
                return i,j

print(search_2darray(arr1, 5))