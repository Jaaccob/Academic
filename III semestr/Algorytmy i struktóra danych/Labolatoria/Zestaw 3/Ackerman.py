def alghormitmAckerman(m, n):
    print("Wartość m = {} , Wartość n = {}".format(m, n))
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return alghormitmAckerman(m - 1, 1)
    if m > 0 and n > 0:
        return alghormitmAckerman(m - 1, alghormitmAckerman(m, n - 1))

    """Funkcja Ackermanna często jest używana do testowania jakości optymalizacji kompilatorów – stosunki czasu 
    wykonania pomiędzy różnymi kompilatorami tego samego języka czasami sięgają tysiąca
    
    Inną funkcją o własnościach podobnych do funkcji Ackermanna (tzn. będąca rekurencyjną i nie pierwotnie 
    rekurencyjną) jest funkcja Sudana.
    """


print(alghormitmAckerman(2, 1))
