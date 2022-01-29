def gcd(a, b):
    assert a >= b and b >= 0 and a + b > 0
    if b == 0:
        d, x, y = a, 1, 0
    else:
        (d, p, q) = gcd(b, a % b)
        x = q
        y = p-q*(a//b)
    assert a % d == 0 and b % d == 0
    assert d == a*x+b*y
    return (d, x, y)


def divide(a, b, n):
    assert n > 1 and a > 0
    (d, x, y) = gcd(n, a)
    assert d == 1
    return y * b % n


# print(divide(2, 7, 9))
