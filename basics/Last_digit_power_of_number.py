'''
Problem: https://www.geeksforgeeks.org/problems/find-last-digit-of-ab-for-large-numbers1936/1
'''
# Solution 1- Using built in function
# Time Complexity- O(log(pow))
# Space Complexity- O(1)

def power_num_direct(n, pow):
    return (n ** pow) % 10

# Solution 2- Using logic
# Time Complexity- O(1)  
# Space Complexity- O(1)
# Max cycle length is 4, hence O(4) which is constant

def power_num(n, pow):
    last_digit_cycle = []
    last_digit = n % 10
    if pow == 0:
        return 1
    current_digit = last_digit
    while current_digit not in last_digit_cycle:
        last_digit_cycle.append(current_digit)
        current_digit = (current_digit * last_digit) % 10
    pow = pow % len(last_digit_cycle)
    return last_digit_cycle[pow - 1]


n = int(input("Enter a number:"))
pow = int(input("Enter the power:"))
print(power_num_direct(n, pow))
print(power_num(n, pow))

# Extra notes
# More notes wrt first Solution
# Naive approach for exponentiation (n ** pow):
# - Time Complexity: O(pow)
# - Simply multiply 'n' by itself 'pow' times.
# - For example, to compute 2 ** 10, it performs 9 multiplications.
# - This is fine for small exponents but becomes inefficient for large powers.

# Exponentiation by Squaring:
# - Time Complexity: O(log(pow))
# - More efficient algorithm that reduces the number of multiplications by halving the exponent.
# - If the exponent is even, we use the identity: (n ** pow) = (n ** (pow // 2)) ** 2.
# - If the exponent is odd, we use: (n ** pow) = n * (n ** (pow - 1)).
# - For example, to compute 2 ** 10, it only performs 4 or 5 multiplications.
# - This approach is much faster for large powers like 2 ** 1000.

def power_recursive(n, pow):
    # Base case: any number to the power of 0 is 1
    if pow == 0:
        return 1
    
    # If the exponent is even
    if pow % 2 == 0:
        half_power = power_recursive(n, pow // 2)
        return half_power * half_power  # (n^(pow/2)) * (n^(pow/2))
    
    # If the exponent is odd
    else:
        return n * power_recursive(n, pow - 1)  # n * (n^(pow-1))
    

def power_iterative(n,pow):
    if pow == 0:
        return 1
    result = 1 
    while pow > 0:
        if pow % 2 != 0:
            result *= n
        n *= n
        pow //= 2
    return result


n = 4
pow = 6
result = power_recursive(n, pow)
result1 = power_iterative(n, pow)
print(f"{n} to the power of {pow} is {result}")
print(f"{n} to the power of {pow} is {result1}")


