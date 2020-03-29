def ReduceFraction(n, m):
    if n > m:
        k = n
    else:
        k = m
    while k != 1:
        if n % k == 0 and m % k == 0:
            return n // k, m // k
        else:
            k -= 1
    return n, m


n, m = int(input()), int(input())
print(ReduceFraction(n, m))
