'''
Problem : Addition of upto n numbers
'''
# Solution 1- Using Iterative Approach
# Time Complexity: O(n)
# Space Complexity: O(1)

def sum_iter(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum


# Solution 2- Using Recursion
# Time Complexity: O(n)
# Space Complexity: O(n)

def sum_recur(n):
    if n <= 0:
        return 0
    return n + sum_recur(n-1)

print(sum_iter(4))
print(sum_recur(4))