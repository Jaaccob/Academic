import Stack

Stos = Stack.Stos


def Infix_nawias_Eval(string):
    """
    Funkcja oblicza wartość zapisaną w notacji infixowej. Korzysta tylko z 4 klasycznych operatorów tj.:
    - dodawanie
    - odejmowanie
    - mnożenie
    - dzielenie
    Konkretne operacje muszą być oddzielone nawiasami ()
    :param string: wartość zapisana w notacji postfiksowej
    :return: Zwraca obliczoną wartość int z notacji postfiksowej
    """
    stos = Stos()
    temporary_table = []
    for i in string.split():
        if i.isnumeric():
            temporary_table.append(i)
        elif i in '(+-*/':
            stos.push(i)
        elif i in ')':
            temporary_table.append(do_math(int(temporary_table.pop()), int(temporary_table.pop()), stos.pop()))
            stos.pop()
        else:
            return "Błąd w wartościach {}".format(i)
    return int(temporary_table.pop())


def do_math(temporary_One, temporary_Two, operator):
    """
    Funkcja pomocnicza do funkcji <code>Postfix_Eval</code> ,która ma za zadanie wykonywać operacje zgodnie z 4
    klasycznymi operatorami
    :param temporary_One: Pierwsza liczba przekazana z temporary_table z funkcji <code>Postfix_Eval</code>
    :param temporary_Two: Druga liczba przekazana z temporary_table z funkcji <code>Postfix_Eval</code>
    :param operator: Jeden z 4 klasycznych operatorów tj:
    - dodawanie
    - odejmowanie
    - mnożenie
    - dzielenie
    :return: Zwraca wynik w zależności od odpowedniego operatora
    """
    if operator == "+":
        return temporary_One + temporary_Two  # Według przykładu 22 + 3
    elif operator == "-":
        return temporary_Two - temporary_One  # Według przykładu 44 - 52
    elif operator == "*":
        return temporary_One * temporary_Two  # Według przykładu 25 * (-8)
    else:
        return temporary_Two / temporary_One  # Według przykładu -189 / 3


print(Infix_nawias_Eval("( ( 11 + ( ( 22 + 3 ) * ( 44 - 52 ) ) ) / 9 )"))       #Wynik -21
