import Stack

Stos = Stack.Stos


def Postfix_to_Infix(string):
    """
    Funkcja przekształca wyrażenie w notacji postfixowej na notację infixową. Zakładamy, że korzystamy z 4 klasycznych
    operatorów tj.:
    - dodawanie
    - odejmowanie
    - mnożenie
    - dzielenie
    :param string: wyrażenie w notacji postfixowej
    :return: zwraca wyrażenie w notacji infixowej
    """
    stos = Stos()
    temporary_table = ""
    for i in string.split():
        if i.isnumeric():
            temporary_table = "{} {}".format(temporary_table, i)
        elif i in "(+-*/":
            stos.push(i)
        elif i in ")":
            while stos.peek() != "(":
                temporary_table = "{} {}".format(temporary_table, stos.pop())
            stos.pop()
        else:
            return "Błąd w wartościach {}".format(i)
    return temporary_table[1:]


print(Postfix_to_Infix("( ( 20 + 10 ) * ( 75 - 45 ) )"))
