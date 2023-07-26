def stairs(n):
    if n <= 2:
        return n

    a, b = 1, 2
    for _ in range(2, n):
        a, b = b, a + b
    return b

def fib(n):
    if n <= 0:
        return 0
    if n == 1 or n == 2:
        return 1
    
    
    one, two = 1, 1
    curr = 0
    for _ in range(2, n):
        curr = one + two
        one, two = two, curr
    return curr
