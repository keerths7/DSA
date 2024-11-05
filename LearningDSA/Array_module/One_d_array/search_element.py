# To search through an array using linear search, if we find the element(target value) we return the index of the element if not return -1

import array 

# Time Complexity: O(n)  we would have to search through the entire array to find the element    
# Space Complexity: O(1)


def search_element(arr1, target):
    for i in range(len(arr1)):
        if arr1[i] == target :
            return i
    return -1
    
    
arr1 = array.array('i', [1,2,3,4,5,6])
target = int(input("Enter the element to be searched: "))
print(search_element(arr1, target))