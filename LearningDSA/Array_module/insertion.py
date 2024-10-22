import array

# Time Complexity to create an array: O(n) - when we insert an element at a particular position, the time complexity depends on the number of elements that need to be shifted right
# Space Complexity to create an array: O(1) - when an element is inserted it only needs one amount of space

array = array.array('i', [1,2,3,4,5])
print(array)
array.insert(0, 6)   # index and value respectively
print(array)
array.insert(3, 7)
print(array)
array.insert(7, 8)
print(array)
array.insert(100, 9)  # index as 100 or any number greater than len-1, the element gets inserted at the end
print(array)