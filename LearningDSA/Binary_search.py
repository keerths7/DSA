'''
Problem : Binary Search
'''
# Solution 1- Iterative Approach
# Time Complexity: O(1)- when mid element is the element to be found, O(logn)
# Space Complexity: O(1)- no extra space used

def binary_search_iter(arr,ele,i,j):
    while i <= j:
        mid = i + (j - i) // 2  # Optimized way to calculate mid to prevent overflow that can occur with (i + j) / 2
        if arr[mid] == ele:
            return mid
        elif arr[mid] < ele:
            i = mid + 1
        else:
            j = mid - 1
    return -1

# Solution 2- Recursive Approach
# Time Complexity: O(1)- when mid element is the element to be found, O(logn)
# Space Complexity: O(log n) - due to the recursion call stack. As the search space is reduced by half with each recursive call, the recursion depth increases logarithmically- So even though the input size increased from 16 to 1024 (a 64x increase), the recursion depth only increased from 4 to 10 calls (a 2.5x increase). This is what we mean when we say that the recursion depth grows logarithmically.

def binary_search_recur(arr,ele,i,j):
    if i > j:
        return -1
    mid = i+(j-i)//2  # Optimized way to calculate mid to prevent overflow that can occur with (i + j) / 2
    if arr[mid] == ele:
        return mid
    elif arr[mid] < ele:
        return binary_search_recur(arr,ele,mid+1,j)
    else:
        return binary_search_recur(arr,ele,i,mid-1)
    

arr = [4,21,44,54,67,69,78,86,89,92,94,103,109,116]
i = 0
j = len(arr)-1
ele = int(input("Enter the element to be searched:"))
print(binary_search_iter(arr,ele,i,j))
print(binary_search_recur(arr,ele,i,j))