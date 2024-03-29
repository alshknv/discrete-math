import functools

# Converts string to hex


def toHex(s):
    lst = []
    for ch in s:
        hv = hex(ord(ch)).replace('0x', '')
        if len(hv) == 1:
            hv = '0'+hv
        lst.append(hv)

    return functools.reduce(lambda x, y: x+y, lst)

# Converts hex to string


def toStr(s):
    return s and chr(int(s[:2], base=16)) + toStr(s[2:]) or ''

# Computes XOR of two messages s1 and s2.
# s1 and s2 must have the same length.


def Xor(s1, s2):
    res = ""
    for i in range(len(s1)):
        res += format(int(s1[i], 16) ^ int(s2[i], 16), '01x')
    return res


def TryGuessingSubstring(substring, message_length, xor_messages):
    good_guesses = []
    for pos in range(message_length - len(substring) + 1):
        guess = toHex(chr(0) * pos + substring + chr(0) *
                      (message_length - len(substring) - pos))
        other_message_part = toStr(Xor(guess, xor_messages))[
            pos:pos + len(substring)]
        good_guess = True
        for i in range(len(other_message_part)):
            if not other_message_part[i].isalpha() and not other_message_part[i].isspace():
                good_guess = False
                break
        if good_guess:
            good_guesses.append((guess, pos, other_message_part))

    print("\nGood guesses:")
    for guess in good_guesses:
        print("position: %d, one message part: \"%s\", another message part: \"%s\"" % (
            guess[1], substring, guess[2]))


message1 = "steal the secret"
message2 = "the boy the girl"
key = "supersecretverys"
ciphertext1 = Xor(toHex(message1), toHex(key))
ciphertext2 = Xor(toHex(message2), toHex(key))
xor_ciphertexts = Xor(ciphertext1, ciphertext2)
xor_messages = Xor(toHex(message1), toHex(message2))
print(xor_ciphertexts)
print(xor_messages)
if xor_ciphertexts == xor_messages:
    print("Xor of the ciphertexts is the same as xor of messages")
else:
    print("Xor of the ciphertexts differs from the xor of messages")

TryGuessingSubstring(" the ", len(message1), xor_messages)
