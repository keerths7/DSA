'''
Problem : Count the number of digits in a number
'''
# Solution 1- 
def count_digits_stri(n):
    return len(str(n))

# Solution 2-
def count_digits_remainder(n):
    count = 0
    while(n % 10 < 0):
        count += 1
    return count


n = int(input("Enter the number:"))
#print(count_digits_stri(n))
print(count_digits_remainder(n))