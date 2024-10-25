'''
Sorting without using sort()
'''
# Solution 1: Finding min repeatedly 
# Time Complexity: O(n^2)
# Space Complexity: O(n)

def sort_array_bruteforce(arr):
    new_arr = []
    while arr:
        for i in range(len(arr)):
            min = arr[0]
            for i in range(1, len(arr)):       
                if min > arr[i]:
                    min = arr[i]
            new_arr.append(min)
            arr.remove(min)
    return new_arr

arr = [56, 39, 24, 4525, 153, 54, 5, 35, 41, 2, 4]
print(sort_array_bruteforce(arr))




