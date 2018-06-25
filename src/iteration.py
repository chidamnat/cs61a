def split(n):
    return n // 10, n % 10

def sum_digits(n):
    if n < 10:
        return n
    else:
        all_but_last , last = split(n)
        return sum_digits(all_but_last) + last

def sum_digits_iter(n):
    sum = 0
    while n > 0:
        n, last = split(n)
        sum +=  last
    return sum

def sum_digits_rec(n, sum):
    if n==0:
        return sum
    else:
        n, last = split(n)
        return sum_digits_rec(n, sum + last)
    
