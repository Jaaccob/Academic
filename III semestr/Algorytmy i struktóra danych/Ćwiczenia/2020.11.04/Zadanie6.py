import math
import random


def rekurencjaDlaPodłogi(n):
    if n == 1:
        return n
    else:
        a = (2 * rekurencjaDlaPodłogi(n // 2)) + (3 * n + 1)
    return a


def rekurencjaDlaSufitu(n):
    if n == 1:
        return n
    else:
        a = (2 * rekurencjaDlaSufitu(math.ceil(n / 2))) + (3 * n + 1)
    return a


def rekurencjaDlaSufituIPodłogi(n):
    if n == 1:
        return n
    else:
        a = (rekurencjaDlaSufituIPodłogi(math.ceil(n / 2)) + rekurencjaDlaSufituIPodłogi(n // 2)) + (3 * n + 1)
    return a


n = 5
print("N = {}".format(n))
print(rekurencjaDlaPodłogi(n))  # Wynik 34
print(rekurencjaDlaSufitu(n))  # Wynik 72
print(rekurencjaDlaSufituIPodłogi(n))  # Wynik 106

n = 7
print("N = {}".format(n))
print(rekurencjaDlaPodłogi(n))  # Wynik 34
print(rekurencjaDlaSufitu(n))  # Wynik 72
print(rekurencjaDlaSufituIPodłogi(n))  # Wynik 106


n = 8
print("N = {}".format(n))
print(rekurencjaDlaPodłogi(n))  # Wynik 34
print(rekurencjaDlaSufitu(n))  # Wynik 72
print(rekurencjaDlaSufituIPodłogi(n))  # Wynik 106

randomN = math.ceil(random.uniform(1, 32))
print("Liczba badana {}".format(randomN))
print(rekurencjaDlaPodłogi(randomN))
print(rekurencjaDlaSufitu(randomN))
print(rekurencjaDlaSufituIPodłogi(randomN))
