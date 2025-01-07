def sum_factors_upto(n):
    sum = 1
    for i in range(2,n+1):
        for j in range(1,i+1):
            if i % j == 0:
                sum+= j
    return sum

print(sum_factors_upto(4))