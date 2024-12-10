# Find missing number in an array except the array starts from any number 

# Solution 1- Using brute force approach
# Time Complexity- O(n)     as we have to traverse across all elements
# Space Complexity- O(1)
def missing_num_modified(listy):
    num1 = listy[0]
    for i in range(1,len(listy)):
        if listy[i] != num1+i:
            return f"The missing number is, {num1+i}"


listy = [89,90,91,92,93,94,95,96,97,98,99,100,101,103,104]
print(missing_num_modified(listy))
