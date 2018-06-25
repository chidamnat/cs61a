def invert(x):
    y = 1/x
    print('Never printed if x is 0')
    return y

def invert_safe(x):
    try:
        invert(x)
    except ZeroDivisionError as e:
        print("handling " , e)
        return 0

from operator import mul, truediv
def reduce(f, s, initial):
    """Combine elements of as pairwise using f, starting with initial.
    >>> reduce(mul, [2,4,8],1)
    64
    """
    for x in s:
        initial = f(initial, x)
    return initial

def reduce1(f, s, initial):
    """Combine elements of as pairwise using f, starting with initial.
    >>> reduce1(mul, [2,4,8],1)
    64
    """
    if not s:
        return initial
    else:
        first , rest = s[0], s[1:]
        return reduce(f, rest, f(initial, first))
        
def divide_all(n, ds):
    try:
        reduce(truediv, ds, n)
    except ZeroDivisionError as e:
        return float('inf')
        
