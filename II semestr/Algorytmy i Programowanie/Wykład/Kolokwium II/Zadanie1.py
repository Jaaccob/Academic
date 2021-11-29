import math


def decor(fun):
    """
    Funkcja dekorująca dla funkcji, która zwraca pierwiastek z x

    ...

    Attributes
    ----------
    fun: str
        nazwa funkcji którą dekorator będzie dekorować
    x: int
        wartość którą mamy poddać pierwi    astowaniu

    Returns
    ---------
    Zwraca wyliczoną funkcję pierwiastek z x jeśli to ma sens

    >>> [function(12)]
    {12: 3.4641016151377544, 6: 2.449489742783178, 199: 14.106735979665885}
    [3]
    >>> [function(6)]
    {12: 3.4641016151377544, 6: 2.449489742783178, 199: 14.106735979665885}
    [2]
    >>> [function(-5)]
    Niepoprawna liczba
    [None]
    """
    slownik = {}

    def wrapper(x):
        try:
            if x <= 0:
                raise ValueError("Niepoprawna liczba")
            if not isinstance(x, int):
                raise ValueError("To powinna być liczba")
            wartosc = fun(x)
            slownik[x] = wartosc
            print(slownik)
            return wrapper2(wartosc)
        except:
            print("Niepoprawna liczba")

    def wrapper2(x):
        return int(x)

    return wrapper


@decor
def function(x):
    return math.sqrt(x)



if __name__ == "__main__":
    print(function(-5))
    print(function(12))
    print(function(6))
    print(function(199))
    print(function("qwerty"))
    import doctest
    doctest.testmod()
