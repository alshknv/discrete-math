def lcm(a, b):
    assert a > 0 and b > 0
    ab = a*b
    while a > 0 and b > 0:
        if a >= b:
            a = a % b
        else:
            b = b % a
    return ab / max(a, b)


print(lcm(15, 10))
