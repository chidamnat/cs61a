def contains(a, b):
    """ contains returns if b is contained in a
    >>> contains('strength', 'stent')
    True
    >>> contains('strength', 'rest')
    False
    >>> contains('strength', 'tenth')
    True
    """
    ai = iter(a)
    for x in b:
        try:
            while(next(ai) != x):
                pass
        except StopIteration:
            return False
    return True


def double(x):
    print('**', x, '=>', 2*x, '**')
    return 2 * x

def even(start, end):
    even = start + (start % 2)
    while even < end:
        yield even
        even += 2

def a_then_b(a, b):
    for x in a:
        yield x
    for x in b:
        yield x

def a_then_b_yield_from(a, b):
    yield from a
    yield from b

def countdown(n):
    for i in range(n,0,-1):
        yield i

def countdown_yield_from(n):
    if n > 0:
        yield n
        yield from countdown_yield_from(n-1)


