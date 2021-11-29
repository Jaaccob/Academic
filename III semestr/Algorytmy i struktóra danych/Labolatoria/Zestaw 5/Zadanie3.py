import Stack

Stos = Stack.Stos


def Infix_to_Postfix(string):
    """
    Funkcja przekształca wyrażenie w notacji infixowej na notację postfixową. Zakładamy, że korzystamy z 4 klasycznych
    operatorów tj.:
    - dodawanie
    - odejmowanie
    - mnożenie
    - dzielenie
    :param string: wyrażenie w notacji infoxowej
    :return: zwraca wyrażenie w notacji postfixowej
    """
    stos = Stos()
    for i in string.split():
        if i.isnumeric():
            stos.push(i)
        else:
            temporary_One = stos.pop()
            temporary_Two = stos.pop()
            stos.push("({} {} {})".format(temporary_One, i, temporary_Two))
    return stos.pop()


print(Infix_to_Postfix("20 10 + 75 45 - * 3 /"))
