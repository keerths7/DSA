'''
Problem: https://www.geeksforgeeks.org/problems/count-digits5716/1
'''
# Time Complexity: O(logn)- , The number of digits k is proportional to log10(n), so we can say the time complexity is O(log n).
# Space Complexity: O(1)- no extra space used

def count_divisible_digits(n):
    count = 0
    n_var = n
    while(n_var > 0):
        if n % (n_var % 10) == 0:
            count+=1
        n_var = n_var // 10
    return count

print(count_divisible_digits(12))
