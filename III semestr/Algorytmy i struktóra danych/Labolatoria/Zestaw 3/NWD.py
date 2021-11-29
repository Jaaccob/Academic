def NWD(a, b):
    if a > b:
        return NWD(a - b, b)
    elif a < b:
        return NWD(a, b - a)
    else:
        return a


def NWD2(a, b):
    if b != 0:
        return NWD2(b, a % b)
    return a


print(NWD(12, 18))
print(NWD2(12, 18))
