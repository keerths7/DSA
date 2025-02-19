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
    print(i-1)

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

print(floor_sqrt(35))
print(floor_sqrt_binarysearch(35))