def FastModularExponentiation2k(b, k, m):
    p = 1
    while (p <= k):
        b = (b * b) % m
        p += 1
    return b


def FastModularExponentiation(b, e, m):
    e %= m-1
    bin = format(e, 'b')
    b2k = []
    k = 1
    while (k <= e):
        b2k.append(
            ((b2k[len(b2k)-1] * b2k[len(b2k)-1] if len(b2k) > 0 else b)) % m)
        k *= 2
    i, b = len(b2k)-1, 1
    for x in bin:
        if x == '1':
            b = (b * b2k[i]) % m
        i -= 1
    return b


# print(FastModularExponentiation2k(7, 3, 11))
# print(FastModularExponentiation(7, 8, 11))
# print(FastModularExponentiation(7, 223, 11))
# print(FastModularExponentiation(7, 3, 11))
