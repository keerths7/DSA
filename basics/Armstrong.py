'''
Problem: https://www.geeksforgeeks.org/problems/armstrong-numbers2727/1
'''

# Solution 1- Using all that we learnt with count and digit seperation
# Time Complexity: O(2logn)
# Space Complexity: O(1)- no extra space used

def find_armstrong(n):
    count = 0
    total = 0
    n_count = n
    while(n_count > 0):
        n_count = n_count // 10
        count += 1
    while(n > 0):
        total += (n % 10)**count
        n = n // 10
    if n == total:
        return True
    return False

print(find_armstrong(153))



