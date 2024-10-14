# Solution 1- Using slice method
# Time Complexity- O(nlogn)
# Space Complexity- O(n)

def third_largest_slice(arr):
    arr.sort()    # Python's sort methos Timsort has time complexity of O(nlogn) and space complexity is O(n) since a new sorted array of the same size n is created
    return arr[-3] 

arr = [23, 45, 67,1,678,28,34,8,62,43]
print(third_largest_slice(arr))

# Solution 2- Using 
# Time Complexity- 
# Space Complexity- 

def third_largest_slice(arr):
    arr