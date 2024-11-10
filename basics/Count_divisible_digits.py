'''
Problem: https://www.geeksforgeeks.org/problems/count-digits5716/1
'''
# Solution 1- Using logic
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


# Solution 2- Using string method
# Time Complexity: O(logn)- The number of digits k is proportional to log10(n), so we can say the time complexity is O(log n).
# Space Complexity: O(logn)

def count_divisible_digits_str(n):
    count = 0
    n_str = str(n)
    for i in n_str:
        if int(i) != 0 and n % int(i) == 0:
            count += 1
    return count


# Solution 3- Using arr
# Time Complexity: O(logn)- The number of digits k is proportional to log10(n), so we can say the time complexity is O(log n).
# Space Complexity: O(logn)

def count_divisible_digits_arr(n):
    arr = [0] * 10
    sum = 0
    n_str = str(n)
    for i in n_str:   # O(logn) time and space complexity for converting n to str
        if int(i) != 0 and n % int(i) == 0:
            arr[int(i)] += 1
    for i in range(len(arr)):
        if arr[i] > 0:
            sum += arr[i]
    return sum


# Solution 4- Using logic, recursively
# Time Complexity: O(logn)- The number of digits k is proportional to log10(n), so we can say the time complexity is O(log n).
# Space Complexity: O(logn)

def count_divisible_digits_recur(n):
    if n <= 0:
        return 0
    if n % 10 != 0 and n % (n % 10) == 0:
        return 1 + count_divisible_digits_recur(n//10)


n = int(input("Enter any number:"))
print(count_divisible_digits(n))
print(count_divisible_digits_str(n))
print(count_divisible_digits_arr(n))
print(count_divisible_digits_recur(n))
