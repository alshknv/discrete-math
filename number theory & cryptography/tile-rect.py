def squares(n, m):
    a = n
    b = m
    while a > 0 and b > 0:
        if a >= b:
            a = a % b
        else:
            b = b % a
    x = max(a, b)
    return n*m/(x*x)


print(squares(10, 6))
