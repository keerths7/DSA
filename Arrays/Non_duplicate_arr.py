

# Solution 1- Brute force 
# Time complexity: O(n^2)
# Space complexity: O(1)

def find_repeating(arr):
    uniuqe_list = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] != arr[j]:
                uniuqe_list.append(arr[i])

# Solution 2- Using set
# Time complexity: O(n)
# Space complexity: O(n)

def find_repeating_using_set(arr):
    seen = set()
    unique_list = []
    for i in arr:
        if i not in seen:
            unique_list.append(i)
            seen.add(i)
    return unique_list

arr = [72, 13, 34, 56, 6, 83, 6, 256]
print(find_repeating(arr))
print(find_repeating_using_set(arr))

