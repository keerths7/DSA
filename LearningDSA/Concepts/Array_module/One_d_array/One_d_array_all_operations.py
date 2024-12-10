from array import *

# 1. Create an array and traverse.

arr1 = array('i', [1,2,3,4,5])

for i in arr1:
    print(i)

# 2. Access individual elements through indexes

print("Step 2")
print(arr1[0])
print(arr1[1])

# 3. Append any value to the array using append()
# Adds the element only at the end of the array
# Less overhead when compared to insert, as it has to check if the position/index exists first 

print("Step 3")
arr1.append(7)
print(arr1)

# 4. Insert any value in the array using insert()
# We can add element at any position using insert(pos, element)

print("Step 4")
arr1.insert(0,8)
print(arr1)

# 5. Extend python array using extend() method
# Using this method an array can be extended with more than one value

print("Step 5")
arr2 = array('i', [12,13,14])
arr1.extend(arr2)
print(arr1)

# 6. Add items from list into array using fromlist() method
# Appends the elements of that list to the array, similar to extend method but it adds elements from a list

print("Step 6")
list1 = [18,19,20]
arr1.fromlist(list1)
print(arr1)

# 7. Remove array element using remove()
# remov() searches for the element, if it is found it removes it

print("Step 7")
arr1.remove(13)
print(arr1)

# 8. Remove last array element using pop() method
# Efficient compared to remove because unlike remove it need not search until the end to remove the element, it can directly access the last element and remove it

print("Step 8")
arr1.pop()
print(arr1)

# 9. Find index of any element using the index() method 

print("Step 9")
print(arr1.index(12))

# 10. Reverse a python array using reverse() method
# This method directly changes the original array

print("Step 10")
arr1.reverse()
print(arr1)

# 11. Get array buffer information using buffer_info() method

print("Step 11")
print(arr1.buffer_info())   # buffer_info returns a tuple: (Memory address of the buffer, Number of elements in the array)


# 12. Count() method gives the number of occurences of a particular element

print("Step 12")
print(arr1.count(8))

# 13. tolist() method converts array to list

print("Step 14")
print(arr1.tolist())    

# 14. slicing array elements

print("Step 15")
print(arr1[:4])
print(arr1[8:])
print(arr1[5:9])