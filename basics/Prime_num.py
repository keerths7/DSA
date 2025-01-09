'''
https://www.geeksforgeeks.org/problems/prime-number2314/1
'''
# Solution 1- Bruteforce
# Time Complexity- O(n)
# Space Complexity- O(1)

def prime_num_bruteforce(n):
    for i in range(2,n):
        if n % i == 0:
            return 0
    return 1


# Solution 2- Taking only upto sqrt
# Time Complexity- O(root(n))
# Space Complexity- O(1)
def prime_num_sqrt(n):
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            return 0
    return 1


# Solution 3- Taking only upto sqrt
# Time Complexity- O(root(n))
# Space Complexity- O(1)

def sixiplusk(n):
    if n % 2 == 0 or n % 3 == 0:
        return 0
    for i in range(5,n):
        if n % i == 0:
            return 0
        i += 6
    return 1


n = int(input("Enter the number:"))
print(prime_num_bruteforce(n))
print(prime_num_sqrt(n))
print(sixiplusk(n))