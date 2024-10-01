'''
Problem: https://www.geeksforgeeks.org/problems/count-digits5716/1
'''
# Solution 1-
# Time Complexity: O(logn)- The number of digits k is proportional to log10(n), so we can say the time complexity is O(log n).
# Space Complexity: O(1)- no extra space used

def count_divisible_digits(n):
    count = 0
    n_var = n
    while n_var > 0:
        digit = n_var % 10
        if digit != 0 and n % digit == 0:
            count+=1
        n_var = n_var // 10
    return count

n = int(input("Enter any number:"))
print(count_divisible_digits(n))

# Solution 2-
# Time Complexity: O(logn)- The number of digits k is proportional to log10(n), so we can say the time complexity is O(log n).
# Space Complexity: O(logn)

def count_divisible_digits2(n):
    count = 0
    num_arr = list(str(n))
    for i in num_arr:
        if int(i) != 0 and n % int(i) == 0:
            count += 1
    return count

print(count_divisible_digits2(n))