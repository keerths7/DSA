'''
Problem: https://www.codingninjas.com/studio/problems/print-all-divisors-of-a-number_1164188
'''
# Time Complexity: O(n)
# Space Complexity: O(1)

def find_divisors(n):
    for i in range(1, n+1):
        if n % i == 0:
            print(i)

n = int(input("Enter any number:"))
find_divisors(n)