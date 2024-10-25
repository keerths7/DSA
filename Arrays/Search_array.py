'''
https://www.geeksforgeeks.org/problems/search-an-element-in-an-array-1587115621/1
'''
# Solution 1- Using built-in in operator
# Time Complexity: O(n)
# Space Complexity: O(1)- since no extra space used

def array_search(arr, ele):
    if ele in arr:
        return arr.index(ele)
    return -1

# Solution 2- using linear search
# Time Complexity: O(n)
# Space Complexity: O(1)- since no extra space used

def array_search_linear(arr, ele):
    for i in range(len(arr)):
        if arr[i] == ele:
            return i
    return -1

# We can also use binary search after sorting the array to find the element
# refer to ./Binary_search.py

arr = [3, 5, 6, 8, 9]
ele = int(input("Enter an element to search in the array: "))
