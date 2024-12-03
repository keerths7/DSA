'''
Problem: https://www.geeksforgeeks.org/problems/armstrong-numbers2727/1
'''

# Solution 1- Using all that we learnt with count and digit seperation
# Time Complexity: O(logn)  actually 2logn as we have 2 while loops
# Space Complexity: O(1)- no extra space used

def find_armstrong(n):
    count = 0
    total = 0
    n_count = n
    n_check = n
    while n_count > 0:
        n_count = n_count // 10
        count += 1
    while n > 0:
        total += (n % 10)**count
        n = n // 10
    return n_check == total

# Solution 2- Using str methods
# Time Complexity: O(logn)
# Space Complexity: O(logn) 

def find_armstrong_str(n):
    sum = 0
    for i in str(n):
        sum += int(i) ** len(str(n))
    return sum == n


print(find_armstrong(153))
print(find_armstrong_str(153))

