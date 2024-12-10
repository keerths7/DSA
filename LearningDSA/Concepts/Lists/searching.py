# search for element in a list using in operator

# the in operator gives boolean output
# Time Complexity: O(n)  under the hood in operator uses linear search, so if the element is in the end of the list, it has to check all n elements, in operator is  more efficient when using with dictionary and sets which are implemented as hash tables.
# Space Complexity: O(1)

list1 = [1, 66, 8, 54, 77, 7, 975, 86, 9, 33]
target = 7
if target in list1:
     print("Element is present in the list.")
else:
     print("Element is not present in the list.")

# linear search
# Time Complexity: O(n)  
# Space Complexity: O(1)

found = False
for i, value in enumerate(list1):  # enumerate function keeps track of the current element 
    if value == target:
        print(i)
        found = True
        break
    
if found == False:
     print("Element not found in the list.")

