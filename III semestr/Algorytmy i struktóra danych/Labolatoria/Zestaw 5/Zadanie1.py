import Stack

Stos = Stack.Stos


def Postfix_Eval(string):
    """
    Funkcja oblicza wartość zapisaną w notacji postfiksowej. Korzysta tylko z 4 klasycznych operatorów tj.:
    - dodawanie
    - odejmowanie
    - mnożenie
    - dzielenie
    :param string: wartość zapisana w notacji postfiksowej
    :return: Zwraca obliczoną wartość int z notacji postfiksowej
    """
    stos = Stos()
    for i in string.split():
        if i.isnumeric():
            stos.push(i)
        else:
            temporary_One = stos.pop()
            temporary_Two = stos.pop()
            stos.push(do_math(int(temporary_One), int(temporary_Two), i))
    return int(stos.pop())


def do_math(temporary_One, temporary_Two, operator):
    """
    Funkcja pomocnicza do funkcji <code>Postfix_Eval</code> ,która ma za zadanie wykonywać operacje zgodnie z 4
    klasycznymi operatorami
    :param temporary_One: Pierwsza liczba przekazana z stosu z funkcji <code>Postfix_Eval</code>
    :param temporary_Two: Druga liczba przekazana z stosu z funkcji <code>Postfix_Eval</code>
    :param operator: Jeden z 4 klasycznych operatorów tj:
    - dodawanie
    - odejmowanie
    - mnożenie
    - dzielenie
    :return: Zwraca wynik w zależności od odpowedniego operatora
    """
    if operator == "+":
        return temporary_One + temporary_Two        #Według przykładu 20 + 10
    elif operator == "-":
        return temporary_Two - temporary_One        #Według przykładu 75 - 45
    elif operator == "*":
        return temporary_One * temporary_Two        #Według przykładu 30 * 30
    else:
        return temporary_Two / temporary_One        #Według przykładu 900 / 3


print(Postfix_Eval("20 10 + 75 45 - * 3 /"))
