'''
Problem : https://www.geeksforgeeks.org/problems/odd-or-even3618/1
'''
#Solution 1 
def evenodd(n):
    if n % 2 == 0:
        return "even"
    return "odd"

#Solution 2
def evenodd2(n):
    return "even" if n % 2 == 0 else "odd"

#Solution 3 - faster: &, which is faster than the modulus operation because it's a direct bit-level check, you check the last digit and that's enough
def evenodd3(n):
    if n & 1 == 1:  #or use n & 0 == 0:
        return "odd"
    return "even"

n = int(input("Enter the number:"))
print(evenodd3(n))
