'''

'''
# Using while loop iteration
def gcd_bruteforce(a,b):
    res = min(a,b)
    while(res > 0):
        if a % res == 0 and b % res == 0:
            return res
        res -= 1

def gcd_subtracted(a,b):
    if a == b:
        return a
    elif a > b:
      return gcd_subtracted(b, a-b)
    else:
      return gcd_subtracted(a, b-a)

# Using recursion
def gcd_euclidean(a,b):
    if b == 0:
        return a
    else:
        return gcd_euclidean(b, a % b)

def gcd_euclidean_iterative(a,b):
    if a == 0:
        return b
    return a
 
    while b != 0:
        a,b = b, a % b
    return a


print(gcd_bruteforce(16,12))
print(gcd_euclidean(16,12))
print(gcd_euclidean_iterative(16,12))
print(gcd_subtracted(16,12))