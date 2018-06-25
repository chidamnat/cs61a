def factorial(n, k=1):
    """
    time complexity = O(n)
    space complexity = O(n)
    """
    if n == 0 :
        return k
    else:
        return factorial(n-1, k*n)

def factIter(n, k):
    """
    time complexity = O(n)
    space complexity = O(1)
    """
    while n > 0:
        n, k = n-1, k * n
    return k


def tail_factorial(n, accumulator=1):
    if n == 0:
        return 1
    else:
        return tail_factorial(n-1, accumulator * n)
