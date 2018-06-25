def is_prime(x):
    """
    >>> is_prime(1)
    False
    >>> is_prime(0)
    False
    >>> is_prime(2)
    True
    >>> is_prime(10)
    False
    >>> is_prime(19)
    True
    """
    if x <= 1:
        return False
    return all(map(lambda y: x % y, range(2,x)))

def sum_primes(a, b):
    return sum(filter(is_prime, range(a, b)))


