# Solution 1- Using iteration
# Time Complexity- O(min(a,b))
# Space Complexity- O(1)

def gcd_bruteforce(a,b):
    if a == 0:
        return b
    if b == 0:
        return a
    res = min(a,b)
    while(res > 0):
        if a % res == 0 and b % res == 0 :
            return res
        res -= 1


# Solution 2- Using Euclidean formula, recursion
# Time Complexity- O(min(a,b))
# Space Complexity- O(log(min(a,b)))

def gcd_euclidean_recur(a,b):
    if b == 0:
        return a
    return gcd_euclidean_recur(b, a % b)


# Solution 3- Using Euclidean formula, iterative
# Time Complexity- O(log(min(a,b)))
# Space Complexity- O(1)

def gcd_euclidean_iter(a,b):
    while b != 0:
        a, b = b, a % b
    return a


print(gcd_bruteforce(12,16))
print(gcd_euclidean_recur(16,12))
print(gcd_euclidean_iter(12,16))

