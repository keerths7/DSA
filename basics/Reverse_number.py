'''
Problem : Reverse a number
'''
# Solution 1- String conversion and reversal
# Time Complexity: O(logn), The number of digits k is proportional to log10(n), so we can say the time complexity is O(log n).
# Space Complexity: O(logn), because the string representation of the number requires space proportional to the number of digits (log10 n).

def num_reversal_stri(num):
    num_to_stri = str(num) # to convert the number into str we need time ans space as O(k) where k is number of digits in the number n, we can calculate k by this- say our n is 8767, so to reach that 10 power how much should you go 10 power k right, taking log on both sides, log n =  log 10**k, we get k as log 10 n  
    return int(num_to_stri[::-1])  # using step in slicing, it steps from reverse, similarly for this also the time and space complexity is O(logn)


# Solution 2- shifting the numbers by reminder and division method,
# Time Complexity: O(1)
# Space Complexity: O(1)- no extra space used

def num_reversal_remdiv(num):
    reversed_num = 0
    while num > 0:
        reversed_num = reversed_num * 10  + num % 10
        num = num // 10
    return int(reversed_num)


# Solution 3- My solution
# Time Complexity: O((logn)**2) due to the string concat logic I proudly thought of 
# Space Complexity: O(logn) because the string representation of the number requires space proportional to the number of digits (log10 n)

def num_reversal_remdiv_str(num):
    reversed_num = ""
    while num > 0: 
        reversed_num += str(num % 10) # each time to concat str, O(1) + O(2) + O(3).... + O(k), where k is no. of digits in the num, is k(k+1)/2 which is O(log**2n)- oh, god, Str concat is risky business
        num = num // 10
    return int(reversed_num) # similarly to convert str to int, the time complexity is O(logn) but space complexity for this is is O(1) only


# Solution 4- shifting the numbers by reminder and division method recuriviely
# Time Complexity: O(logn)
# Space Complexity: O(logn)- no extra space used

def num_reversal_recur(num, reversed = 0):
    if num <= 0:
        return reversed
    reversed = reversed * 10 + (num % 10)
    return num_reversal_recur(num//10, reversed)


num = int(input("Enter number of your choice:"))
print(num_reversal_remdiv(num))
print(num_reversal_stri(num))
print(num_reversal_remdiv_str(num))
print(num_reversal_recur(num))