import numpy as np

# We can't perform arithmetic operations directly on lists like we can with arrays.

arr1 = np.array([1, 2, 3, 4, 5])
print(arr1 / 2)  # This works because NumPy arrays support element-wise operations

list1 = [1, 2, 3, 4, 5]
print(list1 / 2)  # This raises a TypeError because lists don't support element-wise operations

# Arrays in NumPy are typically homogeneous, meaning they must contain elements of the same data type.

list1 = [1, 2, 3, 4, 5, "a", "b"]
print(list1)  # Lists can contain heterogeneous elements (different data types)

arr2 = np.array([1, 2, 3, 4, "a"])  # NumPy converts all elements to a common type (str in this case)
print(arr2)  # The array becomes homogeneous, with all elements converted to strings
