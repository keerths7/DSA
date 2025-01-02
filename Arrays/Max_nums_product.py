'''
Find the product of the first two largest numbers in a list
'''

# Solution 1- Using built-in functions
# Time Complexity: O(nlogn)
# Space Complexity: O(n)- no extra space used
def max_num_product(arr):
    arr.sort()
    return arr[-1] * arr[-2]


# Solution 2- Using 
# Time Complexity: O(n)- since we are searching through all the elements in the array
# Space Complexity: O(1)- no extra space used
def max_num_product(arr):
    max1, max2 = 0,0 
    for i in arr:
        if i > max1:
            max2 = max1
            max1 = i
        elif i > max2:
            max2 = i
    return max1 * max2

arr = [3,4,566,77,2,5,78,90,55,44]
print(max_num_product(arr))

