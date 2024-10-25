def rotate_an_array_extraspace(arr):
    rotated_arr = []
    ele1 = arr[len(arr)-1]
    rotated_arr.append(ele1)
    for i in range(0, len(arr)-1):
        rotated_arr.append(arr[i])
    return rotated_arr


def rotate_an_array(arr):
    x = arr[-1]
    n = len(arr)
    for i in range(n-1):
        arr[n-1-i] = arr[n-2-i]
    arr[0] = x
    return arr

arr = [1,2,3,4,5]
print(rotate_an_array_extraspace(arr))
print(rotate_an_array(arr))