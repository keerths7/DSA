'''
https://codeforces.com/problemset/problem/1294/C
'''

def product_of_three_nums(n):
    for i in range(2, int(n**0.5) + 1): 
        if n % i == 0:
            reduced = n // i 
            break
    else:
        return None

    for j in range(i+1, int((reduced)**0.5) + 1):
        if reduced % j == 0:
            k = reduced // j
            if k != i and k != j:
                return i, j, k
    return None

n = int(input("Enter a number: "))                    
print(product_of_three_nums(n))