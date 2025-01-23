#  List operators

a = [1,2,3]
b = [4,5,6]
c = a + b   #  + operator concatenates the list, it consists of elements from both the lists
print(c)

a =[0]
a = a*4  # * operator repeats the elements to the number of times mentioned
print(a)
print([0,1,2]*3)


# List methods

a = [0,1,2,3,4,5]

print(len(a))  # returns the count of elements in the list

print(max(a))  # returns the item with the highest value in the list

print(min(a))  # returns the item with the lowest value in the list

print(sum(a))  # returns sum of all the elements

# finding avg of list using these functions

print(sum(a)/ len(a))

# problem example sum
total = 0
while(True):
    inp = input("Enter the value: ")
    if inp == "done": break
    value = float(inp)
    total += value
print(total)