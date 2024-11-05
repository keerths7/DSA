'''
Problem: https://www.geeksforgeeks.org/find-first-last-digits-number/
'''

# Solution 1- Using logic
# Time Complexity- O(logn)  
# Space Complexity- O(1)

def first_and_last(n):
    last = n % 10
    while n > 10:
        n = n // 10
    return n, last
    
    
n = int(input("Enter a number:"))
print(first_and_last(n))


# Solution 2- Using str method
# Time Complexity- O(logn)  
# Space Complexity- O(logn)

def first_and_last_str(n):
    str_n = str(n)
    first = int(str_n[0])
    last = int(str_n[-1])
    return first, last

print(first_and_last_str(n))