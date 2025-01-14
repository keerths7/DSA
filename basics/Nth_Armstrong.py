def nth_armstrong(nth):
    count = 0
    num = 1

    while count != nth:
        num_count = num
        num_digit = num
        digit_count = 0
        sum = 0

        while num_count > 0:
            num_count = num_count // 10
            digit_count += 1

        while num_digit > 0:
            digit = num_digit % 10
            sum += digit ** digit_count
            num_digit = num_digit // 10 

        if sum == num:
            count += 1

        num += 1  
                  
    return num-1

print(nth_armstrong(10))
