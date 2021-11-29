def decor(function):
    """
    Funckja decor odpowiedzialna jest za dekorowanie funkcji function, a funkcja wewnętrzna wrapper odpowiedzialna
    jest za stworzenie pliku do którego są wpisywane za pomocą dodawania nowych elementów tylko liczby parzyste

    ...

    Attributes
    ----------
    function: str
        nazwa funkcji którą będziemy dekorować

    Returns:
    --------
    Zwraca odekorowaną funkcję
    """

    def wrapper(a1, q):
        table = function(a1, q)
        table_even = []
        for i in range(len(table)):
            if table[i] % 2 == 0:
                table_even.append(table[i])
        with open("parzyste.txt", 'w') as file:
            try:
                for i in range(len(table_even)):
                    file.write(str(table_even[i]) + "\n")
            except:
                Exception("Coś poszło nie tak")
            finally:
                file.close()

    return wrapper


@decor
def function(a1, q):
    """
    Funkcja function odpowiedzialna jest za wyliczenie 100 pierwszych elementów ciągu geometrycznego i wypisanie go
     do konsoli.

     ...

    Attributes:
    -----------
        a1: int
            Pierwszy wyraz ciągu geometrycznego
        q: int
            Iloraz ciągu geometrycznego
    Returns:
    ---------
        Zwraca wyliczoną listę 100 pierwszych elementów ciągu geometrycznego
    """
    table = []
    for i in range(1, 101):
        table.append(a1 * q ** (i - 1))
    print(table)
    return table


function(2, -2)
