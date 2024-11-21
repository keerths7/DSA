'''
Problem: https://www.codingninjas.com/studio/problems/print-all-divisors-of-a-number_1164188
'''
import math

# Solution 1- Using brute force logic
# Time Complexity: O(n)
# Space Complexity: O(1)

def find_divisors(n):
    for i in range(1, n+1):
        if n % i == 0:
            print(i)

n = int(input("Enter any number:"))
find_divisors(n)

# Solution 2- Using
# Time Complexity: O(root(n))
# Space Complexity: O(1)
# Only checking until root(n)
# Conside 36: 1 x 36, 2 x 18, 3 x 12, 4 x 9, 6 x 6, 9 x 4, 12 x 3, 18 x 2, 36 x 1
# repeats after root of that number

sq_root = int(math.sqrt(n))
for i in range(1, sq_root+1):
    if n % i == 0:
        print(i)
        if i != n // i:
            print(n // i)
