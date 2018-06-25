# Rational Arithmetic

def mul_rational(x, y):
    """Multiply rational numbers x and y."""
    return rational(numer(x) * numer(y), denom(x) * denom(y))

def add_rational(x, y):
    """Add rational numbers x and y."""
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx*dy)

def equal_rational(x, y):
    """Return whther rational numbers x and y are equal."""
    return numer(x) * denom(y) == numer(y) * denom(x)

def gcd(m, n):
    """ returns the greatest common divisor of m, n"""
    if m % n == 0:
        return n
    elif m < n:
        return gcd(n, m)
    else:
        return gcd(m - n, n)

def print_rational(x):
    """ Print rational x."""
    print(numer(x),"/",denom(x))

# Constructor and selectors
# option 1 using list
##def rational(n, d):
##    """ Construct a rational number that represents N/D."""
##    g = gcd(n, d)
##    return [n//g, d//g]
##
##def numer(x):
##    """Return the numerator of rational number X."""
##    return x[0]
##
##def denom(x):
##    """Return the denominator of rational number X."""
##    return x[1]

# option 2 using higher order functions
def rational(n, d):
    """ Construct a rational number that represents N/D."""
    def select(name):
        if name == 'n':
            return n
        elif name == 'd':
            return d
    return select

def numer(x):
    """Return the numerator of rational number X."""
    return x('n')

def denom(x):
    """Return the denominator of rational number X."""
    return x('d')
