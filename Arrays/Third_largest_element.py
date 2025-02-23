'''
https://www.geeksforgeeks.org/problems/third-largest-element/1
'''

# Solution 1- Using slice method
# Time Complexity- O(nlogn)
# Space Complexity- O(n)

def third_largest_slice(arr):
    arr.sort()    # Python's sort methos Timsort has time complexity of O(nlogn) and space complexity is O(n) since a new sorted array of the same size n is created
    return arr[-3] 


# Solution 2- Using multiple loops
# Time Complexity- 
# Space Complexity- 
def third_largest_loops(arr):
    first = float("-inf")
    for i in arr:
        if i > first:
            first = i 
    second = float("-inf")
    for i in arr:
        if i > second  and i < first:
            second = i
    third = float("-inf") 
    for i in arr:
        if i > third and i < second:
            third = i 
    return third


# Solution 3- Using a single loop
# Time Complexity- 
# Space Complexity- 
def third_largest_loop_conditional(arr):
    first, second, third = float("-inf"), float("-inf"), float("-inf")
    for i in arr:
        if i > first:
            third = second
            second = first
            first = i 
        elif i > second:
            third = second
            second = i
        elif i > third:
            third = i 
    return third

arr = [23,45,67,1,678,28,34,8,62,43]
print(third_largest_slice(arr))
print(third_largest_loops(arr))
print(third_largest_loop_conditional(arr))
