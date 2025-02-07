# Solution 1- Using str methiods 
# Time Complexity: O(log10(n)) or O(number of digits)
# Space Complexity: O(log10(n)) or O(number of digits)
def check_palindrome_strmethod(n):
    n_string = str(n)                   # O(log10(n))
    return n_string == n_string[::-1]   # O(log10(n))


# Solution 2- Using logic 
# Time Complexity: O(log10(n)) or O(number of digits)
# Space Complexity: O(1) 
def check_palindrome_logic(n):
    reversed = 0 
    n_var = n
    while n_var > 0:
        reversed = reversed * 10 + (n_var % 10)
        n_var  = n_var // 10 
    return reversed == n


# Solution 3- Using str logic 
# Time Complexity: 
# Space Complexity:  
def check_palindrome_str_logic(n):
    n_string = str(n)
    length = len(n_string)
    for i in range(length // 2):
        if n_string[i] != n_string[length-i-1]:
            return False
    return True


# Solution 4- Using another logic 
# Time Complexity: 
# Space Complexity: 
def check_palindromee(n):
    div = 1
    while n >= 10:
        div *= 10
        n = n // 10
        
        left = n // div
        right = n % 10 
        if left != right:
            return False 
    return True

print(check_palindrome_strmethod(15651))
print(check_palindrome_logic(1551))
print(check_palindrome_str_logic(15651))
print(check_palindromee(1516151))
