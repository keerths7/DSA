'''
https://www.geeksforgeeks.org/problems/find-minimum-and-maximum-element-in-an-array4428/1
'''
# Solution 1- Using built in function
# Time Complexity- O(nlogn)
# Space Complexity- O(n)

def find_max_min(arr):
    if len(arr) == 1:
        return arr[0] 
    arr.sort()              # Python uses Timsort which has time complexity of O(nlogn)
    return arr[0], arr[-1]

# Solution 2- Using brute force
# Time Complexity- O(n)
# Space Complexity- O(1)

def find_max_min_brute(arr):
    if len(arr) == 1:
        return arr[0]
    min_val = arr[0]
    max_val = arr[0]
    for i in range(1,len(arr)):
        if min_val > arr[i]:
            min_val = arr[i]
        if max_val < arr[i]:
            max_val = arr[i]
    return min_val, max_val

# Solution 3- Using adjacent pairs comparision
# Time Complexity- O(n/2) = O(n)
# Space Complexity- O(1)

def find_min_max_initial_comparision_builtinminmax(arr):
    if len(arr) % 2 == 0:
        if arr[0] > arr[1]:
            maxx = arr[0]
            minn = arr[1]
        else:
            maxx = arr[1]
            minn = arr[0] 
        i = 2

    else:
        minn = maxx = arr[0]
        i = 1
           
    while i < len(arr):
        if arr[i] > arr[i+1]:
            maxx = max(maxx, arr[i])
            minn = min(minn, arr[i+1])
        else:
            maxx = max(maxx, arr[i+1])
            minn = min(minn, arr[i])
        i += 2
    return (minn, maxx)

# Solution 4- Using Tournament method- divide and conquer
# Time Complexity- O(n)
# Space Complexity- O(1)

def min_max_tournament(arr, low, high):
    if low == high:
        arr_min = arr[low] 
        arr_max = arr[low]
        return (arr_min, arr_max)
    elif high == low + 1:
        if arr[low] < arr[high]:           
            arr_min = arr[low]    
            arr_max = arr[high]
        else:
            arr_min = arr[high]            
            arr_max = arr[low]    
        return(arr_min, arr_max)
    else:
        mid = (low + high) // 2
        arr_min1, arr_max1 = min_max_tournament(arr, low, mid)         
        arr_min2, arr_max2 = min_max_tournament(arr, mid+1, high)       
    
    return (min(arr_min1, arr_min2), max(arr_max1, arr_max2))


arr = [1000, 11, 445, 45, 330, 3000, 677, 988]
low = 0
high = len(arr) - 1

# print(find_max_min(arr))
# min_val, max_val = find_max_min(arr)  # when I don't want to print it as a tuple
# print(min_val, max_val)

# print(find_max_min_brute(arr))
# print(find_min_max_initial_comparision_builtinminmax(arr))
print(min_max_tournament(arr, low, high))