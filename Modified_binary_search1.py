'''
Problem : Modified Binary search- Find the position of the first infinite element when you are given a list of unsorted numbers with infinite elements at the last
'''
# Solution 1- Iterative Approach
# Time Complexity: O(1)- when mid element is the element to be found, O(logn)
# Space Complexity: O(1)- no extra space used

def modif_binary_search_iter(arr, ele, i, j):
    while i <= j:
        mid = i+(j-i)//2
        if i == j:
            return mid
        if arr[mid] != ele:
            i = mid + 1  # since we can understand from the hint that the infinite numbers start after the numbers
        elif arr[mid] == ele:
            j = mid - 1  # since we need to find the first infinite element
    return -1

# Solution 2- Recursive Approach
# Time Complexity: O(1)- when mid element is the element to be found, O(logn)
# Space Complexity: O(log n) - due to the recursion call stack. As the search space is reduced by half with each recursive call, the recursion depth increases logarithmically- So even though the input size increased from 16 to 1024 (a 64x increase), the recursion depth only increased from 4 to 10 calls (a 2.5x increase). This is what we mean when we say that the recursion depth grows logarithmically.

def modif_binary_search_recur(arr, ele, i, j):
    if i > j:
        return -1
    mid = i+(j-i)//2
    if i == j:
        return mid
    if arr[mid] != ele:
        return modif_binary_search_recur(arr, ele, mid+1, j)  # since we can understand from the hint that the infinite numbers start after the numbers
    elif arr[mid] == ele:
        return modif_binary_search_recur(arr, ele, i, mid-1) # since we need to find the first infinite element

arr = [-34, 7, 31, 4, 49, -34, 0, 345, -34, 88, 3, 13, -45, 33, float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf')]
i = 0
j = len(arr)- 1
ele = float('inf')
print(modif_binary_search_iter(arr, ele, i, j))
print(modif_binary_search_recur(arr, ele, i, j))