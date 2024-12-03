'''
Problem : Factorial of a number
'''
# Solution 1- Iterative approach
# Time Complexity: O(n)
# Space Complexity: O(1)

def factorial_iter(n):
    product = 1
    for i in range(2,n+1):
        product *= i
    return product


# Solution 2- Recursive approach
# Time Complexity: O(n)
# Space Complexity: O(n)

def factorial_recur(n):
    if n <= 1:
        return 1
    return n * factorial_recur(n-1)


n = int(input("Enter the number for which you would like to find Factorial: "))
print(factorial_iter(n))
print(factorial_recur(n))