'''
https://www.geeksforgeeks.org/problems/square-root/1
'''

# Solution 1- Brute Force
# Time Complexity: O(sqrtn)
# Space Complexity: O(1)
def floor_sqrt(n):
    i = 1
    while i * i <= n:
        i += 1 
    return i-1

# Solution 2- Binary Search
# Time Complexity: O(log n)
# Space Complexity: O(1)
# high always holds the largest integer whose square is ≤ n
def floor_sqrt_binarysearch(n):
    low = 1
    high = n
    mid = 0
    while low <= high:
        mid = low + (high-low) // 2 
        if mid*mid == n:
            return mid
        if mid * mid < n:
            low = mid + 1 
        else:
            high = mid - 1    
    return high

# Solution 2- Binary Search using recursion
# Time Complexity: O(logn)
# Space Complexity: O(logn)
# high always holds the largest integer whose square is ≤ n
def floor_sqrt_binarysearch_recur(low, high, n):
    if low > high:
        return high
    mid = (low + high) // 2
    if mid * mid == n: 
        return mid
    elif mid * mid > n:
        return floor_sqrt_binarysearch_recur(low, mid-1, n)
    else:
        return floor_sqrt_binarysearch_recur(mid+1, high, n)
    

print(floor_sqrt(35))
print(floor_sqrt_binarysearch(35))
print(floor_sqrt_binarysearch_recur(0, 35, 35))