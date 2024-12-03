

# Solution 1- Using the built in list methods 
# Time Complexity: O(len(list))
# Space Complexity: O(1)

def avg_list_builtin(list1):
    return sum(list1)/ len(list1)

# Solution 2- Using logic
# Time Complexity: O(len(list))
# Space Complexity: O(1)

def avg_list_logic(list1):
    sum = 0
    count = 0
    for i in list1:
        sum += i 
        count += 1
    return sum/count


list1 = [2,3,4,5,6,7,8]
print(avg_list_builtin(list1))
print(avg_list_logic(list1))
