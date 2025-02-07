# Time Complexity: O(n)   since we visit each and every element in the tuple to print them
# Space Complexity : O(1)  

tuple1 = ('a','b','c','d','e')

for i in tuple1:
    print(i)

# traversal using range
for i in range(len(tuple1)):
    print(tuple1[i])