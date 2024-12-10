# Find missing number in an array of 1 to n elements

def missing_num(list1):
    for i in range(1,len(list1) + 1):
        if i != list1[i-1]:
            return i

def missing_num_logic(list1):
    num_count = len(list1) + 1
    total = (num_count * num_count+1) / 2 
    missing_num = total - sum(list1)
    return missing_num

list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20]
print(missing_num(list1))
print(missing_num_logic(list1))