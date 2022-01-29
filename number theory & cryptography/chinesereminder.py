def ExtendedEuclid(a, b):
    assert a >= b and b >= 0 and a + b > 0
    if b == 0:
        x, y = 1, 0
    else:
        (p, q) = ExtendedEuclid(b, a % b)
        x = q
        y = p-q*(a//b)
    return (x, y)


def ChineseRemainderTheorem(n1, r1, n2, r2):
    if (n2 > n1):
        bf1, bf2 = n1, r1
        n1, r1 = n2, r2
        n2, r2 = bf1, bf2
    (x, y) = ExtendedEuclid(n1, n2)
    return (r1*n2*y + r2*n1*x) % (n1*n2)


print(ChineseRemainderTheorem(11, 3, 17, 7))
