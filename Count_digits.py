'''
Problem : Count the number of digits in a number
'''
# Solution 1- Using string conversion

def count_digits_stri(n):
    return len(str(n))

# Solution 2- Using division

def count_digits_div(n):
    count = 0
    while n > 0:
        n = n // 10 
        count += 1
    return count

n = int(input("Enter the number:"))
print(count_digits_stri(n))
print(count_digits_div(n))