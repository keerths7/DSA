def diagonal_sum(arr):
    total = 0
    if len(arr) == len(arr[0]):
        for i in range(len(arr)):
            total += arr[i][i]  
        return total
    return "check the array"

arr = [[3, 4],[77, 2]]
print(diagonal_sum(arr))