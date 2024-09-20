def linear_search(num_arr,ele):
    for i in range(len(num_arr)):
        if num_arr[i] == ele:
            return i
    return -1
num_arr = [21,43,56,4,5,3,75,24,6,23,54,134]
ele = int(input("Enter a number to search:"))
print("Searching element is present at index,",linear_search(num_arr,ele))