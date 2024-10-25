

# Solution 1- Brute force 
# Time complexity: O(n^2)
# Space complexity: O(1)

def find_repeating(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                return arr[i]

# Solution 2-  
# Time complexity: O(n)
# Space complexity: O(n)

def find_repeating_using_set(arr):
    seen = set()
    for i in arr:
        if i in seen:
            return i
        seen.add(i)
    

arr = [72, 13, 34, 56, 6, 83, 6, 256]
print(find_repeating(arr))
print(find_repeating_using_set(arr))

