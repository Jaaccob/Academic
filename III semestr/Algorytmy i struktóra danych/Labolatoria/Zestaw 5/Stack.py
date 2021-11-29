class Stos():
    """
    Klasa <code>Stos</code> odzwierciedla działanie stosu. Klasa ma 5 funkcji ,które definują jak powinna się zachować
    klasa. Klasa działa na tablicy.
    """
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