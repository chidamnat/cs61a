def gcd(m,n):
    """ returns the greatest common divisor of two numbers.
    >>> gcd(4,2)
    2
    >>> gcd(10,5)
    5
    >>> gcd(2,8)
    2
    >>> gcd(4,4)
    4
    """
    if n % m == 0:
        return m
    elif m < n:
        return gcd(n,m)
    else:
        return gcd(m-n,n)
    
def curry2(f):
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g


curry2lambda = lambda f: lambda x: lambda y: f(x,y)
