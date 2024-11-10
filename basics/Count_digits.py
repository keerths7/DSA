'''
Problem : Count the number of digits in a number
'''
# Solution 1- Using string conversion

# The len() function in Python operates in O(1) time when applied to a string. This is because Python strings internally store their length, so the length can be accessed directly without iterating through the string.
# Time Complexity: O(logn), The number of digits k is proportional to log10(n), so we can say the time complexity is O(log n).
# Space Complexity: O(logn), because the string representation of the number requires space proportional to the number of digits (log10 n).

def count_digits_stri(n):
    return len(str(n)) # to convert the number into str we need time and space as O(k) where k is number of digits in the number n, we can calculate k by this- say our n is 8767, so to reach that 10 power how much should you go 10 power k right, taking log on both sides, log n =  log 10**k, we get k as log 10 n  


# Solution 2- Using division
# Time complexity: O(logn)- The number of digits k is proportional to log10(n), so we can say the time complexity is O(log n).
# Space complexity: O(1) as no extra space is used

def count_digits_div(n):
    count = 0
    while n > 0:
        n = n // 10 
        count += 1
    return count

# Solution 3- Using division recursion
# Time complexity: O(logn)- The number of digits k is proportional to log10(n), so we can say the time complexity is O(log n).
# Space complexity: O(logn) 

def count_digits_div_recur(n):
    if n <= 0:
        return 0
    return 1 + count_digits_div_recur(n//10)

n = int(input("Enter the number:"))
print(count_digits_stri(n))
print(count_digits_div(n))
print(count_digits_div_recur(n))
