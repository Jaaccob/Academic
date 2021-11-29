import random


def haszowanie(rzecz, modulo):
    """
    Summary
    ------
    Haszuje zadane zmienne za pomocą funkcji modulo

    Parameters
    ------
    rzecz : int, str, tuple
        element do zhaszowania
    modulo : int
        definiuje jakiego modulo chcemy użyc do haszowania

    Examples
    ------
    haszowanie("A gdyby tak rzucić wszystko i pojechać w biezczady?",15)
    haszowanie(1.5472748283,10)
    """
    slownik = {" ": 0, "A": 1, "ą": 2, "B": 3, "C": 4, "ć": 5, "D": 6, "E": 7, "ę": 8, "F": 9,
               "G": 10, "H": 11, "I": 12, "J": 13, "L": 14, "ł": 15, "M": 16, "N": 17,
               "ń": 18, "O": 19, "ó": 20, "P": 21, "R": 22, "S": 23, "T": 24, "U": 25,
               "W": 26, "Y": 27, "Z": 28, "ź": 29, "ż": 30, "ś": 31, "K": 32, ",": 33,
               ".": 34, "<": 35, ">": 36, "'": 37, "`": 38, "?": 39, "!": 40, "/": 41,
               "1": 42, "2": 43, "3": 44, "4": 45, "5": 46, "6": 47, "7": 48, "49": 8, "9": 50, "0": 51}
    suma = 0
    if type(rzecz) is str:
        for i in rzecz:
            if i in slownik.keys():
                suma += slownik[i]
        return suma % modulo
    elif type(rzecz) is float:
        rzecz = str(rzecz)
        for i in rzecz:
            if i != ".":
                suma += int(i)
        return suma % modulo
    elif type(rzecz) is int:
        return rzecz % modulo
    elif type(rzecz) is tuple:
        return haszowanie(rzecz[0], modulo)
    elif type(rzecz) is list:
        return haszowanie(rzecz[0], modulo)


def generowanie_rejestracji(liczba):
    lista = []
    alfabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'W',
               'Y', 'X', 'Z']

    for i in range(liczba):
        rejestracja = ""
        for x in range(5):
            if x == 3:
                rejestracja += str(random.randint(10000, 99999))
            else:
                rejestracja += alfabet[random.randint(0, len(alfabet) - 1)]
        lista.append(rejestracja)
    return lista


class tablica_rejestr():
    def __init__(self):
        self.rejestracje = [[]] * 10
        self.modulo = 10

    def get_modulo(self):
        return self.modulo

    def set_modulo(self, modulo):
        if isinstance(modulo, int):
            self.modulo = modulo
        else:
            raise TypeError("Zły typ modulo, powinien być int")

    def dodaj_rejestracje(self, rzecz):
        hasz = haszowanie(rzecz, self.modulo)
        print(hasz)
        self.rejestracje[hasz].append(rzecz)


rejestracje = generowanie_rejestracji(50)
print(rejestracje)
rejestr = tablica_rejestr()

for i in range(50):
    rejestr.dodaj_rejestracje(rejestracje[i])

print(rejestr.rejestracje)