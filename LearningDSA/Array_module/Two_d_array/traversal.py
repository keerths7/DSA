import numpy as np

arr1 = np.array([[1,2,3,4,], [5,6,7,8], [9,10,11,12]])
print(arr1)

# Time Complexity: O(m*n)- The function traverses each element in the 2D array.   
# Space Complexity: O(1)

def traverse_2darr(arr1):
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            print(arr1[i][j])

print(traverse_2darr(arr1))