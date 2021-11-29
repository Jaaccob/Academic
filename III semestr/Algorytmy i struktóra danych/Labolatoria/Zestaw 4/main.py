class Stos():
    def __init__(self):
        self.table = []

    def isEmpty(self):  # Sprawdza czy stos jest pusty
        if len(self.table) == 0:
            return True
        else:
            return False

    def push(self, string):  # Dodaje do stosu element
        self.table.append(string)  # Na koniec listy
        # self.table.insert(0, string)  # Na początek listy

    def pop(self):  # Zwraca element z stosu usuwając go z stosu
        return self.table.pop()

    def size(self):  # Zwraca ile stos ma elementów
        return len(self.table)

    def peek(self):  # Zwraca elemenet z stosu nie usuwając go z stosu
        return self.table[len(self.table) - 1]

    """self.table.append(string)  <- czas działania takiej implementacji jest krótszy niż self.table.insert(0, string)
    1 implementacja będzie miała złożoność stałą gdyż dodaje element na sam koniec nie sprawdzając nic
    2 implementacja będzie miała złożoność liniową gdyż po wprowadzeniu konkretnego elementu przesuwa wszystkie elementy o 1 w prawo w tablicy
    """


def poprawnoscNawiasow(Stos, table):
    otwierajacyNawias = ["(", "[", "{"]
    zamykajacyNawias = [")", "]", "}"]
    for i in range(0, len(table)):
        for j in range(0, len(otwierajacyNawias)):
            if table[i] == otwierajacyNawias[j]:
                Stos.push(table[i])
        for j in range(0, len(zamykajacyNawias)):
            if table[i] == zamykajacyNawias[j]:
                if Stos.isEmpty():
                    return i + 1
                if Stos.pop() != otwierajacyNawias[j]:
                    return i + 1

    return Stos.isEmpty()


def ONP(table):
    stos = Stos()
    znak = ["+", "-", "*", "/"]
    for i in range(0, len(table)):
        if ord(table[i]) >= 48 and ord(table[i]) < 58:
            print(table[i], end="")
        if table[i] == "(":
            stos.push("(")
        elif table[i] == ")":
            while stos.peek() != "(":
                print(stos.pop(), end="")
            stos.pop()
        for j in range(0, len(znak)):
            if table[i] == znak[j]:
                stos.push(table[i])
    while stos.isEmpty() == False:
        print(stos.pop(), end="")


def licz(table):
    stos = Stos()
    znak = ["+", "-", "*", "/"]
    auxiliaryBoard = []  # Tablica pomocnicza
    auxiliaryVariableOne = 0  # Pierwsza zmienna pomocnicza
    auxiliaryVariableTwo = 0  # Druga zmienna pomocnicza
    for i in range(0, len(table)):
        if ord(table[i]) >= 48 and ord(table[i]) < 58:  # Sprawdzanie czy table[i] to liczba
            auxiliaryBoard.append(table[i])
        elif table[i] == "(":  # Sprawdzanie czy table[i] to (
            stos.push("(")
        elif table[i] == ")":  # Sprawdzanie czy table[i] to (
            while stos.peek() != "(":
                auxiliaryBoard.append(
                    stos.pop())  # Wpisywanie do tablicy pomocniczej wszystkiego z stosu aż do nawiasu zamykającego
            stos.pop()
        for j in range(0, len(znak)):  # Pętla dla sprawdzenia czy table[i] to znak
            if table[i] == znak[j]:  # Jeśli table[i] to znak[j] to wrzuć go na stos
                stos.push(table[i])
    while stos.isEmpty() == False:  # Pętla do wypisania pozostałych elementów z stosu
        auxiliaryBoard.append(stos.pop())
    for i in range(0, len(auxiliaryBoard)):
        if ord(auxiliaryBoard[i]) >= 48 and ord(
                auxiliaryBoard[i]) < 58:  # Sprawdzanie czy element z auxiliaryBoard (Tablicy pomocniczej) to liczba
            stos.push(auxiliaryBoard[i])  # Jeśli tak to wrzucamy na stos
        if auxiliaryBoard[i] == "+":
            auxiliaryVariableOne = int(stos.pop())
            auxiliaryVariableTwo = int(stos.pop())
            auxiliaryVariableOne += auxiliaryVariableTwo
            stos.push(auxiliaryVariableOne)
        elif auxiliaryBoard[i] == "-":
            auxiliaryVariableOne = int(stos.pop())
            auxiliaryVariableTwo = int(stos.pop())
            auxiliaryVariableTwo -= auxiliaryVariableOne
            stos.push(auxiliaryVariableTwo)
        elif auxiliaryBoard[i] == "*":
            auxiliaryVariableOne = int(stos.pop())
            auxiliaryVariableTwo = int(stos.pop())
            auxiliaryVariableOne *= auxiliaryVariableTwo
            stos.push(auxiliaryVariableOne)
        elif auxiliaryBoard[i] == "/":
            auxiliaryVariableOne = int(stos.pop())
            auxiliaryVariableTwo = int(stos.pop())
            auxiliaryVariableOne /= auxiliaryVariableTwo
            stos.push(auxiliaryVariableOne)
    return stos.pop()


def binarny(Stos, number):
    while number != 0:
        Stos.push(number % 2)
        number = int(number / 2)
    while Stos.isEmpty() == False:
        print(Stos.pop(), end="")


def oktalny(Stos, number):
    while number != 0:
        Stos.push(number % 8)
        number = int(number / 8)
    while Stos.isEmpty() == False:
        print(Stos.pop(), end="")


def heksadecymalny(Stos, number):
    while number != 0:
        if number % 16 == 10:
            Stos.push("A")
        elif number % 16 == 11:
            Stos.push("B")
        elif number % 16 == 12:
            Stos.push("C")
        elif number % 16 == 13:
            Stos.push("D")
        elif number % 16 == 14:
            Stos.push("E")
        elif number % 16 == 15:
            Stos.push("F")
        else:
            Stos.push(number % 16)
        number = int(number / 16)
    while Stos.isEmpty() == False:
        print(Stos.pop(), end="")


def p(w):
    '''
    w = "(123+34)"
    '''
    w = "(" + w + ")"
    znaki = ["^", "*", "/", "+", "-", "("]
    stos = []
    wyjscie = ""

    for i in w:
        if i.isnumeric() == True:
            wyjscie += str(i)

        if i in znaki:
            wyjscie += " "
            stos.append(str(i))

        if i == ")":
            wyjscie += " "
            while stos[-1] != "(":
                wyjscie += stos[-1]
                stos = stos[:-1]

    return wyjscie


p("((2+3)*5)")
p("((2+7)/3+(14-3)*4)/2")


stos = Stos()
# print(poprawnoscNawiasow(stos, "((()))"))
# print(poprawnoscNawiasow(stos, "foo(bar[i)"))
# ONP("((1+(2-3))*4-5)")
print(licz("((1+(2-3))*4-5)"))
print()
# print()
# binarny(stos, 78)
# print()
# oktalny(stos, 78)
# print()
# heksadecymalny(stos, 78)
