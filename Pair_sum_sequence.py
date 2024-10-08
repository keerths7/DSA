'''
Problem : Pair sum sequence
'''
# Solution-1
# Time Complexity: O(n)
# Space Complexity: O(1)

def pair_sum_sequence(arr):
    total = 0
    for i in range(len(arr)-1):
        total += arr[i] + arr[i+1]
    return total

# Solution-2 Using a separate function for sum
# Time Complexity: O(n)
# Space Complexity: O(1)

def pair_sum_sequence_usingfun(arr):
    total = 0
    for i in range(len(arr)):
        total += sum(i, i+1)
    return total

def sum(a,b):
    return a + b

arr = [5, 6, 8, 2, 3, 9, 23, 56, 10, 22]
print(pair_sum_sequence(arr))
print(pair_sum_sequence_usingfun(arr))
