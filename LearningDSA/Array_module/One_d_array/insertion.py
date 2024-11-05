# To insert element in a given position in an array

import array
# Time Complexity: O(n) - when we insert an element at a particular position, the time complexity depends on the number of elements that need to be shifted right, O(n)(worst case) if the element is to be inserted at 0th index
# Space Complexity: O(1) - when an element is inserted it only needs one amount of space

array1 = array.array('i', [1,2,3,4,5])
print(array1)
array1.insert(0, 6)   # index and value respectively
print(array1)
array1.insert(3, 7)
print(array1)
array1.insert(7, 8)
print(array1)
array1.insert(100, 9)  # index as 100 or any number greater than len-1, the element gets inserted at the end
print(array1)