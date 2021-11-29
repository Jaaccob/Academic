import math


def decor(fun):
    slownik = {}

    def wrapper(x):
        try:
            if x <= 0:
                raise ValueError("Nie ma sensu liczyć")
            if not isinstance(x, int):
                raise ValueError("Nie ma sensu liczyć")
            if x == 3:
                raise ValueError("Nie ma sensu liczyć")
            liczba = fun(x)
            slownik[x] = liczba
            return wrapper2(liczba, slownik, x)
        except:
            ValueError()

    def wrapper2(liczba, slownik, x):
        j = 0
        print(fun.__name__)
        licz = (int(liczba * 100))/100
        return licz

    return wrapper


@decor
def fun(x):
    print(math.sqrt(x) / (x - 3))
    return math.sqrt(x) / (x - 3)


print(fun(7))
