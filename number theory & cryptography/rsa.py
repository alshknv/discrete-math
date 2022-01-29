import math
import modularexp
import modulardiv
import chinesereminder


def PowMod(a, n, modulo):
    return modularexp.FastModularExponentiation(a, n, modulo)


def ConvertToInt(message):
    intmsg = 0
    for char in message:
        intmsg <<= 8
        intmsg |= ord(char)
    return intmsg


def ConvertToStr(m):
    str = ""
    arr = []
    while m > 0:
        arr.append(chr(m & 255))
        m >>= 8
    arr.reverse()
    return "".join(arr)


def IntSqrt(n):
    return math.floor(math.sqrt(n))


def InvertModulo(a, n):
    (d, x, y) = modulardiv.gcd(max(a, n), min(a, n))
    inv = x if a > n else y
    if (inv < 0):
        inv += n
    return inv


def ChineseRemainderTheorem(n1, r1, n2, r2):
    return chinesereminder.ChineseRemainderTheorem(n1, r1, n2, r2)


def Encrypt(message, modulo, exponent):
    return PowMod(ConvertToInt(message), exponent, modulo)


def Decrypt(ciphertext, p, q, exponent):
    d = InvertModulo(exponent, (p-1)*(q-1))
    assert exponent*d % ((p-1)*(q-1)) == 1
    return ConvertToStr(PowMod(ciphertext, d, p * q))


def DecipherSimple(ciphertext, modulo, exponent, potential_messages):
    for message in potential_messages:
        if ciphertext == Encrypt(message, modulo, exponent):
            return message
    return "don't know"


def DecipherSmallPrime(ciphertext, modulo, exponent):
    for small_prime in range(2, 1000000):
        if modulo % small_prime == 0:
            big_prime = modulo // small_prime
            return Decrypt(ciphertext, small_prime, big_prime, exponent)
    return "don't know"


def DecipherSmallDiff(ciphertext, modulo, exponent):
    sqm = IntSqrt(modulo)
    for small_prime in range(sqm - 5000, sqm):
        if modulo % small_prime == 0:
            big_prime = modulo // small_prime
            return Decrypt(ciphertext, small_prime, big_prime, exponent)
    return "don't know"


def GCD(a, b):
    (d, x, y) = modulardiv.gcd(max(a, b), min(a, b))
    return d


def DecipherCommonDivisor(first_ciphertext, first_modulo, first_exponent, second_ciphertext, second_modulo, second_exponent):
    common_prime = GCD(first_modulo, second_modulo)
    if common_prime == 1:
        return ("unknown message 1", "unknown message 2")
    q1 = first_modulo // common_prime
    q2 = second_modulo // common_prime
    return (Decrypt(first_ciphertext, common_prime, q1, first_exponent), Decrypt(second_ciphertext, common_prime, q2, second_exponent))


def DecipherHastad(first_ciphertext, first_modulo, second_ciphertext, second_modulo):
    r = ChineseRemainderTheorem(
        first_modulo, first_ciphertext, second_modulo, second_ciphertext)
    return ConvertToStr(IntSqrt(r))


print("problem 2")
p = 1000000007
q = 1000000009
exponent = 23917
modulo = p * q
ciphertext = Encrypt("attack", modulo, exponent)
message = Decrypt(ciphertext, p, q, exponent)
print(message)

print("problem 3")
modulo = 101
exponent = 12
ciphertext = Encrypt("attack", modulo, exponent)
print(ciphertext)
print(DecipherSimple(ciphertext, modulo, exponent,
      ["attack", "don't attack", "wait"]))

print("problem 4")
modulo = 101 * 18298970732541109011012304219376080251334480295537316123696052970419466495220522723330315111017831737980079504337868198011077274303193766040393009648852841770668239779097280026631944319501437547002412556176186750790476901358334138818777298389724049250700606462316428106882097210008142941838672676714188593227684360287806974345181893018133710957167334490627178666071809992955566020058374505477745993383434501768887090900283569055646901291270870833498474402084748161755197005050874785474707550376333429671113753137201128897550014524209754619355308207537703754006699795711188492048286436285518105948050401762394690148387
exponent = 239
ciphertext = Encrypt("attack", modulo, exponent)
print(ciphertext)
print(DecipherSmallPrime(ciphertext, modulo, exponent))

print("problem 5")
p = 1000000007
q = 1000000009
n = p * q
e = 239
ciphertext = Encrypt("attack", n, e)
message = DecipherSmallDiff(ciphertext, n, e)
print(ciphertext)
print(message)

print("problem 6")
p = 101
q1 = 18298970732541109011012304219376080251334480295537316123696052970419466495220522723330315111017831737980079504337868198011077274303193766040393009648852841770668239779097280026631944319501437547002412556176186750790476901358334138818777298389724049250700606462316428106882097210008142941838672676714188593227684360287806974345181893018133710957167334490627178666071809992955566020058374505477745993383434501768887090900283569055646901291270870833498474402084748161755197005050874785474707550376333429671113753137201128897550014524209754619355308207537703754006699795711188492048286436285518105948050401762394690148387
q2 = 1000000007
first_modulo = p * q1
second_modulo = p * q2
first_exponent = 239
second_exponent = 17
first_ciphertext = Encrypt("attack", first_modulo, first_exponent)
second_ciphertext = Encrypt("wait", second_modulo, second_exponent)
print(DecipherCommonDivisor(first_ciphertext, first_modulo,
      first_exponent, second_ciphertext, second_modulo, second_exponent))

print("problem 7")
p1 = 790383132652258876190399065097
q1 = 662503581792812531719955475509
p2 = 656917682542437675078478868539
q2 = 1263581691331332127259083713503
n1 = p1 * q1
n2 = p2 * q2
ciphertext1 = Encrypt("attack", n1, 2)
ciphertext2 = Encrypt("attack", n2, 2)
message = DecipherHastad(ciphertext1, n1, ciphertext2, n2)
print(message)
