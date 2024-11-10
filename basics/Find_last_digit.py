'''
Problem : Finding the last digit in a number
'''
# Solution 1- using string conversion
# Time Complexity: O(logn), The number of digits k is proportional to log10(n), so we can say the time complexity is O(log n).
# Space Complexity: O(logn), because the string representation of the number requires space proportional to the number of digits (log10 n).

def last_digit_stri(n):
    str_n = str(n) # to convert the number into str we need time ans spacd as O(k) where k is number of digits in the number n, we can calculate k by this- say our n is 8767, so to reach that 10 power how much should you go 10 power k right, taking log on both sides, log n =  log 10**k, we get k as log 10 n
    return str_n[-1]

# Solution 2- using remainder 
# Time Complexity: O(1)
# Space Complexity: O(1)- no extra space used

def last_digit_remainder(n):
    if n > 0:
        return n % 10
    elif n == 0:
        return 0
    else:
        return abs(n) % 10

n = int(input("Enter a number:"))
print(last_digit_stri(n))
print(last_digit_remainder(n))