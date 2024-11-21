'''
Problem: https://www.geeksforgeeks.org/problems/count-digits5716/1
'''
# Solution 1- Using logic
# Time Complexity: O(log(reversed(n)))
# Space Complexity: O(1)- no extra space used

def reversed_num_powered(num):
    reversed_num = 0
    num_var = num
    while num_var > 0:  # O(logn) time complexity
        reversed_num = reversed_num * 10 + num_var % 10 
        num_var = num_var // 10
    return num ** reversed_num  # O(log(reversed(n)) time complexity


num = int(input("Enter the number: "))
print(reversed_num_powered(num))
