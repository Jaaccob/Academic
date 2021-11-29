def sum1(n, suma=0):
    if n != 0:
        suma += 1 / n
        n -= 1
        return sum1(n, suma)
    return suma


def sum2(n, suma=0):
    if n != 0:
        suma = suma + (1 / (n * n))
        n -= 1
        return sum2(n, suma)
    return suma


def sum3(n, suma=0):
    if n != 0:
        suma = suma + n
        n -= 1
        return sum3(n, suma)
    return suma


def sum4(n, suma=0):
    if n != 0:
        suma = suma + 2**n
        n -= 1
        return sum4(n, suma)
    return suma

print(sum1(5))
print(sum2(5))
print(sum3(5))
print(sum4(5))
