'''
https://codeforces.com/problemset/problem/1294/C
'''

def product_of_three_nums(n):
    for i in range(2, int(n**0.5) + 1): 
        if n % i == 0:
            a = i 
            reduced = n // i 
            break

    for j in range(a+1, int((reduced)**0.5) + 1):
        if reduced % j == 0:
            k = reduced // j
            if k != i and k != j:
                return i, j, k

n = int(input("Enter a number: "))                    
print(product_of_three_nums(n))