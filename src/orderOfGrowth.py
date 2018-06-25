def trace(f):
    def traced(*n):
        print("calling ", f, "with argument ", *n)
        return f(*n)
    return traced

@trace
def exp(b, n):
    if n == 0:
        return 1
    else:
        return b * exp(b, n-1)
    
def square(x):
    return x * x

@trace
def fast_exp(b, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return square(fast_exp(b, n//2))
    else:
        return b * fast_exp(b, n-1)
