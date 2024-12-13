# Time Complexity: O(n)
# Space Complexity: O(1)


def search_dict(dict1, target):
    for i in dict1:
        if dict1[i] == target:
            return i
    return -1


dict1 = {"one": "English", "two": "Spanish", "three": "Dutch"}
target = "Spanish"
print(search_dict(dict1, target))
