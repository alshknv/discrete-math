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


def diophantine(a, b, c):
    (d, x, y) = gcd(max(a, b), min(a, b))
    assert c % d == 0
    v1 = x*(c/d)
    v2 = y*(c/d)
    return (v1, v2) if a >= b else (v2, v1)


print(diophantine(10, 6, 14))
print(diophantine(6, 10, 14))
print(diophantine(391, 299, -69))
