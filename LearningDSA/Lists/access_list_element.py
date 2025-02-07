# accesing list element by index

# Time complexity: O(n), accessing a list element (list[i]) has O(1) time complexity since lists are stored contiguously in memory, allowing direct access.  
# Space complexity: O(1), because accessing an element does not require extra memory allocation.  

shoppingList = ["Milk", "Cheese", "Paneer"]

print(shoppingList[0])
print(shoppingList[1])
# print(shoppingList[3]) results in error
print(shoppingList[-1])

# checking whether an element is present in the list using in operator

print("Milk" in shoppingList)
print("Bread" in shoppingList)

# traversing through list element

for i in shoppingList:
    print(i)