'''
https://www.geeksforgeeks.org/problems/perfect-numbers3207/1
'''
# sum of all the factors excluding itself should be the same number 
# no perfect square is perfect number

# Solution 1-
# Time Complexity: 
# Space Complexity: 
def perfect_number_sqrt(n):
    total = 1                   # since 1 is also a factor 
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            total += i 
            if n // i != i:
                total += n // i
    if total == n :
        return f"{n} is a perfect number."


# Solution 2-
# Time Complexity: 
# Space Complexity: 
def perfect_number_sqr(n):
    total = 1                   # since 1 is also a factor 
    i = 2                  
    while i * i <= n:
        if n % i == 0:
            total += i 
        if n // i != i:
            total += n // i
        i += 1 
    if total == n :
        return f"{n} is a perfect number."


print(perfect_number_sqr(6))
print(perfect_number_sqrt(6))