'''
Problem : Finding maximum number in a array
'''
# Solution 1- Using built in functions
def find_max_num_sort(num_arr):
    num_arr.sort()
    return num_arr[-1]

# Solution 2- Using built in functions
def find_max_num_maxfn(num_arr):
    return max(num_arr)

# Solution 3- Using loop 
def find_max_num_loop(num_arr):
    let_max = num_arr[0]
    for i in range(1, len(num_arr)):
        if let_max < num_arr[i]:
            let_max = num_arr[i]
    return let_max

num_arr = [3, 4, 77, 89, 23, 89, 123, 43, 55, 233, 54, 92, 45]
#print(find_max_num_sort(num_arr))
print(find_max_num_maxfn(num_arr))
print(find_max_num_loop(num_arr))