def potega_Liczby(a, n):
    x = a
    while n > 1:
        x *= a
        n -= 1
    return 1 if n == 0 else x


def potega_Liczby_rek(a, n):
    return 1 if n == 0 else potega_Liczby(a, n - 1) * a


print(potega_Liczby(4, 6))
print(potega_Liczby_rek(4, 6))
