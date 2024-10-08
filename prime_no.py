
#
def prime_no(n):
    num_list = []
    for i in range(1,n+1):
        if n % i == 0:     
            num_list.append(i)
    if num_list == [1, n]:
        return 1
    return 0

#
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

#
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