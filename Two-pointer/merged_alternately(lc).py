# def power_iterative(n,pow):
#     if pow == 0:
#         return 1
#     result = 1 
#     while pow > 0:
#         if pow % 2 != 0:
#             result *= n
#         n *= n
#         pow //= 2
#     return result


def binary_search(i,j,arr,target):
    if i > j:
        return None
    mid = (i + j) // 2   
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(mid+1,j,arr,target)
    else:
        return binary_search(i,mid-1,arr,target)


target = 122
arr = [5,6,7,23,55,67,88,98,99,102,122,134,156,167,187]
i = 0
j = len(arr) - 1
print(binary_search(i,j,arr,target))