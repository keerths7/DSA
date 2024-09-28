'''
Problem : Finding the last digit in a number
'''
# Solution 1- using string conversion
# Time Complexity: O(k) - where k is the number of digits in the number which turns out to be O(logn)
# Space Complexity: O(k) - where k is the number of digits in the number which turns out to be O(logn)

def last_digit_stri(n):
    str_n = str(n)
    return str_n[-1]

# Solution 2- using remainder 
# Time Complexity: O(1)
# Space Complexity: O(1)- no extra space used

def last_digit_remainder(n):
    return n % 10

n = int(input("Enter a number:"))
print(last_digit_stri(n))
print(last_digit_remainder(n))