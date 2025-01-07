def permutation(list1, list2):
    if len(list1) == len(list2):
        list1.sort()
        list2.sort()        # O(nlogn)
        if list1 == list2:  # O(2n)
            return "True"
    return "False"

list1 = [1,2,3]         #list1 = ["a","b","c"] 
list2 = [1,3,3]         #list2 = ["b","a","c"]  
print(permutation(list1, list2))