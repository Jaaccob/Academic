import math


def rekurencja(n):
    if n == 1 or n == 2:
        return 4
    else:
        return 2 * rekurencja(n // 3) + rekurencja(math.ceil(n / 3)) + 2 * n + 4


print(rekurencja(10))
