'''

'''
def nth_armstrong(n):
    count = 0               # tracks the count of the numbers, adds the numbers that are armstrong starting from 1
    num = 1
    while count < n :
        n_digit = num
        n_count = num
        digit_count = 0
        total = 0
        while n_count > 0:
            n_count = n_count // 10
            digit_count += 1
        while n_digit > 0: 
            total += (n_digit % 10) ** digit_count
            n_digit = n_digit // 10
        if num == total:
            count += 1
        if count == n:
            return num
        num += 1


print(nth_armstrong(10))    