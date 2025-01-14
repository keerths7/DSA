'''
https://www.geeksforgeeks.org/problems/prime-number2314/1
'''
import math

# Solution 1- Bruteforce
# Time Complexity- O(n)
# Space Complexity- O(1)

def prime_num_bruteforce(n):
    for i in range(2,n):
        if n % i == 0:
            return 0
    return 1


# Solution 2- Taking only upto sqrt
# Time Complexity- O(root(n))
# Space Complexity- O(1)
def prime_num_sqrt(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return 0
    return 1

'''
We know that any integer number can be written in the form of 6k+i, where k is a nonnegative integer (like 0, 1, 2, 3,…) and i is a number between 0 and 5 (so i can be 0, 1, 2, 3, 4, or 5). If we look closely, we’ll notice that when i is 0, 2, 3, or 4, the numbers 6k, 6k+2, 6k+3, and 6k+4 are all divisible by either 2 or 3. But prime numbers greater than 3 can’t be divisible by 2 or 3. Therefore, the only forms left that a prime number can have are 6k+1 or 6k+5 (since these forms are not divisible by 2 or 3).
Instead of checking every number up to the √n to see if it divides n, we only check numbers of the form 6k+1 and 6k+5. This reduces the number of checks needed.
'''

# Solution 3- Optimised Trial division method
# Time Complexity- 
# Space Complexity- O(1)

def optimised_trial_division(n):
    if n <= 1:
        return 0

    if n == 2 or n == 3:
        return 1

    if n % 2 == 0 or n % 3 == 0:
        return 0
    
    i = 5
    # from 5 to sqrt of the number
    while i <= math.sqrt(n):
        if n % i == 0 or n % (i+2):
            return 0
        i += 6
    return 1


n = int(input("Enter the number:"))
print(prime_num_bruteforce(n))
print(prime_num_sqrt(n))
print(sixiplusk(n))