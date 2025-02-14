# Time Complexity: O(n)   since we visit each and every element in the tuple to print them
# Space Complexity : O(1)  

tuple1 = ('a','b','c','d','e')

for i in tuple1:
    print(i)

# traversal using range
for i in range(len(tuple1)):
    print(tuple1[i])


# Find product and sum of all elements in a tuple
# Solution 1- Iterating through loops
# Time Complexity: O(n) as the loop iterates through all the elements in the tuple 
# Space Complexity: O(1) as no additional space os required 
def sum_product(t1):
    total = 0 
    product = 1
    for i in t1:
        total += i 
        product *= i 
    return total, product 

t1 = 1,2,3,4,5
total, product = sum_product(t1)
print(total, product) 