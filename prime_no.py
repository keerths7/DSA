
# Solution 5- Taking only upto sqrt(n)









# Solution 1- My solution
# Time Complexity- O(n)
# Space Complexity- O(d), where d is the number of divisors
# Very inefficient because you find go from 1 to n which is a lot of numbers to find all factors, try using some logic 
def prime_no(n):
    num_list = []
    for i in range(1,n+1):
        if n % i == 0:     
            num_list.append(i)  # should have used count instead and checked if count > 2 then return not prime
    if num_list == [1, n]:
        return 1
    return 0

# Solution 4- Using count instead of appending to list
# Time Complexity- O(n)
# Space Complexity- O(1)
def prime_no(n):
    if n <= 1: 
        return 0
    count = 0
    for i in range(1,n+1):
        if n % i == 0 :
            count += 1
    if count > 2 :
        return 0
    return 1

# Solution 2 - My another solution
# Time Complexity- O(n)
# Space Complexity- O(d), where d is the number of divisors
# Same kind of inefficiency but you tried to make it efficient for even numbers but still for an odd number it goes upto n to find all factors
def prime_no2(n):
    num_list = []
    if n == 2:
        return 1
    if n != 2 and n % 2 == 0:
        return 0
    elif n % 2 != 0:
        for i in range(3, n):
            if n % i == 0:     
                num_list.append(i)
        if num_list == []:
            return 1
        return 0

# Solution 3- Srujitha's Solution
# Time Complexity- O(n)
# Space Complexity- O(1)
# Way better cause you immediately return whether true or false if any of the number from 2 to n-1 turns out to be indivisible, still if that is a very large prime number, you will have to check until n and decide to print prime which still has same time complexity 

def prime_no_3(n):
    if n > 1:
        for i in range(2,n):
            if n % i == 0:
                return 0
        else:
            return 1
    return 0



n = int(input("Enter the number:"))
print(prime_no(n))