
# pow 1
# pow 2
# pow 3


def poww(num):
    last = num % 10
    count = 0 
    num = 1
    while last == num:
        num = last * last 
        count += 1  
    num