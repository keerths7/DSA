# Lists are mutable data structures hence the list elements can be changed

list1 = [1,2,3,4,5,6,7]
print(list1)
list1[2] = 33
print(list1)

# Inserting elements in a list

# insert() method adds an element at any position/ index we specify
list1.insert(0, 44)
print(list1)

# append() method adds an element at the end of the list
list1.append(22)
print(list1)

# extend() method adds a list at the end of another list
# it works by looping through all the elements of the new list provided and adding them one by one at the end of our list
list1.extend([99,88,77])
print(list1)