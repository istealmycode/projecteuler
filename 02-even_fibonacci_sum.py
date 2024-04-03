def even_fibonacci_sum(limit):
    x, y = 1, 1
    even_fib_sum = 0

    while x <= limit:
        if x & 1 == 0:
            even_fib_sum += x
        x, y = y, x + y

    return even_fib_sum
