def power_iterative(n,pow):
    if pow == 0:
        return 1
    result = 1 
    while pow > 0:
        if pow % 2 != 0:
            result *= n
        n *= n
        pow //= 2
    return result

