def count(s, value):
    """ count the number of times that value occurs in the sequence s
    >>> count([1,2,1,2,1],1)
    3
    """
    total , index = 0, 0
    for element in s:
        if element == value:
            total += 1
    return total


def sum_below(n):
    total = 0
    for i in range(n):
        total += i
    return total


def divisor(n):
    """find the list of divisors using list comprehension"""
    return [1] + [x for x in range(2,n) if n % x == 0]
