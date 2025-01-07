# Solution 1- Using iteration
# Time Complexity: O(n)- since we are searching through all the elements in the array
# Space Complexity: O(1)- no extra space used
def max_nums_product_modified(arr):
    max1 = 0
    max2 = 0 
    for i in arr:
        if i > max1:
            max2 = max1
            max1 = i
        elif i > max2 and i != max1:
            max2 = i
    return max1 * max2

my_list = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 90, 1, 2, 0]
print(max_nums_product_modified(my_list)) 