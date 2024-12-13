# Dictionary traversal
# Time Complexity: O(n)
# Space Complexity: O(1)

dict1 = {"one": "English", "two": "Spanish", "three": "Dutch"}
for i in dict1:          # when we use a for loop in python, by design it iterates over the keys
    print(dict1[i])