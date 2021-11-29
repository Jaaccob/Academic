def Potega1(a, n):
    """
    Algorytm <code>Potega1</code> oblicza potęge liczby a do n na zasadzie rekurencji. Algorytm działa na zasadzie dziel
    i rządz. Algorytm rozbija elementy na poszczególne składowe i na ostatecznym końcu łączy je mnożąc każdy element z
    każdym. Dla przykładu algorytm działa w następujący sposób

    1.  n > 1 więc : Potega1(3,2) * Potega1(3,3) dla m = 2
    2.1 n > 1 więc : Potęga1(3,1) * Potega1(3,1) dla m = 1
    2.1 n = 1 więc : 3 * 3 = 9

    1. n > 1 wiec 9 * Potega1(3,3) dla m = 2

    2.2 n > 1 więc : Potega1(3,1) * Potega1(3,2) dla m = 1
    3.2 n = 1 więc : 3 * 3 = 9

    2.2 n > 1  więc : 9 * Potega1(3,2) dla m = 1

    3.3 n > 1 więc : Potega1(3,1) * Potega1(3,1) dla m = 1
    3.3 n = 1 wiec : 3 * 3 = 9

    2.2 n > 1  więc : 9 * 9 = 81 dla m = 1

    1. n > 1 wiec 9 * 81 = 243 dla m = 2
    """
    if n == 1:
        return a
    else:
        m = n // 2
        return Potega1(a, m) * Potega1(a, n - m)



print(Potega1(3,5))