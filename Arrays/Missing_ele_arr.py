'''
https://www.geeksforgeeks.org/problems/missing-number-in-array1416/1
'''
# def find_missing_ele(arr):
#     for i in range(len(arr)+1):
#         if arr[i] != i + 1:
#             return i + 1
        
# input = [1,2,3]
# print(find_missing_ele(input))

def missing_num(arr):
    x=1
    for i in range(len(arr)+1):
        if x not in arr:
            return x
        x+=1
arr=[1,2,3,5]
print(missing_num(arr))