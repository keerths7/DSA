
'''
Problem : https://www.geeksforgeeks.org/problems/odd-or-even3618/1
'''
# Time Complexity: O(1)- because all operations (modulus, bitwise, shifts) take constant time.
# Space Complexity: O(1)- since no extra space used

# Solution 1 
def evenodd(n):
    if n % 2 == 0:
        return "even"
    return "odd"

# Solution 2
def evenodd2(n):
    return "even" if n % 2 == 0 else "odd"

# Solution 3 - faster: &, which is faster than the modulus operation because it's a direct bit-level check, you check the last digit and that's enough
def evenodd3(n):
    if n & 1 == 1:  # or use n & 1 == 0: to return even first
        return "odd"
    return "even"

# Solution 4- Uses right shift and left shift to check if n is even (if after doing both it is still n) or odd ---> Odd numbers: After dividing and multiplying, they do not match the original number because the last bit (1) is lost. Even numbers: After the same process, they match because the last bit (0) remains unchanged. (division can be taken as strict division for understanding purpose)
def evenodd4(n):
    if n == (n >> 1) << 1:
        return "even"
    return "odd"

n = int(input("Enter the number:"))
print(evenodd3(n))
