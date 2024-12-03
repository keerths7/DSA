# To maintain the efficiency of random access, the elements must be stored in contiguous manner 

import array

# Time Complexity: O(n)
#`remove(1)` searches for the element `1` in the array
# After finding the element, all elements to the right are shifted one position to the left,
# which also takes O(n) time in the worst case if the element is at the start of the array.

# Space Complexity: O(1)

arr = array.array('i', [1,2,3,4,5,6,7])
arr.remove(1)
print(arr)