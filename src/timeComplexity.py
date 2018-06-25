def count(f):
    def counted(*args):
        counted.call_count += 1
        return f(*args)
    counted.call_count = 0
    return counted

@count
def divides(k, n):
    return n % k == 0

def factors(n):
    total = 0
    for k in range(1,n+1):
        if divides(k, n):
            total += 1
    return total

from math import sqrt

def factors_fast(n):
    total = 0
    sqrt_n = sqrt(n)
    k = 1
    while k < sqrt(n):
        if divides(k, n):
            total += 2
        k += 1
    if k * k == n:
        total += 1
    return total
