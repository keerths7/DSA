'''
https://www.geeksforgeeks.org/problems/missing-number-in-array1416/1
'''
# Solution 1-  
# Time complexity = O(n)
# Space complexity = O(1)

def find_missing_ele(arr):
    for i in range(len(arr)):
        if arr[i] != i + 1:
            return i + 1
    else:
        return i+2

# Solution 1-  Using summation
# Time complexity = O(n)
# Space complexity = O(1)

def find_missing_ele_sum(arr):
    n = len(arr) + 1
    total = n * (n + 1) // 2
    total1 = sum(arr)
    return total - total1


input = [1]
print(find_missing_ele(input))
print(find_missing_ele_sum(input))