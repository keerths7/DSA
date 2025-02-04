'''
Sum of factors of a number upto n
https://www.geeksforgeeks.org/problems/sum-of-all-divisors-from-1-to-n4738/1?utm_source=youtube&utm_medium=courseteam_practice_desc&utm_campaign=problem_of_the_day
'''

# Solution 1- Brute force
# Time Complexity: O(n^2)- two nested loops
# Space Complexity: O(1)
def sum_factors_upto(n):
    sum = 1
    for i in range(2,n+1):          # O(n)  
        for j in range(1,i+1):      # O(n)
            if i % j == 0:
                sum+= j
    return sum


# Solution 2- Optimized
# Time Complexity: O(n*sqrt(n))
# Space Complexity: O(1)
def sum_factors_upto_optimized(n):
    sum = 1
    for i in range(2,n+1):                      # O(n)
        for j in range(1, int(i**0.5)+1):       # O(sqrt(n))
                if i % j == 0:
                    sum += j
                    if i // j != j:
                        sum += i//j
    return sum


# Solution 3- Better optimized
# Time Complexity: O(n)
# Space Complexity: O(1)
'''
Lets target the numbers in the range of 1 to n, add 8 as 1 is present in all numbers, add 2 in only 8 // 2 times as it is only present in even numbers which equals 4, 4 * 2 = 8, 4 is present 2 times, so 4*2 = 8, 
so the pattern is n // 1 * 1, n // 2 * 2, n //3 * 3 and so on, hence it is number of occurences times the number itself
some numbers like 5,6,7,8, will be added only once as there is no common factors.
'''
def sum_factors_upto_optimized_better(n):
    sum = 0 
    for i in range(1, n+1):
        sum += (n // i) * i 
    return sum


print(sum_factors_upto(49))
print(sum_factors_upto_optimized(49))
print(sum_factors_upto_optimized_better(49))